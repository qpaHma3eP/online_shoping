from django.shortcuts import render
from .models import Category, Product, Cart


# Create your views here.
# Главная страница
def home_page(request):
    # Достаем данные из БД
    products = Product.objects.all()
    categories = Category.objects.all()
    # Передаем данные Frontend
    context = {'products': products, 'categories': categories}

    return render(request, 'home.html', context)
