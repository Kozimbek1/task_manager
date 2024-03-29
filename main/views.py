from django.shortcuts import render, redirect
from django.contrib.auth import logout

from .forms import TaskForm
from .models import Task


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'index.html', {'title': 'Главная страница сайта', 'tasks': tasks})



def create(request):
    error = ''
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Ошибка!!!'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'create.html', context)


from django.shortcuts import redirect, get_object_or_404
from .models import Task

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('home')


from django.shortcuts import render, redirect
from django.views import View

class RegistrationView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        # Получаем данные из формы
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        # Проверяем совпадение с предопределенными значениями
        if (username == 'q' and
            password == 'q'):
            # first_name == 'q' and
            # last_name == 'q'):
            # Перенаправляем на главную страницу
            return redirect('home')  # Замените 'home' на имя вашего URL для главной страницы
        else:
            # Если данные не совпадают, вы можете вернуть ошибку или отобразить сообщение об ошибке
            return render(request, 'register.html', {'error_message': 'Неверные данные. Пожалуйста, попробуйте еще раз.'})



def log(request):
    return redirect('/accounts/login')

def show_prof(request):
    return render(request, 'profile.html')

def logout_view(request):
    logout(request)
    return redirect('/home')

