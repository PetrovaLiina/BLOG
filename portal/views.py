from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Portal, Category
from .forms import PostForm



class HomePortal(ListView):
    paginate_by = 3
    model = Portal
    template_name = 'portal/portal_post_list.html'
    context_object_name = 'portal'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return Portal.objects.filter(is_published=True)


class PortalByCategory(ListView):
    model = Portal
    template_name = 'portal/portal_post_list.html'
    context_object_name = 'portal'
    paginate_by = 3

    def get_queryset(self):
        return Portal.objects.filter(category_id=self.kwargs['category_id'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    allow_empty = False


class ViewPost(DetailView):
    model = Portal
    # pk_url_kwarg = 'post_id'
    context_object_name = 'post_item'


def about(request):
    return render(request, 'portal/about.html')


class CreatePost(CreateView):
    form_class = PostForm
    template_name = 'portal/add_post.html'
    success_url = reverse_lazy('main')
