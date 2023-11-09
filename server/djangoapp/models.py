from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
# User model
class CarMake(models.Model):
    name = models.CharField(null=False, max_length=30, default='')
    description = models.CharField(null=False, max_length=30, default='')
    
    def __str__(self):
        return self.name + " " + self.description


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    name = models.CharField(null=False, max_length=100, default='car name')
    dealer_id = models.IntegerField(max_length=500)
    SEDAN = "sedan"
    SUV="SUV"
    WAGON="Wagon"
    Type_CHOICES = [
        (SEDAN, "Sedan"),
        (SUV, "SUV"),
        (WAGON, "WAGON"),
    ]
    type = models.CharField(null=False, max_length=100,choices=Type_CHOICES,
 default='car name')
    year = models.DateField(null=True)

    carmake = models.ForeignKey(CarMake, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return "Name: " + self.name + "," + \
            "dealer_id: " + self.dealer_id

# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
