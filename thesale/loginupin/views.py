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
            return redirect('/loginupin/blank/')
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
        tk = request.session.get('user_name')
        if tk:
            if request.method == 'GET':
                tk = request.session.get('user_id')
                user = models.users.objects.get(user_id=tk)
                print(user.user_name)
                print(user.user_email)
                print(user.user_money)
                try:
                    x = request.session.get('user_id')
                    imgs = models.IMG.objects.get(img_id=x)
                    imgs = {
                        'imgs': imgs,
                        'user': user,
                    }
                    return render(request, 'self.html', imgs)
                except:
                    error = "没有头像哦!"
                    error = {
                        'error': error,
                        'user': user,
                    }
                    return render(request, 'self.html', error, {'user': user})
            else:
                x = request.session.get('user_id')
                tk = models.IMG.objects.get(img_id=x)
                if tk:
                    tk.img = request.FILES.get('img')
                    tk.name = request.FILES.get('img').name
                    print(request.session.get('user_id'), request.FILES.get('img'), request.FILES.get('img').name)
                    tk.save()
                else:
                    print(request.FILES.get('img').name)
                    new_img = models.IMG(
                        img_id=request.session.get('user_id'),
                        img=request.FILES.get('img'),
                        name=request.FILES.get('img').name
                    )
                    new_img.save()

                return redirect('/loginupin/self/')
        return redirect('/loginupin/')


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
        pwd3 = request.POST.get('pwd3')
        if pwd2 != pwd3:
            return render(request, 'changepwd.html', {'result': '确认两次新密码相同!'})
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
        email = request.POST.get('email')
        number = request.session.get('user_id')
        print(name, phone, email, number)
    else:
        return redirect('/loginupin/')
    if request.method == "GET":
        return render(request, "changebulk.html")
    else:
        try:
            obj = models.users.objects.get(user_id=number)
            obj.user_name = name
            obj.user_phone = phone
            obj.user_email = email
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
            x.comment_or = request.session.get('user_name')
            x.comment_time = datetime.now()
            print(x.comment_time)
            x.comments = content
            #x = models.comment(comment_id=comment_id,comment_or=comment_or,comment_time=comment_time,comments=comments)
            print(x)
        finally:
            x.save()
            print(1)
            return redirect('/loginupin/comment/')








