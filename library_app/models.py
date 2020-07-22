from django.db import models


class Writer(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["pk"]


class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey('Writer', related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["pk"]
