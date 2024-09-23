from django.contrib import admin
# Register your models here.
from first_app.models import Book, Publisher, Author # Post
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group
from .models.book import CustomUser


class CustomAdminPanel(BaseUserAdmin):
    fieldsets = (
        (_('Required Field'), {'fields': ('username', 'password')} ),
        (_('Personal Info'),  {'fields': ('first_name', 'last_name', 'email', 'birth_date', 'date_joined'), }),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')})

    )


    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'is_staff'),
        }),
    )

    list_display = ('username','email','first_name', 'last_name' , 'is_staff')
    search_fields = ('username','email', 'first_name', 'last_name')
    ordering = ('username',)



admin.site.register(CustomUser,CustomAdminPanel)


admin.site.unregister(Group)
admin.site.register(Group)








class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'registered')
    search_fields = ('title', 'author')
    list_filter= ('title', 'author',)
    ordering=('-author', 'title', )
    list_per_page = 2
    #fields = ('title','author', 'published_date', 'registered')





class BookInLine(admin.StackedInline):
    model = Book
    extra = 1


class PublisherAdmin(admin.ModelAdmin):
    inlines = [BookInLine]
    list_display = ('name', 'register_date')


admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Author)
#admin.site.register(Post)
