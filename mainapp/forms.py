from django import forms  # Импортируем класс формы
from mainapp.models import Post


# class AddPostForm(forms.Form):  # Создаем класс формы для поста
#     title = forms.CharField(max_length=255)  # Поле заголовка (строка)
#     text = forms.CharField(widget=forms.Textarea)  # Поле описания (строка)
#     price = forms.FloatField()  # Поле цены (число с плавающей точкой)


class AddPostForm(forms.ModelForm):  # Создаем класс формы для поста
    class Meta:  # Переопределяем класс Мета
        model = Post  # Подключаем нужную нам модель к форме
        fields = ('title', 'text', 'price')  # Указываем какие поля используем
