from django.contrib import admin
from .models import BlogPost

# Register your models here.

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "published", "created_on", "last_update",)
    list_editable = ("published",)

admin.site.register(BlogPost,BlogPostAdmin)