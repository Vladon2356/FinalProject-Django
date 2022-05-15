from django.db import models
from django.urls import reverse


class Movies(models.Model):
    AGE_RATE_CHOICES = (
        ("G", "G"),
        ("PG", "PG"),
        ("PG-13", "PG-13"),
        ("R", "R"),
        ("NC-17", "NC-17"),
    )
    title = models.CharField(max_length=100, unique=True)
    poster = models.ImageField(upload_to="posters/")
    slug = models.SlugField(max_length=110)
    description = models.TextField()
    year = models.SmallIntegerField(default=2022, null=False)
    duration = models.SmallIntegerField(null=False)
    genres = models.ManyToManyField("Genres", related_name="movies")
    actors = models.ManyToManyField("Actors", related_name="movies")
    producer = models.ManyToManyField("Producer", related_name="movies")
    age_rating = models.CharField(max_length=5, null=False, choices=AGE_RATE_CHOICES)
    in_rental = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"


class Genres(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=110)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"


class Producer(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=110)

    def get_absolute_url(self):
        return reverse("producer_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Producer"
        verbose_name_plural = "Producers"


class Actors(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=110)

    def get_absolute_url(self):
        return reverse("actor_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Actor"
        verbose_name_plural = "Actors"
