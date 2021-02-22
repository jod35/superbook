from django.contrib import admin
from .models import Post,Profile


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=["title","created","updated"]
    list_filter=["created"]

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=["bio","profile_pic"]
    list_filter=["bio"]
    
