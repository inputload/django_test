from django.contrib.auth import logout, authenticate, login, get_user_model
from django.shortcuts import render, redirect
from django.views import View

from mainapp.models import Post
from mainapp.forms import AddPostForm  # Импортировали форму

User = get_user_model()


class MainPageView(View):

    def get(self, request):
        context = {
            'posts': Post.objects.all().order_by('-id')
        }
        return render(request, 'main_page.html', context)


class Login(View):

    def get(self, request):
        if request.user.is_anonymous:
            return render(request, 'login.html')
        else:
            return redirect('/')

    def post(self, request):
        user = authenticate(
            username=User.objects.get(email=request.POST.get('email')).username,
            password=request.POST.get('password')
        )
        print(user)
        print(request.POST)
        if user:
            login(request, user)
            return redirect('/')
        return render(request, 'login.html', {"error": "Что-то не так"})


def logout_func(request):
    logout(request)
    return redirect('/login')


class RegistrationView(View):

    def get(self, request):
        if request.user.is_anonymous:
            return render(request, 'registration.html')
        else:
            return redirect('/')

    def post(self, request):
        data = dict(request.POST)
        if data.get('password') == data.get('re_password'):
            user = User.objects.create(
                first_name=data.get('first_name'),
                last_name=data.get('last_name'),
                username=data.get('username'),
                email=data.get('email'),
                password=data.get('password'),
            )
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'registration.html', {'re_password': "Не совпадают"})


class Profile(View):

    def get(self, request):
        if not request.user.is_anonymous:
            return render(request, 'profile.html')
        else:
            return redirect('/login')

    def post(self, request):
        user = request.user
        # users = user.__class__.objects.filter(pk=user.pk)
        # users.update(**request.POST)
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.save()
        return redirect('/')


class AddPost(View):  # Создали класс который отвечает за страницу добавления поста

    def get(self, request):  # Функция которая вызывается когда получаем GET-запрос
        # Используем для отправки страницы в браузер пользователя

        if request.user.is_anonymous:
            return redirect('/login')
        form = AddPostForm()  # Создали экземпляр формы
        context = {'form': form}  # Поместили в словарь контекста который передадим в страниц

        return render(request, 'add_post.html', context=context)  # Возвращаем готовую HTML-страницу

    def post(self, request):  # Функция которая вызывается когда получаем POST-запрос
        # Используем для приема данных от пользователя
        form = AddPostForm(data=request.POST)  # Создали объект формы
        # который сразу заполнили данными из POST-запроса

        if form.is_valid():  # Если форма валидна (Если все поля прошли валидацию)
            Post.objects.create(
                owner=request.user,
                **form.cleaned_data
            )  # Создали объект поста с данными которые мы передали в форме
            return redirect('/')

        else:  # Если форма не валида (Если хотя бы одно поле не прошло валидацию)
            context = {'form': form}  # Поместили в словарь контекст который передадим в страницу
            return render(request, 'add_post.html', context=context) # Возвращаем готовую HTML-страницу
