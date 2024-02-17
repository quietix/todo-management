from django.db import models


# todo
class User(models.Model):
    user_id = models.CharField(max_length=50)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        if self.first_name is None:
            self.first_name = "None"
        if self.last_name is None:
            self.last_name = "None"
        if self.username is None:
            self.username = "None"
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.user_id} {self.first_name} {self.last_name} {self.username}'

