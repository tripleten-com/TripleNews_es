from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic

from .forms import CommentForm
from .models import Comment, News


class NewsList(generic.ListView):
    """Lista de noticias."""
    model = News
    template_name = 'news/home.html'

    def get_queryset(self):
        """
        Solo mostramos las últimas noticias.

        Su cantidad se determina en la configuración del proyecto.
        """
        return self.model.objects.prefetch_related(
            'comment_set'
        )[:settings.NEWS_COUNT_ON_HOME_PAGE]


class NewsDetail(generic.DetailView):
    model = News
    template_name = 'news/detail.html'

    def get_object(self, queryset=None):
        obj = get_object_or_404(
            self.model.objects.prefetch_related('comment_set__author'),
            pk=self.kwargs['pk']
        )
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['form'] = CommentForm()
        return context


class NewsComment(
        LoginRequiredMixin,
        generic.detail.SingleObjectMixin,
        generic.FormView
):
    model = News
    form_class = CommentForm
    template_name = 'news/detail.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.news = self.object
        comment.author = self.request.user
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        post = self.get_object()
        return reverse('news:detail', kwargs={'pk': post.pk}) + '#comments'


class NewsDetailView(generic.View):

    def get(self, request, *args, **kwargs):
        view = NewsDetail.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = NewsComment.as_view()
        return view(request, *args, **kwargs)


class CommentBase(LoginRequiredMixin):
    """Clase base para trabajar con comentarios."""
    model = Comment

    def get_success_url(self):
        comment = self.get_object()
        return reverse(
            'news:detail', kwargs={'pk': comment.news.pk}
        ) + '#comments'

    def get_queryset(self):
        """El usuario solo puede trabajar con sus propios comentarios."""
        return self.model.objects.filter(author=self.request.user)


class CommentUpdate(CommentBase, generic.UpdateView):
    """Editar un comentario."""
    template_name = 'news/edit.html'
    form_class = CommentForm


class CommentDelete(CommentBase, generic.DeleteView):
    """Eliminar un comentario."""
    template_name = 'news/delete.html'
