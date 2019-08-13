from django.db import models
from django.contrib.auth.models import User
from os.path import join
from time import strftime

def get_file_path(instance, filename):
    return join(instance.user.username, strftime('%Y-%m-%d_%H:%M:%S')+'_'+filename)

# Create your models here.
class MyUploads(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file_path = models.FileField(upload_to=get_file_path, default='NULL')
