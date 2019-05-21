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
        x = models.team()
        first = request.POST.get("first", None)
        telephone = request.POST.get("telephone", None)
        email = request.POST.get("email", None)
        competition = request.POST.get("competition", None)
        teamer = request.POST.get("teamer", None)
        category = request.POST.get("category", None)
        description = request.POST.get("description", None)
        #print(first,telephone,email,competition,teamer,category)
        x.first = first
        x.category = category
        x.telephone = telephone
        x.competition = competition
        x.email = email,
        x.teamer = teamer
        x.description = description
        x.save()
        print(first, telephone, email, competition, teamer, description)
        if  category == '' or first == '' or telephone == '' or competition == ''or teamer == '' or description == '':
            return render(request, 'publish.html', {
               'error': "不能有要求的字段为空!"
             })
        else:
            new_img = models.teams_img()
            new_img.img_id = x.id
            new_img.img = request.FILES.get('img')
            new_img.name = request.FILES.get('img').name
            print(request.FILES.get('img'))
            new_img.save()
            return redirect('/theteam/')


def articles(request, num):
    if request.method == "GET":
        tk = request.session.get('user_name')
        if tk:
            imgs = models.teams_img.objects.get(img_id=num)
            article = models.team.objects.filter(id=num)[0]
            return render(request, 'articles.html', {
            'article': article,
            'imgs' : imgs
            })
        else:
            return redirect('/loginin/')
    else:
        return redirect('/loginin/')


