from django.db import models

# Create your models here.
class WorkoutProgram(models.Model):
    program_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    program_picture = models.ImageField(upload_to='program_pictures/', blank=True, null=True)

    def __str__(self):
        return self.name