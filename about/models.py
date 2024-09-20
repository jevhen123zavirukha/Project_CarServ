from django.db import models


class About(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'
