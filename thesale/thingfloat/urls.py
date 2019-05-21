from django.urls import path
from thingfloat import views as thingfloat_views


app_name = 'thingfloat' # 一定要写这一行，否则html中会报错 'account' is not a registered namespace

urlpatterns = [
    path('', thingfloat_views.things, name='things'),
    path('things/', thingfloat_views.things, name='things'),
    path('detail_thing/', thingfloat_views.things, name='things'),
    path('detail_thing/<int:num>/', thingfloat_views.detail_thing, name='detail_thing'),
    path('publish_thing/', thingfloat_views.publish_thing, name='publish_thing')
#path('articles/<int:num>/', theteam_views.articles, name='articles'),
]#+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  这句话是用来指定和映射静态文件的路径
