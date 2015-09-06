# Register your models here.
from django.contrib import admin
from .models import Post, Question, Choice

admin.site.register(Post)
admin.site.register(Question)
admin.site.register(Choice)