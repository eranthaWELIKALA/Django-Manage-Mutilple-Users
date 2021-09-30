from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    class Types(models.TextChoices):
        SPY = "SPY", "Spy"
        DRIVER = "DRIVER", "Driver"

    type = models.CharField(max_length=50, choices=Types.choices, default=Types.SPY)
    name = models.CharField(blank=True, max_length=255)

class SpyManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.SPY)

class Spy(User):
    objects = SpyManager()
    class Meta:
        proxy = True

    @property      
    def more(self)  :
        return self.spymore

    def whisper(self):
        print("ZZZZZ")

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.SPY
        return super().save(*args, **kwargs)

class SpyMore(models.Model):
    spy = models.OneToOneField(Spy, on_delete=models.CASCADE)
    weapon = models.CharField(max_length=255)
    rank = models.IntegerField()

    def __str__(self) -> str:
        return "{spy} - {rank}".format(spy=self.spy, rank=self.rank)

class DriverManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.DRIVER)

class Driver(User):
    objects = DriverManager()
    class Meta:
        proxy = True

    @property      
    def more(self)  :
        return self.drivermore

    def accelerate(self):
        print("Go faster")

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.DRIVER
        return super().save(*args, **kwargs)

class DriverMore(models.Model):
    driver = models.OneToOneField(Driver, on_delete=models.CASCADE)
    model = models.CharField(max_length=255)
    make = models.CharField(max_length=255)
    year = models.IntegerField()

    def __str__(self) -> str:
        return "{driver} - {make} {model}".format(driver=self.driver, make=self.make, model=self.model)