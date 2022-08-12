from ast import mod
from django.contrib import auth
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
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    contributors = models.ManyToManyField('Contributor', through="BookContributor")
    
    def __str__(self) -> str:
        return self.title
    
class Contributor(models.Model):
    """Book Contributors: Author(s), Editor, etc."""
    first_names = models.CharField(max_length=50, help_text="Contributor's first names")
    last_names = models.CharField(max_length=50, help_text="Contributor's last names")
    email = models.EmailField(help_text="Contributor's Email address")
    
    def __str__(self) -> str:
        return self.first_names
    
class BookContributor(models.Model):
    class ContributionRole(models.TextChoices):
        AUTHOR = "AUTHOR", "Author"
        CO_AUTHOR = "CO_AUTHOR", "Co-Author"
        EDITOR = "EDITOR", "Editor"
    
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    role = models.CharField(verbose_name="The role this contributor had in the book.",choices=ContributionRole.choices, max_length=20)
    
class Review(models.Model):
    content = models.TextField(help_text="The Review text.")
    rating = models.IntegerField(help_text="The rating the reviewer has given.")
    date_created = models.DateTimeField(auto_now_add=True, help_text="date and time the review was created.")
    date_edited = models.DateTimeField(null=True, help_text="The date and time the review was last edited.")
    creator = models.ForeignKey(auth.get_user_model(),on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, help_text="The book review was for.")