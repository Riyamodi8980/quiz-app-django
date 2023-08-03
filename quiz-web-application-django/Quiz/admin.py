from django.contrib import admin
from .models import *

# Register your models here.
class QuiQuesModelAdmin(admin.ModelAdmin):
    list_display=['question','category']
admin.site.register(QuesModel)

admin.site.register(QuizCategory)