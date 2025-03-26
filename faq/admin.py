from django.contrib import admin
from .models import FAQ

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'approved', 'created_at')
    list_filter = ('approved',)
    search_fields = ('question', 'answer')
