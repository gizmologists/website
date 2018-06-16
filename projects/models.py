from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Person class in order to just have a list of people associated with a project
# This makes users unnecessary - simply access the admin site
class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    # An id, much like a user id, used as primary key for searches - used because no users needed
    # This is meant to be computing ID most likely
    id = models.CharField(max_length=50, primary_key=True, unique=True)
    # email will likely be based off of computing ID - but possible to change 
    email = models.EmailField(max_length=254)
    # Summary possible for each person - might as well?
    summary = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Project(models.Model):
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    title = models.CharField(max_length=50, unique=True)
    summary = RichTextUploadingField()
    slug = models.SlugField(max_length=50, unique=True)
    # A project has-a leader and a leader can lead many projects
    # Essentially just a way to identify some "face" to the project
    # This is NOT a hard set thing either - if you want a roster, can simply
    # use a ManyToMany field and use the roster_set 
    # Can have no leader as well
    leader = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, blank=True, 
            related_name='project')

    def __str__(self):
        return self.title
