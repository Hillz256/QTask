
from django.shortcuts import get_object_or_404, render
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView, DeleteView
)
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from quikTasks.models import Poem

# Create your views here.


class PoemListView(ListView):
    model = Poem
    context_object_name = 'poems_list'
    ordering = ['-date_created']
    paginate_by = 10


class UserPoemListView(ListView):
    model = Poem
    context_object_name = 'poems_list'
    template_name = 'quikTasks/user_poems.html'
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Poem.objects.filter(author=user).order_by('-date_created')


class PoemDetailView(DetailView):
    model = Poem


class PoemCreateView(LoginRequiredMixin, CreateView):
    model = Poem
    fields = ['title', 'category', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PoemUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Poem
    fields = ['title', 'category', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        if self.request.user == self.get_object().author:
            return True
        return False


class PoemDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Poem
    success_url = '/'

    def test_func(self):
        if self.request.user == self.get_object().author:
            return True
        return False
