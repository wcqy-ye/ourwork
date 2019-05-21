from django.contrib import admin
from loginupin.admin import *

from .models import *
# Register your models here.
xadmin.site.register(things, GlobalSetting)
xadmin.site.register(things_img, GlobalSetting)