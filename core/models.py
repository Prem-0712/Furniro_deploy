from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    STATE_CHOICES = [
        ('AP', 'Andhra Pradesh'),
        ('AR', 'Arunachal Pradesh'),
        ('AS', 'Assam'),
        ('BR', 'Bihar'),
        ('CT', 'Chhattisgarh'),
        ('GA', 'Goa'),
        ('GJ', 'Gujarat'),
        ('HR', 'Haryana'),
        ('HP', 'Himachal Pradesh'),
        ('JH', 'Jharkhand'),
        ('KA', 'Karnataka'),
        ('KL', 'Kerala'),
        ('MP', 'Madhya Pradesh'),
        ('MH', 'Maharashtra'),
        ('MN', 'Manipur'),
        ('ML', 'Meghalaya'),
        ('MZ', 'Mizoram'),
        ('NL', 'Nagaland'),
        ('OR', 'Odisha'),
        ('PB', 'Punjab'),
        ('RJ', 'Rajasthan'),
        ('SK', 'Sikkim'),
        ('TN', 'Tamil Nadu'),
        ('TG', 'Telangana'),
        ('TR', 'Tripura'),
        ('UP', 'Uttar Pradesh'),
        ('UK', 'Uttarakhand'),
        ('WB', 'West Bengal'),
        ('AN', 'Andaman and Nicobar Islands'),
        ('CH', 'Chandigarh'),
        ('DN', 'Dadra and Nagar Haveli and Daman and Diu'),
        ('DL', 'Delhi'),
        ('JK', 'Jammu and Kashmir'),
        ('LA', 'Ladakh'),
        ('LD', 'Lakshadweep'),
        ('PY', 'Puducherry'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2, choices=STATE_CHOICES)
    pincode = models.IntegerField(default=0, blank= True, null= True)

    def __str__(self):
        return str(self.id)
    
class Furniture(models.Model):

    Category_Choice = [
        ("CHAIR", 'Chair'),
        ("SOFA", 'Sofa'),
        ('TABLE', 'Table')
    ]

    name = models.CharField(max_length=255)
    category = models.CharField(max_length=20, choices= Category_Choice)
    small_description = models.CharField(max_length=255)
    description = models.TextField()
    selling_price = models.IntegerField()
    discounted_price = models.IntegerField()
    percentage = models.IntegerField(default=0)
    price_and_quantity_total = models.IntegerField(default=0)
    furniture_img = models.ImageField(upload_to="furniture_img")

    def __str__(self):
        return str(self.id)
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Furniture, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
    
    @property
    def  price_and_quantity_total(self):
        return self.product.discounted_price * self.quantity
    
class Order(models.Model):
    STATUS_CHOICE = [
        ('PENDING', 'Pending'),
        ('PROCESSING', 'Processing'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    furniture = models.ForeignKey(Furniture, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_at = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices = STATUS_CHOICE, default="PENDING")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return str(self.id)
    