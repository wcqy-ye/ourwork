from django.contrib import admin

# Register your models here.
import xadmin

from loginupin.admin import *

from .models import *

from xadmin import views
#
# class GlobalSetting(object):
#
#
# # 设置后台顶部标题
#
#     site_title ='我是后台管理'
#
#     # 设置后台底部标题
#
#     site_footer ='hhh'
#
#     #设置菜单可否折叠
#     # menu_style = "accordion"
# class BaseSetting(object):
#
# # 启用主题管理器
#
#     enable_themes =True
#  # 使用主题
#
#     use_bootswatch =True
#
# # 注册主题设置
#
# xadmin.site.register(views.BaseAdminView, BaseSetting)
# xadmin.site.register(views.CommAdminView, GlobalSetting)
# # xadmin.site.register(,GlobalSetting)
xadmin.site.register(team, GlobalSetting)
xadmin.site.register(teams_img, GlobalSetting)