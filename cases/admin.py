from django.contrib import admin
from .models import Case, CaseTypes, CaseImage

# Register your models here.

admin.site.register(CaseTypes)
admin.site.register(Case)
admin.site.register(CaseImage)


