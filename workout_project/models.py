from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    sessions_quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.username
