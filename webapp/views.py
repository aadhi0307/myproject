from django.shortcuts import render,redirect
from myapp.models import categorydb,productdb
from webapp.models import userdb,contactdb,cartdb
from django.contrib import messages

# Create your views here.

def home(req):
    data = categorydb.objects.all()
    return render(req,"homepage.html",{"data":data})
def aboutus(req):
    return render(req,"aboutus.html")
def contactus(req):
    cat=categorydb.objects.all()
    return render(req,"contactus.html",{"cat":cat})
def categories(req,catname):
    data=categorydb.objects.all()
    pro=productdb.objects.filter(category=catname)
    return render(req,"categories.html",{"data":data,"pro":pro})
def singleproduct(req,dataid):
    pro_single=productdb.objects.get(id=dataid)
    cat=categorydb.objects.all()
    return render(req,"singleproduct.html",{"pro_single":pro_single,"cat":cat})
def userlogin(req):
    return render(req,"userlogin.html")
def userdata(req):
    if req.method=="POST":
        na=req.POST.get('name')
        em=req.POST.get('email')
        mb=req.POST.get('mobile')
        im=req.FILES['image']
        pswd = req.POST.get('pwd')
        cpswd = req.POST.get('cpwd')
        obj=userdb(name=na,email=em,mobile=mb,image=im,pwd=pswd,cpwd=cpswd)
        obj.save()
        messages.success(req, "Signup successfully")
        return redirect(userlogin)
def usersignin(req):
    if req.method=="POST":
        uname=req.POST.get('name')
        pwd=req.POST.get('pwd')
        if userdb.objects.filter(name=uname,pwd=pwd).exists():
            req.session['name']=uname
            req.session['pwd']=pwd
            messages.success(req, "Login successfully")
            return redirect(home)
        else:
            messages.error(req, "incorrect username or password")
            return redirect(userlogin)
    return redirect(userlogin)
def contactdata(req):
    if req.method=="POST":
        na=req.POST.get('user')
        em=req.POST.get('email')
        sb=req.POST.get('subject')
        mg=req.POST.get('message')
        obj=contactdb(name=na,email=em,subject=sb,message=mg)
        obj.save()
        return redirect(contactus)

def userlogout(req):
    del req.session['name']
    del req.session['pwd']
    return redirect(userlogin)
def cartpage(req):
    data=cartdb.objects.filter(username=req.session['name'])
    cat=categorydb.objects.all()
    return render(req,"cart.html",{"data":data,"cat":cat})

def cartdata(req):
    if req.method=="POST":
        na=req.POST.get('uname')
        pn=req.POST.get('pname')
        ds=req.POST.get('description')
        qy=req.POST.get('qty')
        pr=req.POST.get('totalprice')
        obj=cartdb(username=na,pname=pn,description=ds,quantity=qy,price=pr)
        obj.save()
        messages.success(req, "Added to cart")
        return redirect(cartpage)
def checkoutpage(req):
    return render(req,"checkoutpage.html")