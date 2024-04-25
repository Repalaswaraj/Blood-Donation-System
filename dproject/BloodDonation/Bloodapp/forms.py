from pyexpat import model
from turtle import textinput
from django import forms
from django.forms import ModelForm
from .models import Donar,Patient,Patientss




class DonorForm(forms.ModelForm):
    class Meta:
        model=Donar
        fields='__all__'  
        
        widgets={
             'id':forms.TextInput(attrs={'class':'form-control'}),
             'Donar_name':forms.TextInput(attrs={'class':'form-control'}),
              'Donar_email':forms.TextInput(attrs={'class':'form-control'}),
               'Donar_age':forms.TextInput(attrs={'class':'form-control'}),
                'Donar_bloodGroup':forms.TextInput(attrs={'class':'form-control'}),
                'Donar_Unit':forms.TextInput(attrs={'class':'form-control'}),
                'Donar_dat':forms.TextInput(attrs={'class':'form-control'}),
               'Donar_disease':forms.TextInput(attrs={'class':'form-control'}),
               
             
        }
        
      
  
        
class PatientForm(forms.ModelForm):
    class Meta:
        model=Patient
        fields='__all__'  
        
        
        
        widgets={
            'id':forms.TextInput(attrs={'class':'form-control'}),
             'Patient_name':forms.TextInput(attrs={'class':'form-control'}),
              'Patient_email':forms.TextInput(attrs={'class':'form-control'}),
               'Patient_age':forms.TextInput(attrs={'class':'form-control'}),
                'Patient_bloodGroup':forms.TextInput(attrs={'class':'form-control'}),
                'Patient_Unit':forms.TextInput(attrs={'class':'form-control'}),
                'Patient_dat':forms.TextInput(attrs={'class':'form-control'}),
               'Patient_disease':forms.TextInput(attrs={'class':'form-control'}),
               
             
        }
              

class PatientssForm(forms.ModelForm):
    class Meta:
        model=Patientss
        fields='__all__'  
        
        
        
        widgets={
            'id':forms.TextInput(attrs={'class':'form-control'}),
             'Patientss_name':forms.TextInput(attrs={'class':'form-control'}),
              'Patientss_email':forms.TextInput(attrs={'class':'form-control'}),
               'Patientss_age':forms.TextInput(attrs={'class':'form-control'}),
                'Patientss_bloodGroup':forms.TextInput(attrs={'class':'form-control'}),
                'Patients_Unit':forms.TextInput(attrs={'class':'form-control'}),
                'Patientss_dat':forms.TextInput(attrs={'class':'form-control'}),
               'Patientss_disease':forms.TextInput(attrs={'class':'form-control'}),
               
             
        }
              

