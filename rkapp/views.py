import requests
from django.shortcuts import render
from rkapp.models import registertable,feedback,profiledb
import requests
import messages
from django.contrib import messages

# Create your views here.
def profile(request):
    return render(request,'profile-settings.html')

def help(request):
    return render(request,'support-center.html')

def register(request):
    return render(request,'auth-register.html')

def login(request):
    return render(request,'auth-login.html')

def ftd(request):
    if request.method == 'POST':
        uemail = request.POST.get("email")
        upass = request.POST.get("password")
        try:
            userdetails = registertable.objects.get(email=uemail,cpassword=upass)
            request.session['logid'] = userdetails.id
            request.session['logname'] = userdetails.fname
            request.session['mobile'] = userdetails.contact_no
            request.session['email1'] = userdetails.email
            request.session.save()
        except:
            userdetails = None
        if userdetails is not None:
            return render(request,'dashboard-analytics.html')
        else:
            messages.error(request,"incorrect email and password")
    else:
        pass
    return render(request,'auth-login.html')

def fb(request):
    if request.method == 'POST':
        ans = request.POST.get("n")
        feedback1 = feedback(answer=ans)
        feedback1.save()
        messages.success(request,"You are Successfully Registered")
    else:
        pass
    return render(request,'support-center.html')

def logout(request):
    try:
        del request.session['login']
        del request.session['logname']
    except:
        pass
    return render(request,'auth-login.html')

def dashboard(request):
    records = {}
    dataurl = requests.get("https://lds123.000webhostapp.com/dashboard.php")
    smokedata = dataurl.json()
    records['alldata'] = smokedata
    print(records)
    return render(request,'dashboard-analytics.html',records)

def fetchdata(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        firstname = request.POST.get("fname")
        mobile_no = request.POST.get("contact_no")
        newpassword = request.POST.get("npassword")
        conpassword = request.POST.get("cpassword")
        insertdata = registertable(email=email,fname=firstname,contact_no=mobile_no,npassword=newpassword,cpassword=conpassword)
        insertdata.save()
        messages.success(request,"You are Successfully Registered")
    else:
        pass
    return render(request,'auth-login.html')

def water(request):
    records = {}
    dataurl = requests.get("https://lds123.000webhostapp.com/watersensordata.php")
    waterdata = dataurl.json()
    records['waterlivedata'] = waterdata
    return render(request, 'water.html', records)

def smoke(request):
    records = {}
    dataurl = requests.get("https://lds123.000webhostapp.com/smokesensordata.php")
    smokedata = dataurl.json()
    records['smokelivedata'] = smokedata
    return render(request, 'smoke.html', records)

def gas(request):
    records = {}
    dataurl = requests.get("https://lds123.000webhostapp.com/gassensordata.php")
    gasdata = dataurl.json()
    records['gaslivedata'] = gasdata
    return render(request, 'gas.html', records)

def profiledata(request):
    if request.method == 'POST':
        industry = request.POST.get("industry")
        company = request.POST.get("company")
        address = request.POST.get("address")
        country = request.POST.get("country")
        state = request.POST.get("state")
        zip = request.POST.get("zip")
        logid= request.session['logid']
        insertdata = profiledb(address=address,pincode=zip,uid=registertable(id=logid),country=country,state=state,industry=industry,company=company)
        insertdata.save()
        messages.success(request,"Your profile is updated.")
    else:
        pass
    return render(request,'profile-settings.html')

def about(request):
    return render(request,'about.html')
