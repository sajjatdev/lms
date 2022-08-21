from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=255)
    
    def __str__(self):
        pass

    class Meta:
        db_table = 'author'
        managed = True
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'