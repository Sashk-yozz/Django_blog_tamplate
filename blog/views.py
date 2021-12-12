from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import News
from django.views.generic import ListView, DeleteView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Вывод статей
class ShowNewsView(ListView):
    model = News
    template_name = 'blog/home.html'
    context_object_name = 'news'
    # Сортировка
    ordering = ['-date']
    # Количество страниц пагинации
    paginate_by = 3

    def get_context_data(self, **kwargs):
        ctx = super(ShowNewsView, self).get_context_data(**kwargs)

        ctx['title'] = 'Главная страница'
        return ctx


# Вывод ссылки пользователя
class UserAllNewsView(ListView):
    model = News
    template_name = 'blog/user_news.html'
    context_object_name = 'news'
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return News.objects.filter(avtor=user).order_by('-date')

    def get_context_data(self, **kwargs):
        ctx = super(UserAllNewsView, self).get_context_data(**kwargs)

        ctx['title'] = f"Статьи от пользователя {self.kwargs.get('username')}"
        return ctx


# Переход на статью
class NewsDetailView(DeleteView):
    model = News
    template_name = 'blog/news_detail.html'
    context_object_name = 'post'

    # Берет название для титульной страницы из титула статьи
    def get_context_data(self, **kwards):
        ctx = super(NewsDetailView, self).get_context_data(**kwards)

        ctx['title'] = News.objects.get(pk=self.kwargs['pk'])
        return ctx


# Добавляет статьи через сайт
class CreateNewsView(LoginRequiredMixin, CreateView):
    model = News
    template_name = 'blog/create_news.html'

    fields = ['title', 'text']

    # Берет название для титульной страницы из титула статьи
    def get_context_data(self, **kwards):
        ctx = super(CreateNewsView, self).get_context_data(**kwards)

        ctx['title'] = 'Добавление статьи'
        ctx['btn_text'] = 'Добавить статью'
        return ctx

    def form_valid(self, form):
        form.instance.avtor = self.request.user
        return super().form_valid(form)


# Обновление статьи на сайте
class UpdateNewsView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = News
    template_name = 'blog/create_news.html'

    fields = ['title', 'text']

    # Берет название для титульной страницы из титула статьи
    def get_context_data(self, **kwards):
        ctx = super(UpdateNewsView, self).get_context_data(**kwards)

        ctx['title'] = 'Обновление статьи'
        ctx['btn_text'] = 'Обновить статью'
        return ctx

    # Не автор статьи не может редактировать статью
    def test_func(self):
        news = self.get_object()
        if self.request.user == news.avtor:
            return True

        return False

    def form_valid(self, form):
        form.instance.avtor = self.request.user
        return super().form_valid(form)


class DeleteNewsView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = News
    success_url = '/'
    template_name = 'blog/delete-news.html'

    # Не автор статьи не может удалить статью
    def test_func(self):
        news = self.get_object()
        if self.request.user == news.avtor:
            return True

        return False


def contacts(request):
    return render(request, 'blog/contacts.html', {'title': 'Страница контакты'})


def about(request):
    return render(request, 'blog/about.html', {'title': 'О нас'})
