from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime
import os



def home_view(request):
    template_name = 'app/home.html'

    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.datetime.now().time()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    work_dir = os.listdir(path=r'C:\Users\Home\Desktop\Speshilov\HW_django')
    data = ''
    for files in work_dir:
        data += f'<div>{files}</dev>'
    return HttpResponse(data)

