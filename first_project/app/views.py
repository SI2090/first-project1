from django.http import HttpResponse
from django.shortcuts import render, reverse


def home_view(request):
    template_name = 'app/home.html'

    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time_view'),
        'Показать содержимое рабочей директории': reverse('workdir_view')
    }
    
    context = {
        'pages': pages
    }
    return render(request, template_name, context)

def time_view(request):
    current_time = None
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    files = os.listdir()
    files_str = ", ".join(files)
    return HttpResponse(f'Файлы в текущей директории: {files_str}')

    raise NotImplemented
