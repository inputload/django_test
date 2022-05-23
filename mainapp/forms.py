from django import forms  # Импортируем класс формы


class AddPostForm(forms.Form):  # Создаем класс формы для поста
    title = forms.CharField(max_length=255)  # Поле заголовка (строка)
    text = forms.CharField()  # Поле описания (строка)
    price = forms.FloatField()  # Поле цены (число с плавающей точкой)
