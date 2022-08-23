from django.db import models
from author.models import Author


class Collection(models.Model):
    name=models.CharField(max_length=255)
    create_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'collection'
        managed = True


class Course(models.Model):
    title=models.CharField(max_length=255)
    content=models.TextField()
    create_at=models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, related_name='author', on_delete=models.CASCADE)
    collection=models.ForeignKey(Collection,related_name="collection",on_delete=models.CASCADE)
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'course'
        managed = True
     


class Review(models.Model):
    author=models.ForeignKey(Author,related_name="author_review",on_delete=models.CASCADE)
    rating=models.DecimalField(max_digits=6,decimal_places=2)
    description=models.TextField()
    create_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.author

    class Meta:
        db_table = 'review'
        managed = True
