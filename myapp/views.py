from django.shortcuts import render,redirect
from myapp.models import categorydb,productdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from webapp.models import contactdb
from django.contrib import messages
# Create your views here.

def index_page(req):
    return render(req,"index.html")
def category(req):
    return render(req,"addcategory.html")
def categorydata(req):
    if req.method=="POST":
        cn=req.POST.get('cname')
        im=req.FILES['image']
        ds=req.POST.get('description')
        obj=categorydb(cname=cn,image=im,description=ds)
        obj.save()
        messages.success(req,"category added successfully")
        return redirect(category)
def categorydisplay(req):
    data=categorydb.objects.all()
    return render(req, "categorydisplay.html",{'data':data})

def edit_category(req,dataid):
    data=categorydb.objects.get(id=dataid)
    return render(req,"editcategory.html",{"data":data})
def update_category(req,dataid):
    if req.method=="POST":
        cn = req.POST.get('cname')
        ds = req.POST.get('description')
        try:
            img=req.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=categorydb.objects.get(id=dataid).image
        categorydb.objects.filter(id=dataid).update(cname=cn,image=file,description=ds)
        messages.success(req, "category edited successfully")
    return redirect(categorydisplay)
def delete_category(req,dataid):
    data=categorydb.objects.filter(id=dataid)
    data.delete()
    messages.success(req, "category deleted successfully")
    return redirect(categorydisplay)

def addproduct(req):
    data=categorydb.objects.all()
    return render(req,"addproduct.html",{'data':data})

def productdata(req):
    if req.method=="POST":
        ct=req.POST.get('category')
        pn=req.POST.get('pname')
        pr=req.POST.get('price')
        br=req.POST.get('brand')
        pi=req.FILES['pimage']
        dr = req.POST.get('description')
        obj=productdb(category=ct,pname=pn,price=pr,brand=br,pimage=pi,description=dr)
        obj.save()
        messages.success(req,"product added successfully")
        return redirect(addproduct)

def productdisplay(req):
    data=productdb.objects.all()
    return render(req,"productdisplay.html",{"data":data})
def editproduct(req,dataid):
    category=categorydb.objects.all()
    data=productdb.objects.get(id=dataid)
    return render(req,"editproduct.html",{"data":data,"category":category})
def updateproduct(req,dataid):
    if req.method=="POST":
        ct = req.POST.get('category')
        pn = req.POST.get('pname')
        pr = req.POST.get('price')
        br = req.POST.get('brand')
        dr = req.POST.get('description')
        try:
            img=req.FILES['pimage']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=productdb.objects.get(id=dataid).pimage
        productdb.objects.filter(id=dataid).update(category=ct,pname=pn,price=pr,brand=br,pimage=file,description=dr)
        messages.success(req, "product edited successfully")
        return redirect(productdisplay)
def delete_product(req,dataid):
    data=productdb.objects.filter(id=dataid)
    data.delete()
    messages.success(req, "product deleted successfully")
    return redirect(productdisplay)
def loginpage(req):
    return render(req,"loginpage.html")
def admin_login(req):
    if req.method=="POST":
        uname=req.POST.get('username')
        pwd=req.POST.get('pass')
        if User.objects.filter(username__contains=uname).exists():
            user=authenticate(username=uname,password=pwd)
            if user is not None:
                login(req,user)
                req.session['username'] = uname
                req.session['password'] = pwd
                messages.success(req, "Login successfully")
                return redirect(index_page)
            else:
                messages.error(req, "incorrect username or password")
                return redirect(loginpage)
        else:
            messages.error(req, "incorrect username or password")
            return redirect(loginpage)
def admin_logout(req):
    del req.session['username']
    del req.session['password']
    return redirect(loginpage)
def contactdisplay(req):
    data=contactdb.objects.all()
    return render(req,"contactusdisplay.html",{'data':data})
def delete_contactus(req,dataid):
    data=contactdb.objects.filter(id=dataid)
    data.delete()
    return redirect(contactdisplay)


