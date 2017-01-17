from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import NewRelease,Product,ProductCategory,Order_Item,UserInfo
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.models import User
from datetime import datetime
import sys
import ast
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login

from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password


'''
from django.core.mail import send_mail

send_mail(
    'Subject here',
    'Here is the message.',
    'from@example.com',
    ['to@example.com'],
    fail_silently=False,
)
'''

#########################User Login###############################
@csrf_exempt
def user_login(request):
    try:
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)  
            return HttpResponse('success')
        else:
            return HttpResponse('error')
    except Exception as e:
        print (e)

#######################Ends Here##################################
@login_required()
def home(request):
    template = "home.html"
    title = "Home"

    context = {
        "title": title,
    }

    return render(request, template, context)
############################Ends Here###########################

#############################New Releases Page##################
@login_required()
def new_releases(request):
    template = "newrelease.html"
    title = "New Releases"

    context = {
        "title": title,
        "new_releases": NewRelease.objects.all(),
    }

    return render(request, template, context)

######################Ends Here################################

###################My Details Page#############################
@login_required()
def mydetails(request):
    try:
        active_user=request.user
        active_user_id=request.user.id
        template = "user_details.html"
        title = "My Details"
        User_details_list=[]
        User_details_dict={'user_id':'','username':'','email':'','firstname':'','lastname':'','date_joined':'','last_login':'','status':'',
        'info_id':'','business_name':'','address':'','town':'','post_code':'','phone':'','fax':'','contact_name':'',
        'delivery_instructions':''}
        user_info=User.objects.filter(username=active_user)
        for user in user_info:
            user_id=user.id
            user_username=user.username
            user_email=user.email
            user_firstname=user.first_name
            user_lastname=user.last_name
            user_status=user.is_active
            date_joined=user.date_joined
            time_register=date_joined.strftime("%B %d, %Y, %I:%M %p")
            last_login=user.last_login
            time_last_login=last_login.strftime("%B %d, %Y, %I:%M %p")
            userinfo_data=UserInfo.objects.filter(user_id=active_user_id)
            for data in userinfo_data:
                User_details_dict['info_id']=data.info_id
                User_details_dict['business_name']=data.business_name
                User_details_dict['address']=data.address
                User_details_dict['town']=data.town
                User_details_dict['post_code']=data.post_code
                User_details_dict['phone']=data.phone
                User_details_dict['fax']=data.fax
                User_details_dict['contact_name']=data.contact_name
                User_details_dict['delivery_instructions']=data.delivery_instructions
                User_details_dict['user_id']=user_id
                User_details_dict['username']=user_username
                User_details_dict['email']=user_email
                User_details_dict['firstname']=user_firstname
                User_details_dict['lastname']=user_lastname
                User_details_dict['date_joined']=time_register
                User_details_dict['last_login']=time_last_login
                User_details_dict['status']=user_status
                User_details_list.append(User_details_dict.copy())
        context = {
            "title": title,
            "User_Info": User_details_list,
        }

        return render(request, template, context)
    except Exception as e:
        print(e)
#######################Ends Here###########################


########################Contact Us Page##################
@login_required()
def contact(request):
    try:
        template = "contact.html"
        title = "Contact Us"

        context = {
            "title": title,
        }

        return render(request, template, context)
    except Exception as e:
        print (e)
#######################Ends Here###########################

##################Render Order Page########################
@login_required()
def order(request):
    try:
        categories_list=[]
        categories_dict={'category_name':'','category_id':''}
        category_info=ProductCategory.objects.all()
        for cat_info in category_info:
            category_name=cat_info.description
            category_id=cat_info.category_id
            categories_dict['category_name']=category_name
            categories_dict['category_id']=category_id
            categories_list.append(categories_dict.copy())
        products_list=[]
        products_dict={'product_id':'','product_name':'','price':'','color_code':'','list_no':'','protected_variety':''}
        products=Product.objects.filter(category_id='1')
        for product in products:
            product_id=product.product_id
            product_name=product.name
            price=product.price
            color_code=product.colour_code
            protected_variety=product.protected_variety
            list_no=product.list_no
            products_dict['product_id']=product_id
            products_dict['product_name']=product_name
            products_dict['price']=price
            products_dict['color_code']=color_code
            products_dict['protected_variety']=protected_variety
            products_dict['list_no']=list_no
            products_list.append(products_dict.copy())
        template = "order.html"
        title = "Order"
        context = {
            "title": title,
            "categories":categories_list,
            "products":products_list,
        }

        return render(request, template, context)
    except Exception as e:
        print (e)

###########################Ends Here#####################################


##################Get Products for a particular Category########################
@login_required()
@csrf_exempt
def get_products(request):
    try:
        products_list=[]
        products_dict={'product_id':'','product_name':'','price':'','color_code':'','list_no':'','protected_variety':''}
        category_id=request.POST['category_id']
        products=Product.objects.filter(category_id=category_id)
        for product in products:
            product_id=product.product_id
            product_name=product.name
            price=product.price
            color_code=product.colour_code
            protected_variety=product.protected_variety
            list_no=product.list_no
            products_dict['product_id']=product_id
            products_dict['product_name']=product_name
            products_dict['price']=price
            products_dict['color_code']=color_code
            products_dict['protected_variety']=protected_variety
            products_dict['list_no']=list_no
            products_list.append(products_dict.copy())
        try:
            html= render_to_string('category_products.html',{'products':products_list})
            return HttpResponse(html)
        except Exception as e:
            print (e.__cause__)
    except Exception as e:
        print (e)
###############################Ends Here###############################

##################Save order to database########################
@login_required()
@csrf_exempt
def save_order(request):
    try:
        order_data=request.POST['order_data']
        price=request.POST['total_price']
        timestamp=str(datetime.now())
        order=Order_Item.objects.create(user=request.user.id,order_list=order_data,timestamp=timestamp,price=price)
        order.save()
        return HttpResponse('success')
    except Exception as e:
        print (e)
#########################Ends Here############################

##################View Orders of a user########################
@login_required()
@csrf_exempt
def view_orders(request):
    try:
        template = "my_orders.html"
        title = "My Orders"
        order_info_list=[]
        order_info_dict={'order_id':'','price':'','timestamp':''}
        user_id=request.user.id
        order_data=Order_Item.objects.filter(user=user_id)
        for data in order_data:
            order_id=data.order_id
            price=data.price
            timestamp=data.timestamp
            time_register=timestamp.strftime("%B %d, %Y, %I:%M %p")
            order_info_dict['order_id']=order_id
            order_info_dict['price']=price
            order_info_dict['timestamp']=time_register
            order_info_list.append(order_info_dict.copy())
        context = {
            "title": title,
            "orders": order_info_list
        }
        return render(request, template, context)
    except Exception as e:
        print (e)
#########################Ends Here#################################

##################View Particular Order info########################
@login_required()
@csrf_exempt
def order_info(request,id):
    try:
        template = "order_info.html"
        title = "View Order"
        order_info_list=[]
        order_info_dict={'order_id':'','price':'','order_list':'','timestamp':''}
        user_id=request.user.id
        order_data=Order_Item.objects.filter(user=user_id).filter(order_id=id)
        for data in order_data:
            order_id=data.order_id
            price=data.price
            timestamp=data.timestamp
            time_register=timestamp.strftime("%B %d, %Y, %I:%M %p")
            order_list=data.order_list
            final_order_list = ast.literal_eval(order_list)
            order_info_dict['order_id']=order_id
            order_info_dict['price']=price
            order_info_dict['order_list']=final_order_list
            order_info_dict['timestamp']=time_register
            order_info_list.append(order_info_dict.copy())
        context = {
            "title": title,
            "order_info": order_info_list
        }
        return render(request, template, context)
    except Exception as e:
        print (e)

#########################Ends Here############################

##################Delete Particular Order########################\
@login_required()
@csrf_exempt
def delete_order(request):
    try:
        order_id=request.POST['order_id']
        order = Order_Item.objects.get(order_id=order_id)
        order.delete()
        return HttpResponse('success')
    except Exception as e:
        print (e)
#########################Ends Here############################

##################Edit User Profile########################
@login_required()
@csrf_exempt
def edit_profile(request):
    try:
        user_id=request.POST['user_id']
        username=request.POST['username']
        contact_name=request.POST['contact_name']
        business_name=request.POST['business_name']
        delivery_instructions=request.POST['delivery_instructions']
        user_email=request.POST['email']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        phone_number=request.POST['phone_number']
        fax=request.POST['fax']
        address=request.POST['address']
        town=request.POST['town']
        post_code=request.POST['post_code']
        try:
            user_emails = User.objects.filter(email=user_email)
            if user_emails:
                email = User.objects.filter(email=user_email).filter(id=user_id)
                if email:
                    user_data = User.objects.filter(id=user_id).update(username=username,first_name=first_name,last_name=last_name,email=user_email)
                    user_info = UserInfo.objects.filter(user_id=user_id).update(business_name=business_name,address=address,town=town,
                        post_code=post_code,phone=phone_number,fax=fax,contact_name=contact_name,delivery_instructions=delivery_instructions)
                    return HttpResponse('success')
                else:
                    return HttpResponse('duplicate_email')
            else:
                user_data = User.objects.filter(id=user_id).update(username=username,first_name=first_name,last_name=last_name,email=user_email)
                user_info = UserInfo.objects.filter(user_id=user_id).update(business_name=business_name,address=address,town=town,
                        post_code=post_code,phone=phone_number,fax=fax,contact_name=contact_name,delivery_instructions=delivery_instructions)
                return HttpResponse('success')
        except Exception as e:
            return HttpResponse('duplicate_user')
    except Exception as e:
        print (e)
#########################Ends Here############################

##################Change Password Function########################
@login_required()
@csrf_exempt
def change_password(request):
    try:
        user_email=request.POST['user_email']
        old_password=request.POST['old_password']
        changed_password=request.POST['changed_password']
        try:
            password_change = User.objects.filter(email=user_email)
            for pas in password_change:
                savedpassword = pas.password
                check_your_password=check_password(old_password, savedpassword)
                if (check_your_password == True): 
                    enc_password=make_password(changed_password)
                    user_data = User.objects.filter(email=user_email).update(password=enc_password)
                    return HttpResponse('success')
                else:
                    return HttpResponse('wrong_password')
        except Exception as e:
            print (e)
    except Exception as e:
        print (e)
#########################Ends Here############################