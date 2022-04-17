# Generated by Django 4.0.3 on 2022-04-17 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='name')),
                ('rel_date', models.DateField(auto_now=True, verbose_name='release_date')),
                ('english', models.CharField(max_length=1, verbose_name=('in english',))),
                ('dev', models.CharField(max_length=150, verbose_name='developer')),
                ('publisher', models.CharField(max_length=150, verbose_name='publisher')),
                ('platform', models.CharField(max_length=150, verbose_name='platforms')),
                ('rec_age', models.CharField(max_length=155, verbose_name='required Age')),
                ('categories', models.CharField(max_length=255, verbose_name='categeories')),
                ('genre', models.CharField(max_length=150, verbose_name='genres')),
                ('steamspy_tags', models.CharField(max_length=250, verbose_name='steamspy tags')),
                ('achievements', models.BigIntegerField(verbose_name='number of Achievements')),
                ('pos_rate', models.BigIntegerField(verbose_name='positive_ratings')),
                ('neg_rate', models.BigIntegerField(verbose_name='negative_ratings')),
                ('avg_playtime', models.BigIntegerField(verbose_name='average_playtime')),
                ('median_playtime', models.BigIntegerField(verbose_name='median_playtime')),
                ('owners', models.BigIntegerField(verbose_name='number of owners')),
                ('price', models.FloatField(verbose_name='price')),
            ],
        ),
    ]
