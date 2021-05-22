from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from iu_api.models import TrackedUserObject
from django.db.models.signals import post_save
from datetime import datetime


# Аккаунт. Кастомное расширение модели пользователя
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tracked_users = models.ManyToManyField(TrackedUserObject)
    is_premium = models.BooleanField(default=False)
    last_time_login = models.DateTimeField(default=datetime.now)

    # Проверка, заходил ли пользователь в последние 30 суток
    def is_active(self):
        now = datetime.now()
        last_online = self.last_time_login
        t = (now - last_online).total_seconds()
        return t < 2592000


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        account = Account.objects.create(user=instance)
        account.save()
