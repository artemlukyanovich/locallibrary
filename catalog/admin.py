from django.contrib import admin

from .models import Author, Genre, Book, BookInstance, Language

from django_admin_listfilter_dropdown.filters import \
    DropdownFilter, ChoiceDropdownFilter, RelatedDropdownFilter

# Register your models here.

# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)
admin.site.register(Language)


class BookInline(admin.TabularInline):
    model = Book
    extra = 0


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]


admin.site.register(Author, AuthorAdmin)


# class BookInstanceInline(admin.StackedInline):
class BookInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BookInstanceInline]
    # list_filter = ('genre', )


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'display_id')
    # list_filter = ('book__genre', 'book__author')
    list_filter = (('status', ChoiceDropdownFilter), ('borrower', RelatedDropdownFilter), 'due_back', 'book__author')
    search_fields = ['book__title', 'id']

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'borrower', 'due_back')
        }),
    )




