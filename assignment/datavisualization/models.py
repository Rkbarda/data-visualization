from django.db import models

# Create your models here.

class MyModel(models.Model):
    end_year = models.TextField(blank=True, null=True)
    intensity = models.IntegerField(blank=True, null=True)
    sector = models.TextField(blank=True, null=True)
    topic = models.TextField(blank=True, null=True)
    insight = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    region = models.TextField(blank=True, null=True)
    start_year = models.TextField(blank=True, null=True)
    impact = models.TextField(blank=True, null=True)
    added = models.TextField(blank=True, null=True)
    published = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    relevance = models.IntegerField(blank=True, null=True)
    pestle = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    likelihood = models.IntegerField(blank=True, null=True)
    print(MyModel.objects.all)
