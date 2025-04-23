from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponseRedirect, Http404
from .forms import UserRegisterForm, UserLoginForm,Reviews_Form
from django.contrib import messages
from .models import UserRegister, Review, Product
from django.contrib.auth import authenticate, login ,logout,get_user
from django.contrib.auth.decorators import login_required
from urllib.parse import urlparse
from django.urls import is_valid_path
from django.core.mail import EmailMessage

# Create your views here.


def Home(request):
    return render(request, "home.html")

def SignUp(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            try:
                # Send welcome email
                Subject = 'Account Created In OneCheck'
                Body = 'Welcome, You Have Created an account in OneCheck.'
                email = EmailMessage(Subject, Body, to=[form.cleaned_data.get('email')])
                email.send()

                # Save user info
                form_info = UserRegister(
                    username=form.cleaned_data.get('username'),
                    email=form.cleaned_data.get('email'),
                    password=form.cleaned_data.get('password1')
                )
                form_info.save()

                messages.success(request, '🎉 Your account has been created successfully!')
                return redirect('home')  # or change to '/Products' if you want

            except Exception as err:
                print('There is a problem with your email:', err)
                messages.error(request, '❌ There was a problem sending the email. Please try again.')

        else:
            messages.error(request, '❌ Please fix the errors below.')

    else:
        form = UserRegisterForm()

    return render(request, 'SignUp.html', {'form': form})

@login_required(login_url='/Login')
def Products(request):
    Products= Product.objects.all()
    return render(request, "products.html", {"Products":Products})
@login_required
def about_product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    if product is None:
        return Http404
    if request.method == 'POST':
        form =Reviews_Form(request.POST)
        if form.is_valid():
            form_save=form.save(commit=False)
            form_save.user=request.user
            form_save.product = product
            form_save.save()
            messages.success(request, "Your review has been submitted!")
            print("Review done :",form_save.Review)
            return HttpResponseRedirect(f'/Products/{slug}')
        else:
            form = Reviews_Form()
    else:
        form = Reviews_Form()
    review = Review.objects.filter(product=product)

    return render(request, "about_product.html", {"product": product,'form':form,'Reviews':review})


def Login(request):
    next_url = request.GET.get('next', '/Products')
    if request.method == "POST":
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username').strip()
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                print("Authentication successful for user:", user.username)
                login(request, user)
                print("User is authenticated:", get_user(request).is_authenticated)
                next_url = request.POST.get('next', next_url)
                parsed_url = urlparse(next_url)
                print("next url:", next_url)
                print("Parsed URL netloc:", parsed_url.netloc)
                print("Is valid path:", is_valid_path(next_url))

                if not parsed_url.netloc and is_valid_path(next_url):
                    print('Next URL is valid, redirecting...')
                    return HttpResponseRedirect(next_url)
                else:
                    print('Next URL is invalid or external, redirecting to /Products')
                return HttpResponseRedirect('/Products')
            else:
                print("Authentication failed")
                messages.error(request, "Invalid username or password")
                form.add_error(None, "Invalid username or password")

        else:
            messages.error(request, "Please fix the errors below.")
            print("Form errors:", form.errors)
            print("Non-field errors:", form.non_field_errors())
            for field in form:
                print(f"Field Error: {field.name} - {field.errors}")
    else:
        form = UserLoginForm()
    return render(request, "Login.html", {'form': form, 'next': next_url})


def Logout(request):
    logout(request)
    messages.success(request,'Logout Successful')
    return HttpResponseRedirect('/Home')

def signup_view(request):
    return Home(request)

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

@login_required
def history(request):
    reviews = Review.objects.filter(user=request.user)
    return render(request, 'history.html', {'reviews': reviews})