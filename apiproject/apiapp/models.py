from django.db import models

# Create your models here.
class UserData(models.Model):
    sUserID=models.CharField(max_length=36, primary_key=True)
    sLineID=models.CharField(max_length=33, blank=False, null=True)
    # sAccount=models.CharField(max_length=20, blank=False, null=True, unique=True)
    # sPassword=models.CharField(max_length=20, blank=False, null=True)
    sName=models.CharField(max_length=20, blank=False, null=True)
    sNickName = models.CharField(max_length=50, blank=False, null=True)
    sPhone=models.CharField(max_length=20, blank=False, null=True, unique=True)
    sPhoneAuth=models.BooleanField(default=False, null=False)
    sAddress=models.CharField(max_length=50, blank=False, null=True)
    sEmail=models.EmailField(max_length=50, blank=False, null=True)
    sPictureUrl=models.URLField(max_length=200, blank=False, null=True)

    class Meta:
        verbose_name = u"客戶個人資料"
        verbose_name_plural = verbose_name