from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
STATE_CHOICES =(
    ('Dhaka', 'Dhaka'),
    ('Tangail', 'Tangail'),
    ('Barguna', 'Barguna'),
    ('Barishal', 'Barishal'),
    ('Bhola', 'Bhola'),
    ('Jhalokati', 'Jhalokati'),
    ('Patuakhali', 'Patuakhali'),
    ('Pirojpur', 'Pirojpur'),
    ('Bandarban', 'Bandarban'),
    ('Brahmanbaria', 'Brahmanbaria'),
    ('Chandpur', 'Chandpur'),
    ('Chattogram', 'Chattogram'),
    ('Cumilla', 'Cumilla'),
    ('Coxs Bazar', 'Coxs Bazar'),
    ('Feni', 'Feni'),
    ('Khagrachhari', 'Khagrachhari'),
    ('Lakshmipur', 'Lakshmipur'),
    ('Noakhali', 'Noakhali'),
    ('Rangamati', 'Rangamati'),
    ('Faridpur', 'Faridpur'),
    ('Gazipur', 'Gazipur'),
    ('Gopalganj', 'Gopalganj'),
    ('Kishoreganj', 'Kishoreganj'),
    ('Madaripur', 'Madaripur'),
    ('Manikganj', 'Manikganj'),
    ('Munshiganj', 'Munshiganj'),
    ('Narayanganj', 'Narayanganj'),
    ('Narsingdi', 'Narsingdi'),
    ('Rajbari', 'Rajbari'),
    ('Shariatpur', 'Shariatpur'),
    ('Bagerhat', 'Bagerhat'),
    ('Jashore', 'Jashore'),
    ('Khulna', 'Khulna'),


)


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    zipCode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=50)

    def __str__(self):
        return str(self.id)


CATEGORY_CHOICES = (
    ('M', 'Mobile'),
    ('l', 'Laptop'),
    ('TW', 'Top Wear'),
    ('BW', 'Bottom Wear'),
)


class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted = models.FloatField()
    brand = models.CharField(max_length=50)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)


STATE_CHOICES = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('on The Way', 'on The Way'),
    ('Delivered', 'Delivered'),
    ('Cancel', 'Cancel')
)


class OrderPlaced(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
   product = models.ForeignKey(Product, on_delete=models.CASCADE)
   quantity = models.PositiveIntegerField(default=1)
   ordered_date = models.DateTimeField(auto_now_add=True)
   status = models.CharField(max_length=50, choices=STATE_CHOICES, default='Pending')
