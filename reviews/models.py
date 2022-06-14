from django.db import models

# Create your models here.
class Publisher (models.Model):
    """A Company that publishes books."""
    name = models.CharField(max_length=50, help_text="Name of the Publisher.")
    website = models.URLField(help_text="Publisher's Website.")
    email = models.EmailField(help_text="Publisher's Email address")
    
class Book(models.Model):
    """Published book or Article"""
    title = models.CharField(max_length=70, help_text="The Title of Book or Article")
    publication_date = models.DateField(verbose_name="Date book was published")
    isbn = models.CharField(max_length=20, verbose_name="Books ISBN")
    
class Contributor(models.Model):
    """Book Contributors: Author(s), Editor, etc."""
    first_names = models.CharField(max_length=50, help_text="Contributor's first names")
    last_names = models.CharField(max_length=50, help_text="Contributor's last names")
    email = models.EmailField(help_text="Contributor's Email address")