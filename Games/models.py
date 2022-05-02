from django.db import models

# Create your models here.
class Games (models.Model):
    title = models.CharField(("name"), max_length=255)
    rel_date = models.DateField(("release_date"), auto_now=True, null=True)
    english = models.CharField(("in english", ), max_length=1, null=True)
    dev = models.CharField(("developer"), max_length=150)
    publisher = models.CharField(("publisher"), max_length=150)
    platform = models.CharField(("platforms"), max_length=150, null=True)
    rec_age = models.CharField(("required Age"), max_length=155, null=True)
    categories = models.CharField(("categeories"), max_length=255, null=True)
    genre = models.CharField(("genres"), max_length=150)
    steamspy_tags = models.CharField(("steamspy tags"), max_length=250, null=True)
    achievements = models.BigIntegerField(("number of Achievements"),null=True)
    pos_rate = models.BigIntegerField(("positive_ratings"), null=True)
    neg_rate = models.BigIntegerField(("negative_ratings"), null=True)
    avg_playtime = models.BigIntegerField(("average_playtime"), null=True)
    median_playtime = models.BigIntegerField(("median_playtime"),null=True)
    owners = models.CharField(("number of owners"), max_length=100, null=True)
    price = models.FloatField(("price"))

    def __str__(self):
        return self.title

    def get_dev(self):
        return self.dev

    def get_genre(self):
        return self.genre

    def get_pub(self):
        return self.publisher

    def get_price(self):
        return self.price
