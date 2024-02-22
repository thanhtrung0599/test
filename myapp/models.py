from django.db import models

# Create your models here.
class Tinh(models.Model):
    tinh = models.CharField(max_length = 255)
    def __str__(self):
        return self.tinh

class ThanhPho(models.Model):
    thanhpho = models.CharField(max_length = 255)
    tinh = models.ForeignKey(to = Tinh, on_delete = models.CASCADE)
    def __str__(self):
        return self.thanhpho

class QuanHuyen(models.Model):
    quanhuyen = models.CharField(max_length = 255)
    thanhpho = models.ForeignKey(to = ThanhPho, on_delete = models.CASCADE)
    def __str__(self):
        return self.quanhuyen