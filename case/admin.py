from django.contrib import admin
from .models import Case

# Register your models here.

class CaseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('case_name',)}
    list_display = ('case_name', 'esas', 'mahkeme', 'status')

admin.site.register(Case, CaseAdmin)
