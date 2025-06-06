from django.contrib import admin
from .models import Character

@admin.register(Character)
class CharactersAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'franchise', 'age')
    search_fields = ('name', 'role')