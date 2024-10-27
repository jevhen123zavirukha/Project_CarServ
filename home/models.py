from django.db import models


class Establishment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    years_experience = models.CharField(max_length=255)
    expert_technicians = models.CharField(max_length=255)
    satisfies_clients = models.CharField(max_length=255)
    compleate_projects = models.CharField(max_length=255)

    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Establishments'
