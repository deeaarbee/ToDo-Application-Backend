from django.contrib import admin

# Register your models here.

from . models import TodoBoard ,User

admin.site.register(TodoBoard)
admin.site.register(User)