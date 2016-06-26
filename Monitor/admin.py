from django.contrib import admin

# Register your models here.
from .models import Event,User,Kind

admin.site.register(Event)
admin.site.register(User)
admin.site.register(Kind)