from django.db import models

# Create your models here.
class PageVisit(models.Model):
    # db -> table
    # id -> hidden primary key -> autofield -> 1, 2, 3, ...
    path = models.TextField(blank=True,null=True) #col
    timestamp = models.DateTimeField(auto_now_add=True) #col

# python manage.py makemigrations => "get ready to change the database"
# python manage.py migrate => "database table updated"