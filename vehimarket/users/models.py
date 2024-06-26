from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class users(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    u_fname=models.TextField(max_length=50,db_column='firstname',default='null',null=False)
    u_lname=models.TextField(max_length=50,db_column='lastname',default='null',null=False)
    u_dob=models.DateField(db_column='dateofbirth',default='2023-10-02',null=False)
    u_contact=models.CharField(max_length=50,db_column='contactinfo',default='1234567890',null=False)
    u_house=models.TextField(max_length=50,db_column='house',default='null',null=False)
    u_place=models.TextField(max_length=50,db_column='place',default='null',null=False)
    u_pin=models.TextField(max_length=50,db_column='pincode',default='null',null=False)
    u_profile=models.ImageField(upload_to='profile/',db_column='profileimage',default='null',null=False)

    def __str__(self):
        return self.user.username

class CarListing(models.Model):
    STATUS_CHOICES = (
        ('available', 'Available'),
        ('sold', 'Sold'),
    )

    FUEL_TYPE_CHOICES = (
        ('petrol', 'Petrol'),
        ('diesel', 'Diesel'),
        ('electric', 'Electric'),
        ('hybrid', 'Hybrid'),
    )
    OWNER_CHOICES = (
        ('first', 'First'),
        ('second', 'Second'),
        ('third','Third'),
    )

    seller = models.ForeignKey(users, on_delete=models.CASCADE)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='available')
    date_added = models.DateField(auto_now_add=True)
    engine_type = models.CharField(max_length=50)
    transmission_type = models.CharField(max_length=50)
    exterior_color = models.CharField(max_length=50)
    interior_color = models.CharField(max_length=50)
    fuel_type = models.CharField(max_length=50, choices=FUEL_TYPE_CHOICES, default='petrol')
    kilometer_driven = models.PositiveIntegerField()
    owner=models.CharField(max_length=10, choices=OWNER_CHOICES,default='first')
    image_1 = models.ImageField(upload_to='car_images/', null=True, blank=True)
    image_2 = models.ImageField(upload_to='car_images/', null=True, blank=True)
    image_3 = models.ImageField(upload_to='car_images/', null=True, blank=True)
    image_4 = models.ImageField(upload_to='car_images/', null=True, blank=True)
    image_5 = models.ImageField(upload_to='car_images/', null=True, blank=True)
  
    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
    

class TestDrive(models.Model):
    date = models.DateField()
    time_slot = models.CharField(max_length=20)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.date} {self.time_slot}"
    

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Assuming you have a User model
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class CarBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car_listing = models.ForeignKey(CarListing, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.car_listing} - Date: {self.date}"
    
class Payment(models.Model):
    booking = models.ForeignKey('CarBooking', on_delete=models.CASCADE)
    car = models.ForeignKey('CarListing', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for Booking ID {self.booking_id}"
    


class Accessory(models.Model):
    accessory_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.CharField(max_length=100)
    CATEGORY_CHOICES = [
        ('audio', 'Audio'),
        ('body_parts', 'Body Parts'),
        ('exterior', 'Exterior'),
        ('interior', 'Interior'),
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    quantity = models.IntegerField()
    warranty = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when the object is first created

    def __str__(self):
        return self.accessory_name
    
class AccessoryImage(models.Model):
    accessory = models.ForeignKey(Accessory, related_name='images', on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to='accessory_images/',null=True, blank=True)
    image2 = models.ImageField(upload_to='accessory_images/',null=True, blank=True)
    image3 = models.ImageField(upload_to='accessory_images/',null=True, blank=True)
    image4 = models.ImageField(upload_to='accessory_images/',null=True, blank=True)
    # You can add additional fields if needed, such as caption or description

    def __str__(self):
        return f"Image for {self.accessory.accessory_name}"
    

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name
    

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    accessories = models.ManyToManyField('Accessory')
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Wishlist for {self.user.username}"
    

class AddToCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    accessory = models.ForeignKey(Accessory, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.accessory.accessory_name} ({self.quantity})"
    

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # accessory = models.ForeignKey(Accessory, on_delete=models.CASCADE, default=1)  
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    razorpay_order_id = models.CharField(max_length=255)
    # quantity = models.PositiveIntegerField(default=1)  
    payment_datetime = models.DateTimeField(default='2024-04-04T00:00:00Z')  # Set a default value

    class PaymentStatusChoices(models.TextChoices):
        PENDING = 'Pending', 'Pending'
        SUCCESSFUL = 'Successful', 'Successful'
        FAILED = 'Failed', 'Failed'
    
    payment_status = models.CharField(
        max_length=20,
        choices=PaymentStatusChoices.choices,
        default=PaymentStatusChoices.PENDING
    )
    
    def __str__(self):
        return f"Order {self.id} - {self.user.username} - {self.payment_status}"
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    accessory = models.ForeignKey(Accessory, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Order Item {self.id} - {self.order_id} - {self.accessory.accessory_name} - {self.quantity}"


class AccessoryPayment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    accessory = models.ForeignKey(Accessory, on_delete=models.CASCADE)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_datetime = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=20, default='Pending')
    quantity = models.PositiveIntegerField(default=1)  # New field for quantity

    def __str__(self):
        return f"Accessory Payment {self.id} - {self.accessory.accessory_name}"