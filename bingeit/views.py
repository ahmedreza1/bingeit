import requests
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from bingeit.models import Show, Episode, Tag
from . import models
from django.views.generic.detail import DetailView
from django.db.models import Q
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.http.response import HttpResponseRedirect

#### Normal Pages Related Views ####

class HomeView(TemplateView):
	template_name = "bingeit/home.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		user_shows = Show.objects.order_by('-cr_date')
		context['user_shows'] = user_shows
		return context

class ShowListView(ListView):
	model = Show
	def get_queryset(self):
		si = self.request.GET.get("si")
		if si == None:
			si = ""
		showList = Show.object.filter(Q(title__icontains = si) | Q(description__icontains = si) | Q(cast__icontains = si) | Q(director__icontains = si) | Q(show_type__icontains = si)).order_by("-id");
		return showList

class ShowDetailView(DetailView):
	model = Show