from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)

from core.helpers import slicedict
from core.helpers import to_dictionary_list
from core.reports import AllSpecimens
from core.views import ReportView
from direction.forms import (
    NorthDetailsForm,
    EastDetailsForm,
    WestDetailsForm,
    SouthDetailsForm,
)
from direction.models import (
    NorthDetails,
    EastDetails,
    WestDetails,
    SouthDetails,
    NorthOrganism,
    EastOrganism,
    WestOrganism,
    SouthOrganism,
    NorthImages,
    EastImages,
    WestImages,
    SouthImages,
)
from direction.models import StateOfDecay
from direction.models import Texture
from epiphytes.models import EpiphyticOrganism
from trees.models import Tree

from .models import (
    Specimen,
    Location
)
from .forms import (
    SpecimenForm,
    LocationForm,
)


class GenerateAllSpecimensView(ReportView):
    report_class = AllSpecimens


class CreateSpecimenView(CreateView):
    """
    Form view for adding specimens.
    """

    model = Specimen
    form_class = SpecimenForm
    template_name = 'specimen/create-specimen.html'

    def get_success_url(self):
        return reverse_lazy('specimen:detail',
            kwargs={'pk': self.object.pk})


class SpecimenListView(ListView):
    """
    Lists all specimens.
    """

    model = Specimen
    template_name = 'specimen/list-specimen.html'


class SpecimenDetailView(DetailView):
    """
    Detail view for specimens.
    """

    model = Specimen
    template_name = 'specimen/detail-specimen.html'

    def get_context_data(self, **kwargs):
        context = super(SpecimenDetailView, self).get_context_data(**kwargs)

        pk = self.kwargs['pk']
        specimen = Specimen.objects.get(id=pk)

        try:
            context['north_details'] = NorthDetails.objects.get(specimen=specimen)
        except NorthDetails.DoesNotExist:
            context['north_details'] = None

        try:
            context['east_details'] = EastDetails.objects.get(specimen=specimen)
        except EastDetails.DoesNotExist:
            context['east_details'] = None

        try:
            context['west_details'] = WestDetails.objects.get(specimen=specimen)
        except WestDetails.DoesNotExist:
            context['west_details'] = None

        try:
            context['south_details'] = SouthDetails.objects.get(specimen=specimen)
        except SouthDetails.DoesNotExist:
            context['south_details'] = None

        context['north_organisms'] = [
            i.epiphytic_organism for i in specimen.northorganism_set.all()]
        context['east_organisms'] = [
            i.epiphytic_organism for i in specimen.eastorganism_set.all()]
        context['west_organisms'] = [
            i.epiphytic_organism for i in specimen.westorganism_set.all()]
        context['south_organisms'] = [
            i.epiphytic_organism for i in specimen.southorganism_set.all()]

        return context


class UpdateSpecimenView(UpdateView):
    """
    View for updating specimens.
    """

    model = Specimen
    form_class = SpecimenForm
    template_name = 'specimen/update-specimen.html'

    def get_success_url(self):
        return reverse_lazy('specimen:detail',
            kwargs={'pk': self.object.pk})


class SpecimenDeleteView(DeleteView):
    """
    View for deleting specimens.
    """

    model = Specimen

    def get_success_url(self, **kwargs):
        return reverse_lazy('specimen:list')

class AddDirectionDetailsView(View):
    template_name = 'specimen/direction-details.html'

    def get_organism_pks(self, post_request, direction):
        return list(
            slicedict(
                post_request,
                f'{direction}Epiphyte',
                removeEmpty=True)
            .values()
        )

    def save_organisms(self, specimen, organisms_set, organism_model):
        for organism_pk in organisms_set:
            organism = EpiphyticOrganism.objects.get(id=organism_pk)
            organism_object = organism_model.objects.get_or_create(
                specimen=specimen, epiphytic_organism=organism)

    def delete_excluded_organisms(self, specimen):
        north_organisms = specimen.northorganism_set.all()
        east_organisms = specimen.eastorganism_set.all()
        west_organisms = specimen.westorganism_set.all()
        south_organisms = specimen.southorganism_set.all()

        for organisms, model in [
                    (north_organisms, NorthOrganism),
                    (east_organisms, EastOrganism),
                    (west_organisms, WestOrganism),
                    (south_organisms, SouthOrganism)
                ]:
            self.delete_organisms(organisms, model)

    def delete_organisms(self, organisms, model):
        for organism in organisms:
            for organism in organisms:
                model.objects.filter(id=organism.pk).delete()

    def save_details(self, specimen, north, east, west, south):
        for direction, model in [
                    (north, NorthDetails),
                    (east, EastDetails),
                    (west, WestDetails),
                    (south, SouthDetails),
                ]:
            details, created = model.objects.get_or_create(specimen=specimen)
            if direction['ph_level_1']:
                details.ph_level_1 = direction['ph_level_1']
            if direction['ph_level_2']:
                details.ph_level_2 = direction['ph_level_2']
            if direction['ph_level_3']:
                details.ph_level_3 = direction['ph_level_3']
            if direction['state_of_decay']:
                details.state_of_decay = direction['state_of_decay']
            if direction['texture']:
                details.texture = direction['texture']
            details.stain = True if direction['stain'] == 'on' else False
            details.save()

    def get(self, request, pk, *args, **kwargs):
        context = {}
        specimen = Specimen.objects.get(id=pk)
        epiphytes = EpiphyticOrganism.objects.all()

        context['epiphytes'] = epiphytes

        try:
            north_details = NorthDetails.objects.get(specimen=specimen)
        except NorthDetails.DoesNotExist:
            north_details = None

        try:
            east_details = EastDetails.objects.get(specimen=specimen)
        except EastDetails.DoesNotExist:
            east_details = None

        try:
            west_details = WestDetails.objects.get(specimen=specimen)
        except WestDetails.DoesNotExist:
            west_details = None

        try:
            south_details = SouthDetails.objects.get(specimen=specimen)
        except:
            south_details = None

        if north_details:
            context['north_details'] = north_details
        if east_details:
            context['east_details'] = north_details
        if west_details:
            context['west_details'] = north_details
        if south_details:
            context['south_details'] = north_details

        context['north_organisms'] = [
            i.epiphytic_organism.pk for i in specimen.northorganism_set.all()]
        context['east_organisms'] = [
            i.epiphytic_organism.pk for i in specimen.eastorganism_set.all()]
        context['west_organisms'] = [
            i.epiphytic_organism.pk for i in specimen.westorganism_set.all()]
        context['south_organisms'] = [
            i.epiphytic_organism.pk for i in specimen.southorganism_set.all()]

        context['state_of_decay_choices'] = to_dictionary_list(StateOfDecay.choices)
        context['texture_choices'] = to_dictionary_list(Texture.choices)

        return render(request, self.template_name, context=context)

    def post(self, request, pk, *args, **kwargs):
        specimen = Specimen.objects.get(id=pk)

        north_ph_1 = request.POST.get('northPH1')
        north_ph_2 = request.POST.get('northPH2')
        north_ph_3 = request.POST.get('northPH3')
        north_state_of_decay = request.POST.get('northStateOfDecay')
        north_texture = request.POST.get('northTexture')
        north_stain = request.POST.get('northStain')

        east_ph_1 = request.POST.get('eastPH1')
        east_ph_2 = request.POST.get('eastPH2')
        east_ph_3 = request.POST.get('eastPH3')
        east_state_of_decay = request.POST.get('eastStateOfDecay')
        east_texture = request.POST.get('eastTexture')
        east_stain = request.POST.get('eastStain')

        west_ph_1 = request.POST.get('westPH1')
        west_ph_2 = request.POST.get('westPH2')
        west_ph_3 = request.POST.get('westPH3')
        west_state_of_decay = request.POST.get('westStateOfDecay')
        west_texture = request.POST.get('westTexture')
        west_stain = request.POST.get('westStain')

        south_ph_1 = request.POST.get('southPH1')
        south_ph_2 = request.POST.get('southPH2')
        south_ph_3 = request.POST.get('southPH3')
        south_state_of_decay = request.POST.get('southStateOfDecay')
        south_texture = request.POST.get('southTexture')
        south_stain = request.POST.get('southStain')

        north_details = {
            'ph_level_1': north_ph_1,
            'ph_level_2': north_ph_2,
            'ph_level_3': north_ph_3,
            'state_of_decay': north_state_of_decay,
            'texture': north_texture,
            'stain': north_stain,
        }
        east_details = {
            'ph_level_1': east_ph_1,
            'ph_level_2': east_ph_2,
            'ph_level_3': east_ph_3,
            'state_of_decay': east_state_of_decay,
            'texture': east_texture,
            'stain': east_stain,
        }
        west_details = {
            'ph_level_1': west_ph_1,
            'ph_level_2': west_ph_2,
            'ph_level_3': west_ph_3,
            'state_of_decay': west_state_of_decay,
            'texture': west_texture,
            'stain': west_stain,
        }
        south_details = {
            'ph_level_1': south_ph_1,
            'ph_level_2': south_ph_2,
            'ph_level_3': south_ph_3,
            'state_of_decay': south_state_of_decay,
            'texture': south_texture,
            'stain': south_stain,
        }

        self.save_details(
            specimen,
            north_details,
            east_details,
            west_details,
            south_details
        )

        north_organisms_pks = self.get_organism_pks(request.POST, 'north')
        east_organisms_pks = self.get_organism_pks(request.POST, 'east')
        west_organisms_pks = self.get_organism_pks(request.POST, 'west')
        south_organisms_pks = self.get_organism_pks(request.POST, 'south')

        self.delete_excluded_organisms(specimen)

        for organism_set, organism_model in [
                    (north_organisms_pks, NorthOrganism),
                    (east_organisms_pks, EastOrganism),
                    (west_organisms_pks, WestOrganism),
                    (south_organisms_pks, SouthOrganism)
                ]:
            self.save_organisms(specimen, organism_set, organism_model)

        return HttpResponseRedirect(reverse_lazy('specimen:detail',
            args=[pk]))


class SpecimenSamplesFormView(View):
    template_name = 'specimen/direction-samples.html'

    def segregate_images(self, post_request, direction):
        return list(
            slicedict(
                post_request,
                f'{direction}Image',
                removeEmpty=True)
            .values()
        )

    def get(self, request, pk, *args, **kwargs):
        specimen = Specimen.objects.get(id=pk)
        return render(request, self.template_name, context={})

    def post(self, request, pk, *args, **kwargs):
        specimen = Specimen.objects.get(id=pk)

        north_images = self.segregate_images(request.FILES, 'north')
        east_images = self.segregate_images(request.FILES, 'east')
        west_images = self.segregate_images(request.FILES, 'west')
        south_images = self.segregate_images(request.FILES, 'south')

        for images, model in [
                    (north_images, NorthImages),
                    (east_images, EastImages),
                    (west_images, WestImages),
                    (south_images, SouthImages),
                ]:
            if len(images) > 0:
                for image in images:
                    direction_image, created = (
                        model.objects.get_or_create(
                            specimen=specimen, image=image))
                    direction_image.save()

        return HttpResponseRedirect(reverse_lazy('specimen:detail',
            args=[pk]))


class NorthDeleteSampleImageView(DeleteView):
    model = NorthImages

    def get_success_url(self, **kwargs):
        return reverse_lazy('specimen:detail',
            kwargs={'pk': self.object.specimen.pk })


class EastDeleteSampleImageView(DeleteView):
    model = EastImages

    def get_success_url(self, **kwargs):
        return reverse_lazy('specimen:detail',
            kwargs={'pk': self.object.specimen.pk })


class WestDeleteSampleImageView(DeleteView):
    model = WestImages

    def get_success_url(self, **kwargs):
        return reverse_lazy('specimen:detail',
            kwargs={'pk': self.object.specimen.pk })


class SouthDeleteSampleImageView(DeleteView):
    model = SouthImages

    def get_success_url(self, **kwargs):
        return reverse_lazy('specimen:detail',
            kwargs={'pk': self.object.specimen.pk })


class AddLocationView(CreateView):
    """
    Form view for adding locations.
    """

    template_name = 'specimen/add-location.html'
    model = Location
    form_class = LocationForm
