from django.contrib import admin
from .models import Profile
from blblbl.models import Post, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    readonly_fields = ('post', )



class PostInline(admin.StackedInline):
    model = Post
    readonly_fields = ('slug', )
    can_delete = False

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    inlines =  (PostInline, CommentInline)
    list_display = ('user', 'first_name', 'second_name', 'date_of_birth')
    fieldsets = (('Никнэйм', {'fields': ('user', )}),
                 ('Информация профиля', {'fields': ('first_name', 'second_name', 'date_of_birth')}))
    ordering = ('user', 'date_of_birth')
    readonly_fields = ('user', )



# Register your models here.
