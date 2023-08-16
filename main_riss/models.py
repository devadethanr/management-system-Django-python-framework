from django.db import models

# Create your models here.
class user_log(models.Model):
    user_name=models.CharField(max_length=255)
    user_pass=models.CharField(max_length=255)
    user_type=models.CharField(max_length=255)
    
class user_reg(models.Model):
    name=models.CharField(max_length=255)
    user_name=models.CharField(max_length=255)
    user_mail=models.CharField(max_length=255)
    user_pass=models.CharField(max_length=255)
    
class product(models.Model):
    p_name=models.CharField(max_length=255)
    p_cat=models.CharField(max_length=255)
    p_price=models.CharField(max_length=255)
    p_quant=models.CharField(max_length=255)
    
class user(models.Model):
    user_id=models.AutoField(primary_key=True)
    f_name=models.CharField(max_length=255)
    l_name=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    logins=models.ForeignKey(user_log,on_delete=models.CASCADE)