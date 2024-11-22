from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.messages import constants as messages
from .forms import UserRegisterForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages  # Correct import for messages
from .forms import UserRegisterForm
from django.shortcuts import render, get_object_or_404
from .models import Category
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Category, Cart, CartItem
from .forms import CartAddForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Category, Cart, CartItem
from .forms import CartAddForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Category, Cart, CartItem


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Category, Cart, CartItem


from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import UserRegisterForm


from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import UserRegisterForm

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import UserRegisterForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import UserRegisterForm




# Create your views here.
from django.shortcuts import render


  # Ensure you have a template named `test.html`


from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import UserRegisterForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import UserRegisterForm
@csrf_exempt
def home_page(request):
    return render(request, 'HomePage.html')  # Template name and location
@csrf_exempt
def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful')
            return redirect('test')  # Ensure this URL pattern exists
        else:
            messages.error(request, 'Registration failed. Please try again.')
    else:
        form = UserRegisterForm()
    
    context = {'form': form}
    return render(request, 'UserRegister.html', context)
@csrf_exempt
def test_view(request):
    return render(request, 'test.html')  # Template name and location

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful')
                return redirect('home_page')  # Redirect to home page after successful login
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})




def test_view(request):
    return render(request, 'test.html')

# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category
from .forms import CategoryForm

from django.shortcuts import render
from .models import Category

from django.shortcuts import render
from .models import Category



def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'category_form.html', {'form': form})

def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category_form.html', {'form': form})

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    else:
        return render(request, 'category_confirm_delete.html', {'category': category})




# @login_required
# def category_detail(request, pk):
#     category = get_object_or_404(Category, pk=pk)
#     cart, created = Cart.objects.get_or_create(user=request.user)
#     cart_count = sum(item.quantity for item in cart.items.all())
#     cart_items = cart.items.all()
#     return render(request, 'category_detail.html', {'category': category, 'cart_count': cart_count, 'cart_items': cart_items})




# @login_required
# def add_to_cart(request, pk):
#     category = get_object_or_404(Category, pk=pk)
#     cart, created = Cart.objects.get_or_create(user=request.user)
#     cart_item, created = CartItem.objects.get_or_create(cart=cart, category=category)
#     cart_item.quantity += 1
#     cart_item.save()
#     return redirect('cart_detail')

# @login_required
# def remove_from_cart(request, pk):
#     category = get_object_or_404(Category, pk=pk)
#     cart = Cart.objects.get(user=request.user)
#     cart_item = get_object_or_404(CartItem, cart=cart, category=category)
#     if cart_item.quantity > 1:
#         cart_item.quantity -= 1
#         cart_item.save()
#     else:
#         cart_item.delete()
#     return redirect('cart_detail')



# @login_required
# def cart_detail(request):
#     cart, created = Cart.objects.get_or_create(user=request.user)
#     cart_items = cart.items.all()
#     cart_count = sum(item.quantity for item in cart_items)  # Summing up the quantity of each item
#     return render(request, 'cart_detail.html', {'cart': cart, 'cart_items': cart_items, 'cart_count': cart_count})





from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Category, Cart, CartItem

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Category, Cart, CartItem, Comment
from .forms import CommentForm

from django.shortcuts import render, get_object_or_404
from .models import Category

from django.shortcuts import render, get_object_or_404
from .models import Category, Cart, CartItem
from .forms import CommentForm

from django.shortcuts import redirect, get_object_or_404
from .models import Category, Cart, CartItem
from django.shortcuts import render, get_object_or_404
from .models import Cart, CartItem


from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, CartItem
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, CartItem
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.shortcuts import render, get_object_or_404
from .models import Category

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Category, CartItem

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Category, CartItem
from django.shortcuts import render, get_object_or_404
from .models import Category, CartItem
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404
from .models import Category, CartItem
from .forms import CommentForm

@login_required
def category_list(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'category_list.html', context)

@login_required


def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)
        cart_count = cart_items.count()
    else:
        cart_items = []
        cart_count = 0

    context = {
        'category': category,
        'cart_count': cart_count,
        'cart_items': cart_items,
        'comments': category.comments.all(),
        'form': CommentForm() if request.user.is_authenticated else None,
    }
    return render(request, 'category_detail.html', context)

@login_required

def add_to_cart(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, category=category)

        if not created:
            cart_item.quantity += 1
            cart_item.save()
        else:
            cart_item.price = category.price
            cart_item.save()

    return redirect('cart_detail')

from django.shortcuts import redirect, get_object_or_404
from .models import Category, Cart, CartItem

@login_required

def remove_from_cart(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.user.is_authenticated:
        cart = get_object_or_404(Cart, user=request.user)
        cart_item = get_object_or_404(CartItem, cart=cart, category=category)
        
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()

    return redirect('cart_detail')


@login_required

def cart_detail(request):
    if request.user.is_authenticated:
        cart = get_object_or_404(Cart, user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)
        total_price = sum(item.price * item.quantity for item in cart_items)
    else:
        cart_items = []
        total_price = 0

    context = {
        'cart_items': cart_items,
        'total_price': total_price  # Include total price in the context
    }
    return render(request, 'cart_detail.html', context)




from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta

@login_required
def continue_shopping(request):
    end_time = timezone.now() + timedelta(hours=24)
    return render(request, 'continue_shopping.html', {'end_time': end_time})



from django.shortcuts import render, redirect
from .models import Address
from .forms import AddressForm

def continue_shopping(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            return redirect('home_page')  # Redirect to the home page or any other page after saving the address
    else:
        form = AddressForm()

    return render(request, 'continue_shopping.html', {'form': form})
