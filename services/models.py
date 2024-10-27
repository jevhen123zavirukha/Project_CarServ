from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=150)
    is_visible = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Services'
