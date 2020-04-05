from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Callee(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Call(models.Model):
    created_at = models.DateTimeField(default=datetime.now, blank=False)
    caller = models.ForeignKey(User, on_delete=models.CASCADE)
    callee = models.ForeignKey(Callee, on_delete=models.CASCADE)
    notes = models.TextField(blank=True)
