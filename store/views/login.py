from django.shortcuts import render , redirect , HttpResponseRedirect
from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import View
from django.contrib.auth import authenticate, login, logout
#from . import models


class Login(View):
    return_url = None

    def get(self, request):
        Login.return_url = request.GET.get ('return_url')
        return render (request, 'login.html')

    def post(self, request):
        phone = request.POST.get ('phone')
        password = request.POST.get ('password')
        customer = Customer.get_customer_by_phone (phone)
        #user = authenticate(username = phone, password = password)
        error_message = None
        if customer:
            flag = check_password (password, customer.password)
            #login(request, user)
            if flag:
                request.session['customer'] = customer.id

                if Login.return_url:
                    return HttpResponseRedirect (Login.return_url)
                else:
                    Login.return_url = None
                    return render(request,'base2.html')
            else:
                error_message = 'Invalid !!'
        else:
            error_message = 'Invalid !'

        print (phone, password)
        return render (request, 'base2.html', {'error': error_message})

def logout(request):
    request.session.clear()
    return redirect('login')