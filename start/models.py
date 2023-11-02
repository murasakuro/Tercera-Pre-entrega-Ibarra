from django.db import models

class Die(models.Model):
    # dice_set=models.BooleanField()
    style=models.CharField(max_length=60)
    faces=models.IntegerField()
    numbering=models.CharField(max_length=40)
    def __str__(self):
        return f'{self.id} - {self.style} - {self.faces} - {self.numbering}'

class DiceBag(models.Model):
    material=models.CharField(max_length=40)
    color=models.CharField(max_length=40)
    capacity=models.IntegerField()
    def __str__(self):
        return f'{self.id} - {self.material} - {self.color} - {self.capacity}'

class Tray(models.Model):
    material=models.CharField(max_length=40)
    color=models.CharField(max_length=40)
    size=models.IntegerField()
    def __str__(self):
        return f'{self.id} - {self.material} - {self.color} - {self.size}'