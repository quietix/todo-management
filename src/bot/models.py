from django.db import models


# todo
class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
