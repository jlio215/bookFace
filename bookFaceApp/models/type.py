from django.db import models
from.user import User

class Type(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_role = models.CharField('User_role', max_length = 30)
    right = models.CharField('Right', max_length = 30)
    logs = models.DateTimeField()
    