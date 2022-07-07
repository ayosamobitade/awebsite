from django.contrib import admin

# Register your models here.
from .models import Quote

admin.site.register(Quote)


class QuoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'company', 'submitted', 'quotedate', 'quoteprice')
    list_filter = ('submitted', 'quotedate')
    readonly_fields = ('submitted',)
    fieldsets = (
        (None, {
            'fields': ('name', 'email', 'descriprion')
        }),
        ('Contact Information', {
            'classes': ('postion', 'company', 'address', 'phone', 'web')

        }),
        ('Job Information', {
            'classes':('collapse',),
            'fields':('sitestatus', 'priority', 'submitted')

        }),
        ('Quote Admin',{
            'classes':('collapse',),
            'fields':('quotedate', 'quoteprice', 'username')
        }),
    )