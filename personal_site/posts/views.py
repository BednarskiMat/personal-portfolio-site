from django.shortcuts import render
from django.views.generic import ListView
from .models import Project
from .models import Job
from .models import Skill
from django.views.generic import TemplateView
class HomePageView(ListView):
    model = Project
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        ctx = super(HomePageView, self).get_context_data(**kwargs)
        ctx['jobs'] = Job.objects.all()
        ctx['skills'] = Skill.objects.all()
        return ctx
