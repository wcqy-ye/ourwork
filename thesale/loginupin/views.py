from django.conf.urls import url
from django.shortcuts import HttpResponse, render, redirect
from loginupin import models
from datetime import datetime
from django.views.decorators.http import require_http_methods
# Create your views here.


@require_http_methods(["GET", "POST"])
def loginin(request):
    if request.method == "GET":
        return render(request, 'loginin.html')
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        result = models.users.objects.filter(user_email=email, user_password=password).first()
        if result:
            request.session['is_login'] = True
            request.session['user_id'] = result.user_id
            request.session['user_name'] = result.user_name
            tk = request.session.get('user_name')
            print(tk)
            return redirect('/loginupin/signup/')
        else:
            return render(request, 'loginin.html')


@require_http_methods(["GET", "POST"])
def signup(request):
    if request.method == "GET":
        return render(request, 'signup.html')
    if request.method == "POST":
        name = request.POST.get("name", None)
        email = request.POST.get("email", None)
        phone = request.POST.get("phone", None)
        password = request.POST.get("password", None)
        if name != None and email != None and password != None and phone != None:
            models.users.objects.create(user_name=name, user_email=email, user_phone=phone, user_password=password)
            return redirect('/loginupin/')
        else:
            return render(request, "signup.html")


@require_http_methods(["GET", "POST"])
def blank(request):
    tk = request.session.get('user_name')
    if tk:
        return render(request , "blank.html")
    else:
        return redirect('/loginupin/')


@require_http_methods(["GET", "POST"])
def self(request):
    if request.method == 'GET':
        tk = request.session.get('user_name')
        if tk:
            return render(request, "self.html")
        else:
            return redirect('/loginupin/')
    else:
        print(request.FILES.get('img').name)
        new_img = models.IMG(
            img=request.FILES.get('img'),
            name=request.FILES.get('img').name
        )
        new_img.save()
    return redirect('/loginupin/show/')


@require_http_methods(["GET"])
def showImg(request):
    tk = request.session.get('user_name')
    if tk:
    #"""
   # 图片显示
   #:param request:
   # :return:
   # """
        imgs = models.IMG.objects.all()
        content = {
        'imgs': imgs,
        }
        for i in imgs:
            print(i.img.url)
        return render(request, 'show.html', content)
    else:
        redirect('/loginupin/')


@require_http_methods(["GET", "POST"])
def changepwd(request):
    if request.method == "GET":
        tk = request.session.get('user_name')
        if tk:
            return render(request, "changepwd.html")
        else:
            return redirect('/loginupin/')
    else:
        pwd1 = request.POST.get('pwd1')
        pwd2 = request.POST.get('pwd2')
        number = request.session.get('user_id')
        print(pwd1, pwd2, number)
        try:
            obj = models.users.objects.get(user_password=pwd1, user_id=number)
            obj.user_password = pwd2
            obj.save()
            result = '修改成功！'
            return render(request, "changepwd.html", {'result': result})
        except:
            result = '确认旧密码正确！'
            return render(request, "changepwd.html", {'result': result})


@require_http_methods(["GET", "POST"])
def changebulk(request):
    tk = request.session.get('user_name')
    if tk:
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        number = request.session.get('user_id')
        print(name, phone, number)
    else:
        return redirect('/loginupin/')
    if request.method == "GET":
        return render(request, "changebulk.html")
    else:
        try:
            obj = models.users.objects.get(user_id=number)
            obj.user_name = name
            obj.user_phone = phone
            obj.save()
            result = '修改成功！'
            return render(request, "changebulk.html", {'result': result})
        except:
            result = '修改失败！'
            return render(request, "changebulk.html", {'result': result})


@require_http_methods(["GET"])
def comment(request):
    tk = request.session.get('user_name')
    if tk:
        number = request.session.get('user_id')
        print(number)
    else:
        return redirect('/loginupin/')
    messages = models.comment.objects.all()
    return render(request, 'comment.html', {'messages': messages})


@require_http_methods(["GET", "POST"])
def tocomment(request):
    tk = request.session.get('user_name')
    if tk:
        number = request.session.get('user_id')
        print(number)
    else:
        return redirect('/loginupin/')
    if request.method == "GET":
        return render(request, 'tocomment.html')
    else:
        try:
            content = request.POST.get('content')
            print(content)
            x = models.comment()
            x.comment_id = request.session.get('user_id')
            x.comment_or = request.session.get('user_name')
            x.comment_time = datetime.now()
            print(x.comment_time)
            print(1)
            x.comments = content
            #x = models.comment(comment_id=comment_id,comment_or=comment_or,comment_time=comment_time,comments=comments)
            print(x)
        finally:
            x.save()
            print(1)
            return redirect('/loginupin/comment/')








