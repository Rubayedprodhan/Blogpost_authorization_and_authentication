from django.shortcuts import render,redirect
from . import forms
# Create your views here.
def add_categories(request):
    if request.method=='POST':
        create_categories=forms.CategoryForm(request.post)
        if create_categories.is_valid():
            create_categories.save()
            return redirect('add_categories')
    else: 
        category_form = forms.CategoryForm()
    return render(request, 'addCategories.html', {'form' : category_form})


