from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,'my_app/Home.html')

def login_page(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=authenticate(request,email=email,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.warning(request,"Username or Password is incorrect.")
    return render(request, 'my_app/login.html')

def logoutuser(request):
    logout(request)
    return redirect('home')

def payment(request):
    return render(request, 'my_app/payment.html')

def policy(request):
    return render(request,'my_app/policy.html')

def pricing(request):
    return render(request,'my_app/pricing.html')
@login_required(login_url='login')
def registration1(request):
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        fullname=fname+" "+lname
        age=request.POST['age']
        house_type=request.POST['house']
        gender=request.POST['gender']
        phone_number=request.POST['phone']
        email=request.POST['email']
        house_sitter_gender=request.POST['hs_age']
        register=Resgistration.objects.create(username=request.user,fullname=fullname,age=age,house_type=house_type,gender=gender,phone_number=phone_number,email=email,house_sitter_gender=house_sitter_gender)
        
        register.save()
        return redirect(register,permanent=True)
    
    return render(request,'my_app/registration 1.html')

@login_required(login_url='login')
def registration2(request,pk):
    if request.method=='POST':
            register=Resgistration.objects.get(id=pk)
            register.starting_date=request.POST['start']
            register.ending_date=request.POST['end']
            register.age_for_sitter=request.POST['age']
            register.country_visit=request.POST['country']
            register.staying_in_house=request.POST['shift']
            register.to_appoint=request.POST['to_appoint']
            register.address=request.POST['address']
            register.city=request.POST['city']
            register.state=request.POST['state']
            register.pincode=request.POST['pincode']
            register.instructions=request.POST['instructions']
            register.save()
            return redirect('home')
    
    return render(request,'my_app/registration 2.html')


def signin(request):
    form=CreateUserForm()
    if request.method=='POST': 
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Account Created! Kindly Login!")
    return render(request,'my_app/sign in.html',{'form':form})

@login_required(login_url='login')
def submitted_form(request):
    submitted=Resgistration.objects.all().filter(username=request.user)
    return render(request,'my_app/submitted_form.html',{'submitted':submitted})

    

def stafflogin(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=authenticate(request,email=email,password=password)
        if user is not None and user.is_staff==True:
            login(request,user)
            return redirect('home')
        else:
            messages.warning(request,"Username or Password is incorrect.")
    
    return render(request,'my_app/staff login.html')

@login_required(login_url='stafflogin')
def staff_page(request):
    if request.user.is_staff==True:
        return render(request,'my_app/staff_page.html')
    else:
        return redirect('stafflogin')
    
@login_required(login_url='stafflogin')
def takeing_care(request):
    if request.user.is_staff==True:
        submitted=Resgistration.objects.all().filter(sitter_allotment='Not Alloted').filter(to_appoint='house sitting')
        return render(request,'my_app/staff_appoint.html',{'submitted':submitted})
    else:
        return redirect('stafflogin')

@login_required(login_url='stafflogin')
def elder_care(request):
    if request.user.is_staff==True:
        submitted=Resgistration.objects.all().filter(sitter_allotment='Not Alloted').filter(to_appoint='elder care')
        return render(request,'my_app/staff_appoint.html',{'submitted':submitted})
    else:
        return redirect('stafflogin')
    
@login_required(login_url='stafflogin')
def pet_care(request):
    if request.user.is_staff==True:
        submitted=Resgistration.objects.all().filter(sitter_allotment='Not Alloted').filter(to_appoint='pet care')
        return render(request,'my_app/staff_appoint.html',{'submitted':submitted})
    else:
        return redirect('stafflogin')

@login_required(login_url='stafflogin')
def everythig(request):
    if request.user.is_staff==True:
        submitted=Resgistration.objects.all().filter(sitter_allotment='Not Alloted').filter(to_appoint='Everything')
        return render(request,'my_app/staff_appoint.html',{'submitted':submitted})
    else:
        return redirect('stafflogin')
