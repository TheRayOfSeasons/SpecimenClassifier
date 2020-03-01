from django.shortcuts import render
from django.views import View


class ReportView(View):
    """
    A custom generic view for reports.
    """

    report_class = None

    def get(self, request, *args, **kwargs):
        if self.report_class:
            return self.report_class.generate()
        else:
            raise('No report_class supplied.')
