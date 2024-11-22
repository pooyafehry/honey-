from django.contrib import admin
from .models import User
from django.contrib import admin
from .models import Category, Cart, CartItem





@admin.register(User)
class Useradmin(admin.ModelAdmin):
    list_display =['first_name','last_name','username','birthday']

# Register your models here.

from django.contrib import admin
from .models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'image')
    search_fields = ('name',)
    list_filter = ('name',)
