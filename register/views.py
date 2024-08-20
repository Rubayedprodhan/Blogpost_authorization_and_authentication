from django.shortcuts import render,redirect
from . import forms
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from post.models import post

def register(request):
    if request.method=='POST':
        register_form=forms.Registerfrom()
        if register_form.is_valid():
            register_form.save()
            messages.success(request,"Account Created Successfully")
            return redirect('register')

    else:
        register_form=forms.Registerfrom()

    return render(request,'register.html',{'form':register_form,'type':'Register'})
# def user_loging(request):
#     if request.method== 'POST':
#         form=AuthenticationForm(request,request.POST)
#         if form.is_valid():
#             username=form.cleaned_data['username']
#             user_pass=form.cleaned_data['password']
#             user=authenticate(username=username,password=user_pass)
#             if user is not None:
#                 messages.success(request,"Logged in Successfully")
#                 login(request,user)
#                 return redirect('profile')
#             else:
#                 messages.warning(request, 'Login informtion incorrect')
#                 return redirect('register')
            
#         else:
#             form=AuthenticationForm()
#         return render(request,'register.html',{'form':form,'type':'login'})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username=username, password=user_pass)
            if user is not None:
                messages.success(request, "Logged in Successfully")
                login(request, user)
                return redirect('profile')
            else:
                messages.warning(request, 'Login information incorrect')
        else:
            messages.warning(request, 'Invalid form submission')
    else:
        form = AuthenticationForm()

    return render(request, 'register.html', {'form': form, 'type': 'login'})

@login_required
def profile(request):
    data = post.objects.filter(author=request.user)
    return render(request, 'profile.html', {'data':data})

@login_required
def profile_edit(request):
    if request.method=="POST":
        profile_form=forms.ChangeUserFrom(request.POST,intance=request.post)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, "Profile Updated successfully")
            return redirect('profile')
    else:
        profile_form =forms.ChangeUserFrom(instance = request.user)
    return render(request, 'updateprofile.html', {'form' : profile_form})

def profile_edit_password_change(request):
    if request.method=='POST':
        form=PasswordChangeForm(request.user,data=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,'Password Updated Successfully')
            update_session_auth_hash(request,form.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'passchange.html', {'form' : form})
def user_logout(request):
    logout(request)
    return redirect('user_loging')
