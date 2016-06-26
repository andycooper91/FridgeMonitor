from django.db import models

# Create your models here.


class Kind(models.Model):
    kindCode = models.CharField(max_length=200)
    kindDescription = models.CharField(max_length=200)
    
    def __str__(self):
        return self.kindCode
    
class User(models.Model):
    userFirstName = models.CharField(max_length=200)
    userLastName = models.CharField(max_length=200)
    userMiddleName = models.CharField(max_length=200)
    
    def __str__(self):
        return self.userFirstName+ " "+self.userMiddleName+" "+self.userLastName
    
    
class Event(models.Model):
    user = models.ForeignKey(User)
    kind = models.ForeignKey(Kind)
    event_date = models.DateTimeField('date published')
    
    