from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages, auth
from .forms import UserLoginForm, UserRegistrationForm

# Create your views here.
def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect("home")
    
def login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
            
            if user is not None:
                auth.login(request, user)
                messages.success(request, "You have successfully logged in")
                return redirect("home")
            else:
                form.add_error(None, "Your username or password was not recognised")
            
    
    form = UserLoginForm()

    return render(request, "accounts/login.html", {"form": form})
    
def profile(request):
    return render(request, "accounts/profile.html")
    
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            user = auth.authenticate(username=request.POST.get('username'),
                                     password=request.POST.get('password1'))

            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                return redirect('profile')

            else:
                messages.error(request, "unable to log you in at this time!")

    else:
        form = UserRegistrationForm()


    return render(request, 'accounts/register.html', {'form': form})