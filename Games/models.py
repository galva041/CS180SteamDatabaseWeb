from django.db import models

# Create your models here.
class Games (models.Model):
    title = models.CharField(("name"), max_length=255)
    dev = models.CharField(("developer"), max_length=150)
    rel_date = models.DateField(("release_date"), auto_now=True)
    publisher = models.CharField(("publisher"), max_length=150)
    categories = models.CharField(("categeories"), max_length=255)
    genre = models.CharField(("genres"), max_length=150)
    pos_rate = models.BigIntegerField(("positive_ratings"))
    neg_rate = models.BigIntegerField(("negative_ratings"))
    avg_playtime = models.BigIntegerField(("average_playtime"))
    median_playtime = models.BigIntegerField(("median_playtime"))
    price = models.FloatField(("price"))