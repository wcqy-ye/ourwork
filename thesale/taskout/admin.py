from django.contrib import admin
from loginupin.admin import *

from .models import *
# Register your models here.
xadmin.site.register(tasks, GlobalSetting),
xadmin.site.register(tasks_img, GlobalSetting)