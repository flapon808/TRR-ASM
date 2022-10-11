from django.shortcuts import render, redirect, reverse 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import Group
from . forms import RestaurantForm, CommentForm
# Create your views here.
from .models import *

# @login_required
# def restaurant (request):
@login_required(login_url='login')
def searchBar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            products = Restaurant.objects.filter(price__icontains=query) 
            return render(request, 'searchbar.html', {'products':products})
        else:
            print("No information to show")
            return render(request, 'searchbar.html', {})

@login_required(login_url='login')
def add_comment(request, pk):
    eachProduct = Restaurant.objects.get(id=pk)

    form = CommentForm(instance=eachProduct)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=eachProduct)
        if form.is_valid():
            name = request.user.username
            body = form.cleaned_data['comment_body']
            c = Comment(product=eachProduct, commenter_name=name, comment_body=body, date_added=datetime.now())
            c.save()
            return redirect('showProducts')
        else:
            print('form is invalid')    
    else:
        form = CommentForm()    


    context = {
        'form': form
    }

    return render(request, 'add_comment.html', context)

@login_required(login_url='login')
def delete_comment(request, pk):
    comment = Comment.objects.filter(product=pk).last()
    product_id = comment.product.id
    comment.delete()
    return redirect(reverse('product', args=[product_id]))