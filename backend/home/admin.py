from django.contrib import admin

# Register your models here.
from .models import Post
from .models import Author

class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'create_date', 'category', 'title', 'description','content')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'netid')

# Register your models here.

admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)