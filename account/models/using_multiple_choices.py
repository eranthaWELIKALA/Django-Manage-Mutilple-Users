from django.db import models, transaction
from django.contrib.auth.models import AbstractUser, UserManager as BaseUserManager

class UserTypes(models.TextChoices):
        SPY = "SPY", "Spy"
        DRIVER = "DRIVER", "Driver"

class UserManager(BaseUserManager):
    def get_queryset(self):
        return super().get_queryset().select_related()

class User(AbstractUser):
    type = models.CharField(max_length=50, choices=UserTypes.choices, default=UserTypes.SPY)
    def save(self, *args, **kwargs):
        if not self.pk:
            with transaction.atomic():
                save_result = super().save(*args, **kwargs)
                if self.type==UserTypes.SPY:
                    spy = Spy(user=self)
                    spy.save()
                else:
                    driver = Driver(user=self)
                    driver.save()
                return save_result
        else: 
            return super().save(*args, **kwargs)

class Spy(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    weapon = models.CharField(max_length=255, default="")
    rank = models.IntegerField(default=0)

    def __str__(self) -> str:
        return "{spy} - {rank}".format(spy=self.user, rank=self.rank)

class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    model = models.CharField(max_length=255, default="")
    make = models.CharField(max_length=255, default="")
    year = models.IntegerField(default=2021)

    def __str__(self) -> str:
        return "{driver} - {make} {model}".format(driver=self.user, make=self.make, model=self.model)