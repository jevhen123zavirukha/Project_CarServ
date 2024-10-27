from django.db import models


class About(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    is_visible = models.BooleanField(default=True)
    experience_years = models.IntegerField(default=0)
    experience_text = models.CharField(max_length=50, default="Years Experience")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'


class AboutFeature(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name="features")
    order = models.PositiveIntegerField()
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.order}. {self.title}"