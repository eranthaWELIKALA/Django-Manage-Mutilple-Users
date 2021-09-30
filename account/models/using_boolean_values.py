from django.db import models, transaction
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_spy = models.BooleanField(default=True)
    is_driver = models.BooleanField(default=False)

    # This both boolean values can not be True
    def save(self, *args, **kwargs):
        if self.is_spy and self.is_driver:
            self.is_driver = False
        elif (not self.is_spy) and (not self.is_driver):
            self.is_spy = True
        if not self.pk:
            with transaction.atomic():
                save_result = super().save(*args, **kwargs)
                if self.is_spy:
                    spy = Spy(user=self)
                    spy.save()
                elif (not self.is_spy) and (not self.is_driver):
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