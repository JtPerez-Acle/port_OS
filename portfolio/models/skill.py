from django import models

class Skill(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    years_of_expertise = models.IntegerField()

    def __str__(self):
        return self.name