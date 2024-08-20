from django.shortcuts import render
from post.models import post
from categories.models import Category
def home(request, category_slug = None):  
    
    data = post.objects.all() 
    if category_slug is not None:
        category = Category.objects.get(slug = category_slug) 
        data = post.objects.filter(category  = category) 
    categories = Category.objects.all() 
    return render(request, 'home.html', {'data' : data, 'category' : categories})