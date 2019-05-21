from django.urls import path
from theteam import views as theteam_views


app_name = 'theteam' # 一定要写这一行，否则html中会报错 'account' is not a registered namespace

urlpatterns = [
    path('', theteam_views.listtemaer, name='listteamer'), # 列表页的url规则
    # path('1/', theteam_views.post_detail, name=''),# 详情页的url规则
    path('articles/', theteam_views.listtemaer, name='listteamer'),
    path('articles/<int:num>/', theteam_views.articles, name='articles'),
    path('publish/', theteam_views.publish, name='publish'),
]#+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  这句话是用来指定和映射静态文件的路径
