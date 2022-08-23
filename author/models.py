from django.db import models





class Author(models.Model):
    
    STATUS=[("AUTHOR","Author",),("STUDENT","Student"),("BOTH","Both")]
    name=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    status=models.CharField(choices=STATUS,default="STUDENT",max_length=255)
    create_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'author'
        managed = True
