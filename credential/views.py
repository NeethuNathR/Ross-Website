from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages, auth

# Create your views here.


from credential.models import StaffRegistration,staffLogin,Contact



def senior(request):
    return render(request,'senior.html')
def abouts(request):
   return render(request,'abouts.html')
def services(request):
   return render(request,'services.html')
def contacts(request):
   return render(request,'contacts.html')

def staff(request):
    return  render(request,'staff.html')
def aboutss(request):
    return  render(request,'aboutss.html')
def servicess(request):
    return  render(request,'servicess.html')
def contactss(request):
    return  render(request,'contactss.html')


def staff_registration(request):

    if request.method=='POST':
        userid= request.POST['userid']

        username=request.POST['username']
        designation=request.POST['designation']
        email=request.POST['email']
        address=request.POST['address']
        contact=request.POST['contact']
        pincode=request.POST['pincode']
        district=request.POST['district']
        state=request.POST['state']
        password=request.POST['password1']
        cpassword=request.POST['password2']

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exist")
                return redirect("staff_registration")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"this email id already exist")
                return redirect("staff_registration")
            else:



                user = User.objects.create_user(username=username, email=email, password=password)

                user.save()
                staffregister = StaffRegistration.objects.create(userid=userid, designation=designation,
                                                                 address=address, pincode=pincode, contact=contact,
                                                                 district=district, state=state)
                staffregister.save()

        else:
            messages.info(request,"password not matching")
            return redirect("staff_registration")
        return redirect("senior")


    return render(request,'staff_registration.html')


def staff_login(request):
    if request.method=='POST':
        userid=request.POST['userid']
        username=request.POST["username"]
        password=request.POST["password"]
        user=auth.authenticate(username=username,password=password)

        try:
            stafflogin = StaffRegistration.objects.get(userid=userid)
            stafflogin.save()
        except ObjectDoesNotExist:
            messages.info(request, "User id  not found.")
            return redirect("staff_login")


        if user is not None:


            auth.login(request,user)

            return redirect("staff")
        else:
            messages.info(request,"invalid Username or Password")

            return redirect("staff_login")

    return render(request,"staff_login.html")

def logout(request):
    auth.logout(request,)
    return redirect("/")

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, update_session_auth_hash

def change_password(request):
    if request.method == 'POST':
        username = request.POST['username']
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']

        user = authenticate(username=username, password=old_password)

        if user is not None:
            user.set_password(new_password)
            user.save()
            update_session_auth_hash(request, user)
            return HttpResponse('Password changed successfully.')

        else:
            return HttpResponse('Invalid username or password.')
    else:
        return render(request, 'change password.html')

def queries(request):
    if request.method == 'POST':
        FullName = request.POST['FullName']
        Email = request.POST['Email']
        Subject = request.POST['Subject']
        Message=request.POST['Message']

        contact = Contact(FullName=FullName, Email=Email, Subject=Subject, Message=Message)
        contact.save()

        return render(request, 'contact.html')



