"""wagner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'wholesale.views.home', name='home'),
    url(r'^user_login/', 'wholesale.views.user_login', name='user_login'),
    url(r'^newreleases/', 'wholesale.views.new_releases', name='new_releases'),
    url(r'^order/', 'wholesale.views.order', name='order'),
    url(r'^save_order/', 'wholesale.views.save_order', name='save_order'),
    url(r'^get_products/', 'wholesale.views.get_products', name='get_products'),
    url(r'^view_orders/', 'wholesale.views.view_orders', name='view_orders'),
    url(r'^order_info/(?P<id>\d+)/$','wholesale.views.order_info',name='order_info'),
    url(r'^delete_order/', 'wholesale.views.delete_order', name='delete_order'),
    url(r'^contact/', 'wholesale.views.contact', name='contact'),
    url(r'^mydetails/', 'wholesale.views.mydetails', name='mydetails'),
    url(r'^edit_profile/', 'wholesale.views.edit_profile', name='edit_profile'),
    url(r'^change_password/', 'wholesale.views.change_password', name='change_password'),
]
