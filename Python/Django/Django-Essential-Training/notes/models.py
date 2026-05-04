from django.db import models

class Notes(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    # Challenge - Class 03 (read notes for detail):
    
    # My solution:
    # likes = models.IntegerField(null=True)

    # Instructor's Solution: PositiveSmallIntegerField
    likes = models.PositiveSmallIntegerField(default=0)

    
    