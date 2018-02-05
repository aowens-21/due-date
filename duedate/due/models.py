from django.db import models


class Assignment(models.Model):
    name = models.CharField(max_length=200)
    due_date = models.DateTimeField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.name
