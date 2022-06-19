from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView


from .forms import ContactForm
from .models import *
from .utils import *


class LogopedHome(DataMixin, ListView):
    paginate_by = 5
    model = Publication
    template_name = 'logoped/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Publication.objects.filter(is_published=True).select_related('category')


class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'logoped/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Обратная связь")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        return redirect('home')


class ShowPost(DataMixin, DetailView):
    model = Publication
    template_name = 'logoped/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


class PublicationCategory(DataMixin, ListView):
    model = Publication
    template_name = 'logoped/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Publication.objects.filter(category__slug=self.kwargs['cat_slug'],
                                          is_published=True).select_related('category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title='Категория - ' + str(c.name),
                                      category_selected=c.pk)
        return dict(list(context.items()) + list(c_def.items()))


def about(request):
    return render(request, 'logoped/about.html', {'menu': menu, 'title': 'О сайте'})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

