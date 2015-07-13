from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
  user = models.ForeignKey(User)
  title = models.CharField(max_length=10)
  content =  models.CharField(max_length=10)
  def __unicode__(self):
    return self.title


		