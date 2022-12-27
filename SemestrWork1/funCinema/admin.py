
from django.contrib import admin
from .models import Category, Genre, Serials, Actor, Cadrs

admin.site.register(Cadrs)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Serials)
admin.site.register(Actor)

