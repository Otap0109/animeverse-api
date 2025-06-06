from django.contrib import admin
from .models import Franchise

@admin.register(Franchise)
class FranchiseAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'rating', 'genre')
    search_fields = ('title', 'genre')
