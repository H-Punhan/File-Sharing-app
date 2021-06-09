from django.db import models
from django.contrib.auth.models import User



class Files(models.Model):
    file=models.FileField(upload_to='static')
    name=models.CharField(max_length=25,blank=True)
    description=models.CharField(max_length=250,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_id',null=True)

class Comments(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='comment_user_id',null=True)
    file=models.ForeignKey(Files,on_delete=models.CASCADE,related_name='file_id',null=True)
    comment=models.TextField()


class Shared(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE,related_name='owner',null=True)
    shared=models.ForeignKey(User,on_delete=models.CASCADE,related_name='shared',null=True)
    file=models.ForeignKey(Files,on_delete=models.CASCADE,related_name='shared_file',null=True)