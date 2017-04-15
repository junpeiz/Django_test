from django.db import models
from django.utils import timezone

# models.Model means that the Post is a Django Model, so Django knows that it should be saved in the database.
# This Post class is a child class of models.Model
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200) # for text with a limited number of characters
    text = models.TextField() # for long text without a limit
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        # When call str(PostX), just return the post's title
        return self.title
