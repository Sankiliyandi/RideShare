from django.core.serializers import serialize
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from .form import*
from .models import user,offerARide
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sessions.models import Session
from .otpHandler import otp
import random

# Create your views here.
@csrf_exempt
def home(request):
     try:
       login=request.session['login']
       emailId=request.session['email']
       userLog=user.objects.get(email_id=emailId)
       username=userLog.uname
       return render(request,'home.html',{'login':login ,'username':username})
     except:
       login=False
       return render(request,'home.html',{'login':login})
def logout(request):
   request.session.modified = True
   del request.session['email'] 
   del request.session['password']
   del request.session['username']
  # del request.session['phoneNo']
   del request.session['login']
  # del request.session['otpcode']
   return HttpResponseRedirect("/")
def register(request):
    if(request.method == "GET"):
     print("naaaa")
     return render(request,'registerform.html')
    else:
        passWord=request.POST.get('password')
        username=request.POST.get('user name')
        emailId=request.POST.get('email')
        phoneNo=request.POST.get('phoneNo')
        print(username)
        print(passWord)
        print(request.POST)
        if user.objects.filter(email_id=emailId):
    
          messages.error(request,'email already used try to login')
          return render(request,'registerform.html')
       
        else:
        
         request.session['email'] = emailId
         request.session['password']=passWord
         request.session['username']=username
         request.session['phoneNo']=phoneNo
         request.session['login']=True
         userLog=user.objects.get(email_id=emailId)
         request.session['username']=userLog.uname
         phone="+91"+phoneNo 
         rcode=random.randint(1000,9999)
         code=str(rcode)
         request.session['otpcode']=code
         print(phone) 
         otp(phone,code)
         return HttpResponseRedirect("otp")
      
def loginform(request):
    if(request.method=="GET"):
     print("naaaa")
     return render(request,'loginform.html')
    else:
        passWord=request.POST.get('password')
        emailId=request.POST.get('email')
    if user.objects.filter(email_id=emailId):
        userLog=user.objects.filter(email_id=emailId).values()
        print(userLog)
        if user.objects.filter(email_id=emailId, password=passWord):
         userLog=user.objects.get(email_id=emailId)
         print(userLog.uname)
         request.session['login']=True
         request.session['email'] = emailId
         request.session['password']=passWord
         request.session['username']=userLog.uname
        
         return HttpResponseRedirect("/")
        else:
           messages.error(request,'incorrect password')
           return render(request,'loginform.html') 
    else:
       messages.error(request,'email not registered try to signup')
       return render(request,'loginform.html') 


 

def offerpost(request):
  if(request.method=="POST"):
   try: 
    LFrom=request.POST.get('from').lower()
    Gto=request.POST.get('to').lower()
    Date=request.POST.get('date')
    emailSES=request.session['email']
    userLog=user.objects.get(email_id=emailSES)

    username=userLog.uname
    phoneNO=userLog.phoneNo
    nofp=request.POST.get('noOfp')
    print(LFrom)
    print(emailSES)
    print(Date)
    print(username)
    print(phoneNO)
    offerData=offerARide(email_id=emailSES,uname=username,date=Date,leavingfrom=LFrom,goingto=Gto,noOfPassenger=nofp,phoneNo=phoneNO)
    offerData.save()
    print(offerData)
    return HttpResponse('200')
   except:
    return HttpResponse('401')
   
      
  
  else:
     try:   
      login=request.session['login']
      username=request.session['username']
      return render(request,'offerRide.html',{'login':login,'username':username})
     except:
      login=False
      return render(request,'offerRide.html',{'login':login})

def offerRide(request):
   print("offerRide")


def searchRide(request):
   if(request.method=="POST"):
    
      print("getRide")
      LFrom=request.POST.get('from').lower()
      Gto=request.POST.get('to').lower()
      Date=request.POST.get('date')
      print(Date)
      if offerARide.objects.filter(date=Date,leavingfrom=LFrom,goingto=Gto):
          offerData=offerARide.objects.filter(date=Date,leavingfrom=LFrom,goingto=Gto).only()
          offerJSON=serialize("json",offerData)
          print(offerJSON)
          return HttpResponse(offerJSON)
      else:
        return HttpResponse("404")

   else:
      try:   
       login=request.session['login']
       username=request.session['username']
       return render(request,'search.html',{'login':login,'username':username})
      except:
       login=False
       return render(request,'search.html',{'login':login})
    

def otpScreen(request):
    
     if(request.method=="GET"):
      return  render(request,'otp.html')  
     else:
        otpCode=request.POST.get('otpCode')
        code= request.session['otpcode']
        emailId=request.session['email'] 
        passWord=request.session['password']
        username=request.session['username']
        phoneNo=request.session['phoneNo']
        request.session['login']=True
      
        if otpCode==code:
          userData=user(uname=username,email_id=emailId, password=passWord,phoneNo=phoneNo)
          userData.save()
          return HttpResponseRedirect("/")
        else:
           messages.error(request,'incorrect code')
           return render(request,'otp.html') 
        
       
   
 
 
 
 
 
 
 
 
       