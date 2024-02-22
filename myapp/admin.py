from django.contrib import admin

# Register your models here.
from .models import Tinh, ThanhPho, QuanHuyen
admin.site.register(Tinh)
admin.site.register(ThanhPho)
admin.site.register(QuanHuyen)