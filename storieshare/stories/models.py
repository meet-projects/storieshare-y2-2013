from django.db import models

# Create your models here.
#class account (models.Model)
#   username = models.CharField(max_length = 15)
#    password = models.CharField(max_length = 15)
#
#    def _unicode_(self):
#        return username

class story (models.Model)
    storyTitle = models.CharField(max_length = 25) 
    storyLikes = models.IntegerField()
    storyComments = models.CharField(max_length = 250)
    
class Paragraph (models.Model)
    pargraphContent = models.CharField()
    Story = models.ForeignKey("story")

class Comments (models.Model)
    Comment = models.ForeignKey("story")




