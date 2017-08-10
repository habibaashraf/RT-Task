from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

class User(models.Model):
    Name=models.CharField(max_length=250)
    Email = models.CharField(max_length=500)
    Phone = models.IntegerField()
    Age = models.IntegerField(blank=True, null=True)
    Gender = models.CharField(max_length=250, blank=True, null=True)
    Comment= models.CharField(max_length=1000, blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def get_absolute_url(self):
        return reverse('newApp:saved',args=[str(self.id)])
    def __str__(self):
        return self.Name