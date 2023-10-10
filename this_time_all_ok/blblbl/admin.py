from django.contrib import admin
from .models import Comment, Post, Images


class CommentInline(admin.TabularInline):
    model = Comment
    readonly_fields = ('post', 'profile')


class ImageInline(admin.StackedInline):
    model = Images
    readonly_fields = ('post',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'description'),
        }),
        ('Даты', {
            'fields': ('created_at', 'updated_at'),
        }),

        ('Дополнительная информация', {
            'fields': ('slug',),
        }),
    )
    list_display = ('title', 'created_at', 'updated_at')
    ordering = ('updated_at', 'title', 'created_at')
    readonly_fields = ('created_at', 'updated_at', 'slug')
    inlines = (CommentInline, ImageInline)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('profile', 'post', 'text')
    readonly_fields = ('profile', 'post')
    fieldsets = (('Профиль', {'fields': ('profile', )}), ('Пост и текст', {'fields':('post', 'text')}))


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'post')
    ordering = ('id', 'post')
    readonly_fields = ('post', )

# Register your models here.
