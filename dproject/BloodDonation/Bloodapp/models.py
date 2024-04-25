from django.db import models

# Create your models here.

class Donar(models.Model):
    
   Donar_name=models.CharField(max_length=50,null=True)
   Donar_email=models.EmailField(max_length=50,null=True)
   Donar_age=models.IntegerField(null=True) 
   Donar_bloodGroup=models.CharField(max_length=10,null=True)
   Donar_Unit=models.IntegerField(null=True) 
   Donar_dat=models.IntegerField(null=True) 
   Donar_disease=models.CharField(max_length=50,null=True)
   
   
   
   
class Patient(models.Model):
    
   Patient_name=models.CharField(max_length=50,null=True)
   Patient_email=models.EmailField(max_length=50,null=True)
   Patient_age=models.IntegerField(null=True) 
   Patient_bloodGroup=models.CharField(max_length=10,null=True)
   Patient_Unit=models.IntegerField(null=True) 
   Patient_dat=models.IntegerField(null=True) 
   Patient_disease=models.CharField(max_length=50,null=True)
   
   
   
   
class Patientss(models.Model):
    
   Patientss_name=models.CharField(max_length=50,null=True)
   Patientss_email=models.EmailField(max_length=50,null=True)
   Patientss_age=models.IntegerField(null=True) 
   Patientss_bloodGroup=models.CharField(max_length=10,null=True)
   Patientss_Unit=models.IntegerField(null=True) 
   Patientss_dat=models.IntegerField(null=True) 
   Patientss_disease=models.CharField(max_length=50,null=True)