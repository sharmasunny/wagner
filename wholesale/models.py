from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.signals import post_init


class Order(models.Model):
    # order_id
    # customer_id
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    # order_status
    order_value = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.created_date


class Product(models.Model):
    product_id = models.PositiveIntegerField()
    list_no = models.PositiveIntegerField()
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    colour_code = models.CharField(blank=True,null= True,max_length=3)
    protected_variety = models.BooleanField(default=False)
    category_id = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    # order_id
    # product_id
    quantity = models.PositiveIntegerField()
    comments = models.CharField(max_length=50)

    def __str__(self):
        return self.quantity


class ColourClass(models.Model):
    colour_code = models.CharField(max_length=3)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name_plural = "Colour classes"


class ProductCategory(models.Model):
    category_id = models.PositiveIntegerField()
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name_plural = "Product categories"


class NewRelease(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(blank=True, null=True)
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    description=models.CharField(max_length=10000000,null=True)

    def __str__(self):
        return self.name


######################Order Model#########################
class Order_Item(models.Model):
    order_id=models.AutoField(primary_key=True,unique=True,verbose_name='order_id')
    user=models.IntegerField(default=0)
    order_list=models.CharField(max_length=10000000,null=True)
    timestamp=models.DateTimeField(null=True, verbose_name='created on')
    price=models.CharField(max_length=100000,verbose_name='price')

    def __str__(self):
        return self.order_id



######################User_info Model#########################
class UserInfo(models.Model):
    info_id=models.AutoField(primary_key=True,unique=True,verbose_name='info_id')
    user=models.ForeignKey(User)
    business_name=models.CharField(max_length=100,null=True,verbose_name='business_name')
    address=models.CharField(max_length=10000000,null=True,verbose_name='address')
    town=models.CharField(max_length=100,null=True,verbose_name='town')
    post_code=models.CharField(max_length=10000000,null=True,verbose_name='post_code')
    phone=models.CharField(max_length=10000000,null=True,verbose_name='phone')
    fax=models.CharField(max_length=10000000,null=True,verbose_name='fax')
    contact_name=models.CharField(max_length=10000000,null=True,verbose_name='contact_name')
    delivery_instructions=models.CharField(max_length=10000000,null=True,verbose_name='delivery_instructions')

    def __str__(self):
        return self.business_name
    