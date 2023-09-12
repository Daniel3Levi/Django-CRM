from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, NewRecordForm
from .models import Record


# Create your views here.
def home(request):
    # Get all the records
    records = Record.objects.all()
    # Check if user logging in, not connected = POST req or connected = GET req.
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You logged in successfully!")
            return redirect('home')
        else:
            messages.success(request, "There was an error logging in, please try agine.")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records': records})


def logout_user(request):
    logout(request)
    messages.success(request, "You logged out successfully!")
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You are successfully register!')
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})

    return render(request, 'register.html', {'form': form})


def single_record(request, pk):
    if request.user.is_authenticated:
        # Search record - get single object
        record = Record.objects.get(id=pk)
        return render(request, "record.html", context={"record": record})
    else:
        messages.success(request, "You must logged in to view that page!")
        return redirect('home')


def delete_record(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        record.delete()
        messages.success(request, "The record deleted successfully!")
        return redirect('home')
    else:
        messages.success(request, "You must logged in to view that page!")
        return redirect('home')


def new_record(request):
    form = NewRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, "New record created successfully!")
                return redirect('home')
        return render(request, "new_record.html", context={'form': form })
    else:
        messages.success(request, "You must logged in to view that page!")
        return redirect('home')


def update_record(request,pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = NewRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "New record updated successfully!")
            return redirect('home')
        return render(request, "update_record.html", context={'form': form})
    else:
        messages.success(request, "You must logged in to view that page!")
        return redirect('home')
