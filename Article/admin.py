from django.contrib import admin
from .models import Point,Rating,Article
# Register your models here.

class Admin(admin.ModelAdmin):
   class Meta:
      model = Article
admin.site.register(Article,Admin)
admin.site.register(Point,Admin)
admin.site.register(Rating,Admin)
