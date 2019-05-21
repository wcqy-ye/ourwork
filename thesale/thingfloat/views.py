from django.shortcuts import render
from django.shortcuts import HttpResponse, render, redirect
from thingfloat import models
from datetime import datetime
from django.views.decorators.http import require_http_methods

# Create your views here.


@require_http_methods(["GET", "POST"])
def things(request):
    tk = request.session.get('user_name')
    if tk:
        number = request.session.get('user_id')
        print(number)
    else:
        return redirect('/loginupin/')
    if request.method == "GET":
        things = models.things.objects.all()
        return render(request, 'things.html', {'things': things})
    else:
        return redirect('/loginupin/')


@require_http_methods(["GET", "POST"])
def detail_thing(request, num):
    tk = request.session.get('user_name')
    if tk:
        number = request.session.get('user_id')
        print(number)
    else:
        return redirect('/loginupin/')
    if request.method == "GET":
        thing = models.things.objects.get(thing_id=num)
        try:
            x = models.things_img.objects.get(img_id=num)
            return render(request, 'detail_thing.html', {'thing': thing, 'imgs': x})
        except:
            error = '没有上传图片哦'
            return render(request, 'detail_thing.html', {'thing': thing ,'error': error})
    else:
        return redirect('/loginupin/')


@require_http_methods(["GET", "POST"])
def publish_thing(request):
    tk = request.session.get('user_name')
    if tk:
        number = request.session.get('user_id')
        print(request.POST.get('img'))
        print(number)
    else:
        return redirect('/loginupin/')
    if request.method == "GET":
        return render(request, 'publish_thing.html')
    else:
        thing_class = request.POST.get('thing_class')
        thing_name = request.POST.get('thing_name')
        thing_description = request.POST.get('thing_description')
        thing_publisher = request.session.get('user_name')
        thing = models.things()
        thing.thing_class = thing_class
        thing.thing_description = thing_description
        thing.thing_publisher = thing_publisher
        thing.thing_name = thing_name

        if thing_class == '' or thing_description == '' or thing_publisher == '' or thing_name == '':

            return render(request, 'publish_thing.html', {
               'error': "不能有要求的字段为空!"
             })
        else:
            try:
                thing.save()
                print(thing.thing_id)
                new_img = models.things_img()
                new_img.img_id = thing.thing_id
                new_img.img = request.FILES.get('img')
                new_img.name = request.FILES.get('img').name
                print(request.FILES.get('img'))
                new_img.save()
                return redirect('/thingfloat/things/')
            except:
                return render(request, 'publish_thing.html', {
                    'error': "出错啦"
                })






