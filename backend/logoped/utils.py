from django.db.models import Count

from .models import Category

menu = [{'title': "Главная", 'url_name': 'home'},
        {'title': "О сайте", 'url_name': 'about'},
        {'title': "Обратная связь", 'url_name': 'contact'}]


class DataMixin:
    paginate_by = 20

    @staticmethod
    def get_user_context(**kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('publication'))

        user_menu = menu.copy()
        # if not self.request.user.is_authenticated:
        #     user_menu.pop(1)

        context['menu'] = user_menu

        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
