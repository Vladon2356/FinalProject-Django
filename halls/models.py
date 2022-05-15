from django.db import models
from django.urls import reverse


class Halls(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=60)
    rows = models.SmallIntegerField()
    columns = models.SmallIntegerField()

    def get_absolute_url(self):
        return reverse("hall_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Hall"
        verbose_name_plural = "Halls"
