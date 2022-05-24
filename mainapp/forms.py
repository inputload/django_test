from django import forms  # Импортируем класс формы
from django.contrib.auth import get_user_model

from mainapp.models import Post

User = get_user_model()

# class AddPostForm(forms.Form):  # Создаем класс формы для поста
#     title = forms.CharField(max_length=255)  # Поле заголовка (строка)
#     text = forms.CharField(widget=forms.Textarea)  # Поле описания (строка)
#     price = forms.FloatField()  # Поле цены (число с плавающей точкой)


class AddPostForm(forms.ModelForm):  # Создаем класс формы для поста
    class Meta:  # Переопределяем класс Мета
        model = Post  # Подключаем нужную нам модель к форме
        fields = ('title', 'text', 'price')  # Указываем какие поля используем

    def clean(self):
        Post.objects.create(
            owner=User.objects.get(pk=1),
            **self.cleaned_data
        )
        return super(AddPostForm, self).clean()