from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from main_riss.models import *
 #session on login
# Create your views here.
#login table
def index(request):
    return render(request, 'home.html')

#registration table
def reg(request):
    if request.method=='POST':
        fnames=request.POST['fname']
        lnames=request.POST['lname']
        u_name=request.POST['uname']
        u_phone=request.POST['phone']
        u_mail=request.POST['email']
        u_pass=request.POST['pass']
        c_pass=request.POST['cpass']
        utype=request.POST['u_type']
        
        print(u_name)
        
        if u_pass==c_pass:
            q2=user_log(user_name=u_name,user_pass=u_pass,user_type=utype)
            q2.save()
            q=user(f_name=fnames,l_name=lnames,phone=u_phone,email=u_mail,logins=q2)
            q.save()
    return render(request,'reg.html')


#product table
def products(request):
    if request.method =="POST":
        pname=request.POST['p_names']
        pprice=request.POST['p_prices']
        pquant=request.POST['p_quants']
        pcat=request.POST['p_cats']
        
        qp=product(p_name=pname,p_cat=pcat,p_price=pprice,p_quant=pquant)
        qp.save()
    return render(request,'product.html')

#login form and queries
def login(request):
    if request.method=='POST':
        u_name=request.POST['uname']
        u_pass=request.POST['pass']
        try:
            lg=user_log.objects.get(user_name=u_name,user_pass=u_pass)
            if lg:
                if lg.user_type=='admin':
                    request.session['lid']=lg.id
                    ses=(request.session['lid'])
                    print(ses)
                    return HttpResponseRedirect('admin')
                elif lg.user_type=='user':
                    return HttpResponseRedirect('user_dashboard')
        except:
            return HttpResponseRedirect('login')
    return render(request, 'login.html')

#trying css
def home_css(request):
    return render(request,'product.css')

#admin dashboard
def admin(request):
    qlist=user.objects.all()
    return render(request,'admin.html',{"list":qlist})
    
#user dashboard
def user_dashboard(request):
    return render(request,'user.html')

#view products
def view_products(request):
    view_pr=product.objects.all()
    return render(request,'view_products.html',{"pr_list":view_pr})

#update products
def product_update(request,id):
    updateproduct=product.objects.get(id=id)
    if request.method=='POST':
        u_pname=request.POST['p_names']
        u_pcat=request.POST['p_cats']
        u_pprice=request.POST['p_prices']
        u_pquant=request.POST['p_quants']
        
        updateproduct.p_name=u_pname
        updateproduct.p_cat=u_pcat
        updateproduct.p_price=u_pprice
        updateproduct.p_quant=u_pquant
        updateproduct.save()
        return HttpResponseRedirect('/view_products')
    return render(request,'product_update.html',{"product_update":updateproduct})

# def productdelete(request,id):
#     dele=ins.objects.get(id=id)
#     dele.delete()    
#     return HttpResponseRedirect('/productview')
             
#delete product from table                                         
def pd_delete(request,id):
    del_pr=product.objects.get(id=id)
    del_pr.delete()
    return HttpResponseRedirect('/view_products')
