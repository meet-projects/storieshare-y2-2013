from django.db import models

# Create your models here.
#class account (models.Model)
#   username = models.CharField(max_length = 15)
#    password = models.CharField(max_length = 15)
#
#    def _unicode_(self):
#        return username

class story (models.Model):
    storyHeadline = models.CharField(max_length = 25) 
    storyDescription = models.CharField(max_length = 100)
  
    
class Paragraph (models.Model):
    pargraphContent = models.CharField(max_length = 500)
    story = models.ForeignKey("story")

#class Comments (models.Model):
    #Comment = models.ForeignKey("story")




