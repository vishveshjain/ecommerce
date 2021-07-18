from django.db import models

# Create your models here.
class productData(models.Model):
    # productImage = models.ImageField( upload_to='productImages')
    productName = models.CharField(max_length=200)
    productPrice = models.IntegerField()
    productQuantity = models.IntegerField()
    productSize = models.CharField( max_length=50)
    productColor = models.CharField( max_length=50)

class billingAddress(models.Model):
    firstName = models.CharField( max_length=50)
    lastName = models.CharField( max_length=50)
    email = models.EmailField( max_length=254)
    mobile = models.IntegerField()
    address = models.TextField()
    country = models.CharField( max_length=50)
    city = models.CharField( max_length=50)
    state = models.CharField( max_length=50)
    zipCode = models.CharField( max_length=50)

