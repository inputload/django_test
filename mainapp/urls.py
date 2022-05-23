from django.urls import path
from .views import \
    (MainPageView, Login, logout_func, RegistrationView, Profile, AddPost)
# Имортировали класс который отвечает за конкретный маршрут

urlpatterns = [
    path('', MainPageView.as_view()),
    path('login/', Login.as_view()),
    path('logout/', logout_func),
    path('registration/', RegistrationView.as_view()),
    path('profile/', Profile.as_view()),

    path('add_post/', AddPost.as_view()),  # Прописали путь, по которому пользователь
    # может получить страницу, и подключили класс за нее отвечающий
]