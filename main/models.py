from django.db import models

# Create your models here.

class UserContact(models.Model):
    name = models.CharField(max_length=64, unique=True)
    email = models.EmailField(max_length=254,)
    comments = models.TextField(blank=True)


    class Meta:
        verbose_name_plural = 'Контакты пользователей'


    def __str__(self):
        return self.name