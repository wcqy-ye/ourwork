from django.contrib import admin
from loginupin.admin import *

from .models import *
# Register your models here.
xadmin.site.register(task, GlobalSetting),