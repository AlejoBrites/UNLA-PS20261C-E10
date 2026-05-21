from django.contrib import admin
from .models import Category, Game


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'developer', 'is_available', 'created_at')
    list_filter = ('category', 'is_available')
    search_fields = ('title', 'developer')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('is_available',)
