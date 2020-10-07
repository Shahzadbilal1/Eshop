from django.shortcuts import render
from django.http import HttpResponse
from .models.customer import Customer
from .models.product import Product
from .models.category import Category


# Create your views here.
def index(request):
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products();
    data = {}
    data['products'] = products
    data['categories'] = categories
    return render(request, 'index.html', data)


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        # Validation
        error_message = None
        if (not first_name):
            error_message = "first name Required !!"
        elif len(first_name) < 4:
            error_message = "First name must be 4 char long or more"
        elif not last_name:
            error_message = "last name Required !!"
        elif len(last_name) < 4:
            error_message = "last name must be 4 char long or more"
        elif not phone:
            error_message = "Phone Number Required !!"
        elif len(phone) < 10:
            error_message = "Phone Number must be 4 char long or more"
        elif len(password) < 6:
            error_message = "Password must be 6 char long or more"
        elif len(email) < 6:
            error_message = "email must be 6 char long or more"

        # Saving
        if not error_message:
            print(first_name, last_name, phone, email, password)
            customer = Customer(first_name=first_name,
                                last_name=last_name,
                                phone=phone,
                                email=email,
                                password=password)
            customer.register()
            return render(request, 'signup.html')
        else:
            return render(request, 'signup.html', {'error': error_message})
