from django.contrib import admin
from django.http import HttpResponse
from .models import Person, Project, Post


class PersonAdmin(admin.ModelAdmin):

    def mark_as_added_to_email(self, request, queryset):
        rows_updated = queryset.update(need_added_to_email=False)
        if rows_updated == 1:
            message_bit = "1 person was"
        else:
            message_bit = "%s people were" % rows_updated

        self.message_user(request, "%s successfully marked added to email list." % message_bit)

    def get_need_to_be_added(self, request, queryset):
        people = Person.objects.filter(need_added_to_email=True)
        people_string = '\n'.join(person.id for person in people)
        return HttpResponse(people_string, content_type='text/plain')
            
    def get_need_to_be_removed(self, request, queryset):
        people = Person.objects.filter(need_removed_from_email=True)
        people_string = '\n'.join(person.id for person in people)
        return HttpResponse(people_string, content_type='text/plain')

    mark_as_added_to_email.short_description = "Mark selected people as added to email list"
    get_need_to_be_added.short_description = "Get list of people who need to be added"
    # Currently don't support removing - do through email
    #get_need_to_be_removed.short_description = "Get list of people who need to be removed"

    actions = [mark_as_added_to_email, get_need_to_be_added]

    search_fields = ('first_name', 'last_name', 'id')

    list_filter = ('need_added_to_email', 'need_removed_from_email')

class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Person, PersonAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Post, PostAdmin)
