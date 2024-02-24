from django.db import models
from django.db.models.signals import post_delete


# todo
class User(models.Model):
    user_id = models.CharField(max_length=50)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)

    # todo remove save ovreriting, set blank=True option
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


class Section(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    section_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.section_name


class SectionItem(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=255)
    text_content = models.TextField(blank=True)
    photo_content = models.ImageField(upload_to=f'images/{section}/', blank=True)
    file_content = models.FileField(upload_to=f'files/{section}/', blank=True)

# todo add deletion cached files & images