from django.shortcuts import render
from .models import Product, Category
import random


# Create your views here.
def index(request):
    categories = list(Category.objects.all())
    random.shuffle(categories)
    products = list(Product.objects.all())[0:12]
    random.shuffle(products)

    context = {
        'products': products,
        'categories': categories,
        # 'featured' : Category.objects.all()[0]
    }

    return render(request, 'index.html', context)

def product_single(request, product_id):
    product = Product.objects.get(pk=product_id)
    category = product.category
    related = category.products.all()
    context = {
        'product' : product,
        'related' : related
    }
    return render(request, 'product-single.html', context)
def products_by_cat(request, category_id):
    category = Category.objects.get(pk=category_id)
    context = {
        'products' : Product.objects.filter(category=category),
        'categories' : Category.objects.all(),
        'selected' : category
    }

    print(context['products'])

    return render(request, 'product.html', context)

def products(request):
    context = {
        'products': Product.objects.all(),
        'categories': Category.objects.all()
    }

    return render(request, 'product.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST['email']
        message = request.POST['message']
        context = {
            'message' :"Message Sent. Feel free to email us directly"
        }
        return render(request, 'contact.html', context)
    return render(request, 'contact.html')


def about(request):
    return render(request, 'contact.html')
