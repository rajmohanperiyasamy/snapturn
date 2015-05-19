from django.db import models
from django.forms import ModelForm
from django.utils.translation import ugettext as _
from django.conf import settings


from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill, SmartResize



class ProfileImage(models.Model):
    imgtitle = models.CharField(max_length=100)
    imgdesc = models.CharField(max_length=100)
    image = models.FileField(upload_to='images/%Y/%m/%d')

    thumbnail = ImageSpecField(
        source='image', processors=[ResizeToFill(250, 250)], format='PNG',
        options={'quality':60})

    smart = ImageSpecField(
        source='image', processors=[SmartResize(250, 250)], format='PNG')


class Youtube(models.Model):
    url = models.CharField(max_length=200)
#
#class BackgroundImage(models.Model):
#    image = ProcessImageField(
#        upload_to='background/%Y/%m/%d', processors=[ResizeToFill(600, 600)],
#        format='PNG')