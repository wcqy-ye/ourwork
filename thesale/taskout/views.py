from django.shortcuts import render
from django.shortcuts import HttpResponse, render, redirect
from taskout import models
from datetime import datetime
from django.views.decorators.http import require_http_methods

# Create your views here.

@require_http_methods(["GET", "POST"])
def tasks(request):
    tk = request.session.get('user_name')
    if tk:
        number = request.session.get('user_id')
        print(number)
    else:
        return redirect('/loginupin/')
    if request.method == "GET":
        tasks = models.tasks.objects.all()
        return render(request, 'tasks.html', {'tasks': tasks})
    else:
        return redirect('/loginupin/')


@require_http_methods(["GET", "POST"])
def detail_task(request, num):
    tk = request.session.get('user_name')
    if tk:
        number = request.session.get('user_id')
        print(number)
    else:
        return redirect('/loginupin/')
    if request.method == "GET":
        task = models.tasks.objects.get(task_id=num)
        try:
            x = models.tasks_img.objects.get(img_id=num)
            return render(request, 'detail_task.html', {'task': task, 'imgs': x})
        except:
            error = '没有上传图片哦'
            return render(request, 'detail_task.html', {'task': task ,'error': error})
    else:
        return redirect('/loginupin/')


@require_http_methods(["GET", "POST"])
def publish_task(request):
    tk = request.session.get('user_name')
    if tk:
        number = request.session.get('user_id')
        print(number)
    else:
        return redirect('/loginupin/')
    if request.method == "GET":
        return render(request, 'publish_task.html')
    else:
        task_class = request.POST.get('task_class')
        task_name = request.POST.get('task_name')
        task_description = request.POST.get('task_description')
        task_publisher = request.session.get('user_name')
        task = models.tasks()
        task.task_class = task_class
        task.task_description = task_description
        task.task_publisher = task_publisher
        task.task_name = task_name
        if task_class == '' or task_description == '' or task_publisher == '' or task_name == '':

            return render(request, 'publish_task.html', {
                'error': "不能有要求的字段为空!"
            })
        else:
            try:
                task.save()
                print(task.task_id)
                new_img = models.tasks_img()
                new_img.img_id = task.task_id
                new_img.img = request.FILES.get('img')
                new_img.name = request.FILES.get('img').name
                print(request.FILES.get('img'))
                new_img.save()
                return redirect('/taskout/tasks/')
            except:
                return render(request, 'publish_task.html', {
                    'error': "出错啦"
                })
        


