import requests
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from bingeit.models import Show, Episode, Tag, Banner
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
		home_shows = Show.objects.order_by('-cr_date')
		home_banner = Banner.objects.order_by('-id')
		context['home_shows'] = home_shows
		context['home_banner'] = home_banner
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
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		show_tags = Tag.objects.filter(show_id=self.kwargs['pk']).order_by('id')
		show_episodes = Episode.objects.filter(show_id=self.kwargs['pk']).order_by('-id')
		context['show_tags'] = show_tags
		context['show_episodes'] = show_episodes
		return context