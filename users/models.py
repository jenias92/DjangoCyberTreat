from django.utils.timezone import localtime

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUsers(AbstractUser):
    def __init__(self, *args, **kwargs):
        super(CustomUsers, self).__init__(*args, **kwargs)
        self.original_password = self.password

    def save(self, *args, **kwargs):
        super(CustomUsers, self).save(*args, **kwargs)
        if self._password_has_been_changed():
            CustomUserPasswordHistory.remember_password(self)

    def _password_has_been_changed(self):
        return self.original_password != self.password


class CustomUserPasswordHistory(models.Model):
    username = models.ForeignKey(CustomUsers, on_delete=models.CASCADE)
    old_pass = models.CharField(max_length=128)
    pass_date = models.DateTimeField()

    @classmethod
    def remember_password(cls, user):
        cls(username=user, old_pass=user.password, pass_date=localtime()).save()
