from django.contrib import admin
from .models import List, Item


admin.site.register(List)  # registra o models no admin
admin.site.register(Item) 