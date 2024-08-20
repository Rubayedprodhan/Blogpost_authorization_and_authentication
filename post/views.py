# from django.shortcuts import render, redirect
# from . import forms
# from . import models
# # Create your views here.
# from django.contrib.auth.decorators import login_required

# def post_new(request):
#     if request.method=='POST':
#         post=forms.PostForm(request.post)
#         if post.is_valid():
#             post.instance.register = request.user
#             post.save()
#             return redirect('add_post')
#     else:
#         post=forms.PostForm
#     return redirect(request,'addpost.html',{'form':post})

# @login_required
# def edit_post(request,id):
#     post_id=models.post.objects.get(pk=id)
#     post=forms.PostForm(instance=post_id)
#     if request.method=='POST':
#         post=forms.PostForm(request.POST , instance=post)
#         if post.is_valid():
#             post.instance.register = request.user
#             post.save()
#             return redirect('homepage')
        

# @login_required
# def delete_post(request, id):
#     post = models.post.objects.get(pk=id) 
#     post.delete()
#     return redirect('homepage')
from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from . import models
from django.contrib.auth.decorators import login_required

@login_required
def post_new(request):
    if request.method == 'POST':
        form = forms.PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('homepage')  
    else:
        form = forms.PostForm()
    return render(request, 'addpost.html', {'form': form})

@login_required
def edit_post(request, id):
    post = get_object_or_404(models.post, pk=id)
    if request.method == 'POST':
        form = forms.PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('homepage') 
    else:
        form = forms.PostForm(instance=post)
    return render(request, 'addpost.html', {'form': form})

@login_required
def delete_post(request, id):
    post = get_object_or_404(models.post, pk=id)
    post.delete()
    return redirect('homepage')  
