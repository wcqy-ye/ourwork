from django.shortcuts import render
from django.shortcuts import HttpResponse, render, redirect
from theteam import models
# Create your views here.

def listtemaer(request):
    if request.method == "GET":
        tk = request.session.get('user_name')
        if tk:
            listteam = models.team.objects.all()
            return render(request, 'list.html', {
            'listteam': listteam
            })
        else:
            return redirect('/loginin/')
    else:
        return redirect('/loginin/')

def publish(request):
    if request.method == "GET":
        tk = request.session.get('user_name')
        if tk:
            return render(request, "publish.html")
        else:
            return redirect('/loginin/')
    if request.method == "POST":
        first = request.POST.get("first", None)
        telephone = request.POST.get("telephone", None)
        email = request.POST.get("email", None)
        competition = request.POST.get("competition", None)
        teamer = request.POST.get("teamer", None)
        description = request.POST.get("description", None)
        print(first, telephone, email, competition, teamer, description)
        models.team.objects.create(first=first, telephone=telephone, email=email, competition=competition, teamer=teamer, description=description)
        if first == '' or telephone == '' or competition == ''or teamer == '' or description == '':
            return render(request, 'publish.html', {
               'error': "不能有要求的字段为空!"
             })
        else:
            return redirect('/theteam/')


def articles(request, num):
    if request.method == "GET":
        tk = request.session.get('user_name')
        if tk:
            article = models.team.objects.filter(id=num)[0]
            return render(request, 'articles.html', {
            'article': article
            })
        else:
            return redirect('/loginin/')
    else:
        return redirect('/loginin/')


