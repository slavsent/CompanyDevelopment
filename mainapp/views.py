from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from mainapp import models as mainapp_models


class MainPageView(TemplateView):
    template_name = "mainapp/index.html"

    def get_context_data(self, **kwargs):
        context = super(MainPageView, self).get_context_data(**kwargs)
        context["company"] = mainapp_models.Company.objects.all()[:5]
        context["develop"] = mainapp_models.Developments.objects.all()
        context["devlp_1"] = mainapp_models.Developments.objects.filter(levels="1")
        context["devlp_2"] = mainapp_models.Developments.objects.filter(levels="2").values_list('parent', flat=True)
        context["devlp_3"] = mainapp_models.Developments.objects.filter(levels="3").values_list('parent', flat=True)
        context["devlp_4"] = mainapp_models.Developments.objects.filter(levels="4").values_list('parent', flat=True)
        context["devlp_5"] = mainapp_models.Developments.objects.filter(levels="5").values_list('parent', flat=True)
        return context


class WorkerPageListView(TemplateView):
    template_name = "mainapp/workers_list.html"

    def get_context_data(self, pk=None, **kwargs):
        context = super(WorkerPageListView, self).get_context_data(**kwargs)
        context["develop"] = get_object_or_404(mainapp_models.Developments, pk=pk)
        context["workers"] = mainapp_models.Worker.objects.filter(development=context["develop"])
        return context


class ContactsPageView(TemplateView):
    pass


class DocSitePageView(TemplateView):
    pass


class LoginPageView(TemplateView):
    pass
