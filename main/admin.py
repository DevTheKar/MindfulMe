from django.contrib import admin
from .models import Note, ToDoList, Item
# Register your models here.

admin.site.register(Note)
admin.site.register(ToDoList)
admin.site.register(Item)
