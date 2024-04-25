from django.shortcuts import render

# Create your views here.



from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Donar,Patient,Patientss
from Bloodapp.forms import DonorForm,PatientForm,PatientssForm
# Create your views here.





@login_required(login_url='login')
def HomePage(request):
    ddata=Donar.objects.all()
    pdata=Patient.objects.all()  
        
       
    context={
         'ddata':ddata,
          'pdata':pdata
       
    }
    return render (request,'home.html',context)
 
 
 
@login_required(login_url='plogin') 
def donor(request):
     donar_form=DonorForm()
     
    
     if request.method=='POST':
        donar_form=DonorForm(request.POST)
        donar_form.save()
        donar_form=DonorForm()
        
     ddata=Donar.objects.all()
     pdata=Patient.objects.all()  
        
       
     context={
         'dform':donar_form,
         'ddata':ddata,
          'pdata':pdata
        
    }
     return render (request,'donar.html',context)
 
 

@login_required(login_url='plogin') 
def patient(request):
    patient_form=PatientForm()
    
    if request.method=='POST':
        patient_form=PatientForm(request.POST)
        patient_form.save()
        patient_form=PatientForm()
    ddata=Donar.objects.all()    
    pdata=Patient.objects.all()   
        
    context={
         'pform':patient_form,
         'pdata':pdata,
          'ddata':ddata
        
    }
    return render(request,'patient.html',context)




 
def patientss(request):
    patientss_form=PatientssForm()
    
    if request.method=='POST':
        patientss_form=PatientssForm(request.POST)
        patientss_form.save()
        patientss_form=PatientssForm()
        
    pdata=Patientss.objects.all()   
        
    context={
         'psform':patientss_form,
         'psdata':pdata
        
    }
    return render(request,'patientss.html',context)











def Main(request):
     return render(request,'Main.html')
 
 
def Benifits(request):
    return render(request,'Benifits.html')
     












    







def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    return render (request,'signup.html')






def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')




def pSignup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    return render (request,'psignup.html')




def pLogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'plogin.html')




def dSignup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    return render (request,'dsignup.html')




def dLogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'dlogin.html')