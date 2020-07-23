from django.contrib import admin
from .models import Show, Episode, Tag, Banner

# Register your models here.
admin.site.register(Show)
admin.site.register(Episode)
admin.site.register(Tag)
admin.site.register(Banner)