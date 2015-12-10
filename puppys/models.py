from django.db import models
from django import forms


class ImageUploadForm(forms.Form):
    image = forms.ImageField()


class ToyPoodle(models.Model):
    Name = models.CharField(max_length=70)
    Description = models.TextField()
    Pic = models.ImageField(upload_to='../media/pic_folder/', default='')

    def __str__(self):
        return self.Name


class ShihTzu(models.Model):
    Name = models.CharField(max_length=70)
    Description = models.TextField()
    Pic = models.ImageField(upload_to='..media/pic_folder/', default='')

    def __str__(self):
        return self.Name
