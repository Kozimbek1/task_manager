from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')
    is_deleted = models.BooleanField('Удалено', default=False)

    def __str__(self):
        return self.title

