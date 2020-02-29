from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.template.defaultfilters import slugify

from django.views.generic import (
    ListView, DetailView,
    CreateView, DeleteView,
    UpdateView, DeleteView
    )

from .models import Draft, Post
# Create your views here.

def home(request):
    return render(request, 'home.html')

class DraftListView(ListView):
    model = Draft
    #context_object_name = 'reports'
    template_name = 'drafts/draft_list.html'
    ordering = ['-date_created']

    def get_queryset(self):
        return Draft.objects.filter(author=self.request.user.pk )

class DraftDetailView(DetailView):
    model = Draft
    template_name = "drafts/draft_detail.html"

class DraftCreateView(LoginRequiredMixin, CreateView):
    model = Draft
    template_name = 'drafts/draft_form.html'
    
    fields = ['title', 'body', 'tags']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)


class DraftUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Draft
    template_name = 'drafts/draft_form.html'
    fields = ['title', 'body', 'tags']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)

    def test_func(self):
        draft = self.get_object()
        if self.request.user == draft.author:
            return True
        return False


class DraftDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Draft
    template_name = "drafts/draft_confirm_delete.html"
    success_url = '/'
    
    def test_func(self):
        draft = self.get_object()
        if self.request.user == draft.author:
            return True
        return False
