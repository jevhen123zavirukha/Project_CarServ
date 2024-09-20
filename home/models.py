from django.db import models


class Establishment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Establishments'


# class CustomerReview(models.Model):
#     establishment = models.ForeignKey(Establishment, on_delete=models.CASCADE)
#     customer_name = models.CharField(max_length=100)
#     rating = models.PositiveSmallIntegerField()
#     comment = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f'{self.customer_name} - {self.rating}'
#
#     class Meta:
#         verbose_name_plural = 'Customer Reviews'
