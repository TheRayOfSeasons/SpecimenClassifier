import xlwt
import datetime

from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse

from specimen.models import Specimen


class AllSpecimens:

    @staticmethod
    def generate():
        wb = xlwt.Workbook()
        sheet = wb.add_sheet('Sheet1', cell_overwrite_ok=True)
        font = xlwt.Font()
        header_font = xlwt.Font()
        header_font.bold = True
        alignment = xlwt.Alignment()
        alignment.horz = xlwt.Alignment.HORZ_CENTER
        style = xlwt.XFStyle()
        header_style = xlwt.XFStyle()
        style.alignment = alignment
        style.font = font
        header_style.font = header_font

        specimens = Specimen.objects.all()
        initial_row = 1
        data_row = initial_row

        headers = [
            'Specimen Code Number',
            'Name',
            'Host Tree',
            'Location',
            'Latitude',
            'Longhitude',
            'DBH',
            'Collection Date',
            'Direction',
            '1st',
            '2nd',
            '3rd',
            'Average',
            'Epiphytic Organisms',
            'State of Decay',
            'Bark Texture',
            'Filter Paper',
        ]

        for hcol, hcol_data in enumerate(headers):
            sheet.write(0, hcol, hcol_data, header_style)

        for specimen in specimens:
            col = 0
            row_data = [
                specimen.code,
                specimen.name,
                specimen.host_tree.name,
                specimen.location.name,
                specimen.latitude,
                specimen.longhitude,
                specimen.dbh,
                specimen.collection_date.strftime('%B %d, %Y'),
            ]

            for data in row_data:
                sheet.write_merge(
                    data_row,
                    data_row + 3, col, col, data, style)
                col += 1

            for i, direction in enumerate(['N', 'E', 'W', 'S']):
                sheet.write(data_row + i, col, direction, style)
            
            col += 1

            for row, data in enumerate([
                        specimen.northdetails,
                        specimen.eastdetails,
                        specimen.westdetails,
                        specimen.southdetails
                    ]):
                direction_col = col
                for ph_level in [
                            data.ph_level_1,
                            data.ph_level_2,
                            data.ph_level_3,
                            data.average_ph
                        ]:
                    if ph_level:
                        sheet.write(data_row + row, direction_col, ph_level, style)
                    direction_col += 1

            col += 4
            stain = ''
            if specimen.stain is True:
                stain = '+'
            elif specimen.stain is False:
                stain = '-'

            post_row_data = [
                ', '.join(specimen.get_distinct_organisms),
                # specimen.get_state_of_decay_display(),
                specimen.get_bark_texture_display(),
                stain
            ]

            for data in post_row_data:
                sheet.write_merge(
                    data_row,
                    data_row + 3, col, col, data, style)
                col += 1

            data_row += 4

        today = datetime.date.today()
        filename = 'Tree Bark Collection-{}'.format(today)
        response = HttpResponse(content_type="application/vnd.ms-excel")
        response['Content-Disposition'] = \
            'attachment; filename=%s.xls' % filename
        wb.save(response)
        return response
