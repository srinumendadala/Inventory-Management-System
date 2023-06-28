from django.shortcuts import render, redirect
from .models import Customer, Category, Brands, Supplier, Product, Purchase, Manage
from .forms import BrandsForm, ProductForm, PurchaseForm, ManageForm
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.

# function for add Customer in customer module
def addCustomer(request):
    cust = Customer.objects.all()

    if request.method == 'POST':
        name = request.POST['name']
        mobile = request.POST['mobile']
        balance = request.POST['balance']
        address = request.POST['address']

        data = Customer(name=name, mobile=mobile, balance=balance, address=address)
        data.save()
        return redirect('addCustomer')
    page_num = request.GET.get('page')
    paginator = Paginator(cust, 1)
    try:
        cust = paginator.page(page_num)
    except PageNotAnInteger:
        cust = paginator.page(1)
    except EmptyPage:
        cust = paginator.page(paginator.num_pages)

    context = {'cust':cust}

    return render(request, 'customer.html', context)

def customerSearch(request):
    if request.method == "GET":
        query = request.GET.get('query')
        if query:  # condition is true
            cust = Customer.objects.filter(name__contains=query)
            return render(request, 'customer.html', {'cust': cust})
        else:
            print("No information show based on the search")
            return render(request, 'customer.html', {})

def delete(requst, pk):
    delt = Customer.objects.get(id=pk)
    delt.delete()
    return redirect('addCustomer')

# function for add Category in Category module
def addCategory(request):
    cate = Category.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        data = Category(name=name)
        data.save()
        return redirect('addCategory')
    page_num = request.GET.get('page')
    paginator = Paginator(cate, 1)
    try:
        cate = paginator.page(page_num)
    except PageNotAnInteger:
        cate = paginator.page(1)
    except EmptyPage:
        cate = paginator.page(paginator.num_pages)

    context = {'cate':cate}
    return render(request, 'category.html', context)
def deletecat(request, pk):
    cate2 = Category.objects.get(id=pk)
    cate2.delete()
    return redirect('addCategory')

def categorySearch(request):
    if request.method == "GET":
        query = request.GET.get('query')
        if query:
            cate = Category.objects.filter(name__contains=query)
            return render(request, 'category.html', {'cate': cate})
        else:
            print("No information show based on the search")
            return render(request, 'category.html', {})


def addBrand(request):
    brand = Brands.objects.all()
    form = BrandsForm()
    if request.method == 'POST':
        form = BrandsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('addBrand')

    page_num = request.GET.get('page')
    paginator = Paginator(brand, 1)
    try:
        brand = paginator.page(page_num)
    except PageNotAnInteger:
        brand = paginator.page(1)
    except EmptyPage:
        brand = paginator.page(paginator.num_pages)

    context = {'form':form, 'brand':brand}
    return render(request, 'brandList.html', context)
def deletebrand(request, pk):
    brand1 = Brands.objects.get(id=pk)
    brand1.delete()
    return redirect('addBrand')

def addSupplier(request):
    supply = Supplier.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        mobile = request.POST['mobile']
        address = request.POST['address']
        data = Supplier(name=name, mobile=mobile, address=address)
        data.save()
        return redirect('supplier')
    page_num = request.GET.get('page')
    paginator = Paginator(supply, 1)
    try:
        supply = paginator.page(page_num)
    except PageNotAnInteger:
        supply = paginator.page(1)
    except EmptyPage:
        supply = paginator.page(paginator.num_pages)

    context = {'supply':supply}
    return render(request, 'supplier.html', context)
def deletesupplier(request, pk):
    supply1 = Supplier.objects.get(id=pk)
    supply1.delete()
    return redirect('supplier')

def addProduct(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products')
    prod = Product.objects.all()
    page_num = request.GET.get('page')
    paginator = Paginator(prod, 1)
    try:
        prod = paginator.page(page_num)
    except PageNotAnInteger:
        prod = paginator.page(1)
    except EmptyPage:
        prod = paginator.page(paginator.num_pages)
    context = {'form':form ,'prod': prod}
    return render(request, 'product.html', context)
def deleteproduct(request, pk):
    prod1 = Product.objects.get(id=pk)
    prod1.delete()
    return redirect('products')

def addPurchase(request):
    form = PurchaseForm
    if request.method == 'POST':
        form = PurchaseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('purchase')
    purc = Purchase.objects.all()
    page_num = request.GET.get('page')
    paginator = Paginator(purc, 1)
    try:
        purc = paginator.page(page_num)
    except PageNotAnInteger:
        purc = paginator.page(1)
    except EmptyPage:
        purc = paginator.page(paginator.num_pages)
    context = {'form': form, 'purc': purc}
    return render(request, 'purchase.html', context)
def deletepurchase(request, pk):
    purc1 = Purchase.objects.get(id=pk)
    purc1.delete()
    return redirect('purchase')

def manage(request):
    form = ManageForm()
    if request.method == 'POST':
        form = ManageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('manage')
    mana = Manage.objects.all()
    page_num = request.GET.get('page')
    paginator = Paginator(mana, 1)
    try:
        mana = paginator.page(page_num)
    except PageNotAnInteger:
        mana = paginator.page(1)
    except EmptyPage:
        mana = paginator.page(paginator.num_pages)
    context = {'mana': mana, 'form':form}
    return render(request, 'manage.html', context)
def deleteorder(request, pk):
    mana1 = Manage.objects.get(id=pk)
    mana1.delete()
    return redirect('manage')

def home(request):
    products = Product.objects.all()
    purchase = Purchase.objects.all()
    context = {'products': products, 'purchase': purchase}
    return render(request, 'home.html', context)


def login(request):
    if request.method == "POST": # (POST == POST) True
        username = request.POST['username']  # raju
        password = request.POST['password']  # welcome@123

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "Login successfully")
            return redirect('home')
        else:
            messages.error(request, "Invalid Credientials")
            return redirect('login')
    else:
        return render(request, 'login.html')

# LogOut
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        print("Logged Out from Website")
        return redirect('login')

def edit_customer(request):
    cust = Customer.objects.all()

    context = {'cust':cust}
    return redirect(request, 'customer.html', context)

def update_customer(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        balance = request.POST.get('balance')

        cust = Customer(
            id=id,
            name=name,
            mobile=mobile,
            address=address,
            balance=balance,
        )
        cust.save()
        return redirect('addCustomer')
    return redirect(request, 'customer.html')


def edit_category(request):
    cate = Category.objects.all()

    context = {'cate':cate}
    return redirect(request, 'category.html', context)

def updateCategory(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        cate = Category(id=id, name=name)
        cate.save()

        return redirect('addCategory')
    return redirect(request, 'category.html')

def edit_supplier(request):
    supply = Supplier.objects.all()

    context = {'supply': supply}
    return redirect(request, 'supplier.html', context)

def updateSupplier(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')

        supply = Supplier(id=id, name=name, mobile=mobile, address=address)
        supply.save()

        return redirect('supplier')
    return redirect(request, 'supplier.html')