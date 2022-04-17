from django.db import models

# Create your models here.
class Games (models.Model):
    title = models.CharField(("name"), max_length=255)
    rel_date = models.DateField(("release_date"), auto_now=True)
    english = models.CharField(("in english", ), max_length=1)
    dev = models.CharField(("developer"), max_length=150)
    publisher = models.CharField(("publisher"), max_length=150)
    platform = models.CharField(("platforms"), max_length=150)
    rec_age = models.CharField(("required Age"), max_length=155)
    categories = models.CharField(("categeories"), max_length=255)
    genre = models.CharField(("genres"), max_length=150)
    steamspy_tags = models.CharField(("steamspy tags"), max_length=250)
    achievements = models.BigIntegerField(("number of Achievements"))
    pos_rate = models.BigIntegerField(("positive_ratings"))
    neg_rate = models.BigIntegerField(("negative_ratings"))
    avg_playtime = models.BigIntegerField(("average_playtime"))
    median_playtime = models.BigIntegerField(("median_playtime"))
    owners = models.BigIntegerField(("number of owners"))
    price = models.FloatField(("price"))