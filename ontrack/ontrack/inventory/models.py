from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
# Create your models here.

class Clothes(models.Model):
    TEES = 'Tee(s)'
    PANTS = 'Pant(s)'
    JEANS = 'Jeans'
    SHIRTS = 'Shirt(s)'
    SHORTS = 'Shorts'
    UNDERGARMENTS = 'Undergarment(s)'
    SOCKS = 'Socks'
    ETHNICTOP = 'Ethnic Top(s)'
    ETHNICBOTTOM = 'Ethnic Bottom(s)'
    TOP = 'Top(s)'
    SKIRT = 'Skirt(s)'
    LEGGINGS = 'Leggings'
    DRESS = 'Dress(es)'
    
    FORMAL = 'Formal'
    CASUAL = 'Casual'
    SEMIFORMAL = 'Semi-Formal'
    NIGHTWEAR = 'Nightwear'
    
    TYPE_CHOICES = (
    	(TEES,'Tee(s)'),
    	(PANTS,'Pants'),
    	(JEANS,'Jeans'),
    	(SHIRTS,'Shirt(s)'),
    	(SHORTS,'Shorts'),
    	(UNDERGARMENTS,'Undergarment(s)'),
    	(SOCKS,'Socks'),
    	(ETHNICTOP,'Ethnic Top(s)'),
    	(ETHNICBOTTOM,'Ethnic Bottom(s)'),
    	(TOP,'Women\'s Top(s)'),
    	(SKIRT,'Skirt(s)'),
    	(LEGGINGS,'Leggings/Skins'),
    	(DRESS,'Women\'s Dress(es)'),
    )
    
    CATEGORY_CHOICES = (
    (FORMAL,'Formal Wear'),
    (CASUAL, 'Casual Wear'),
    (SEMIFORMAL, 'Semi-Formal Wear'),
    (NIGHTWEAR,'Night Wear'),
    )
    
    COLOUR_CHOICES = (
	('White','White'),    
    ('Red','Red'),
    ('Black','Black'),
    ('Blue','Blue'),
    ('Brown','Brown'),
    ('Yellow','Yellow'),
    ('Orange','Orange'),
    ('Purple','Purple'),
    ('Green','Green'),
    ('Grey','Grey'),
    ('Pink','Pink'),
    ('Custom Colour','Custom Colour'),
    )
    quantity = models.IntegerField(db_column = 'Qty')
    types = models.CharField(choices=TYPE_CHOICES,max_length =20,blank=False,db_column = 'Type')
    category = models.CharField(choices=CATEGORY_CHOICES,max_length =20,blank=False,db_column = 'Category')
    colour = models.CharField(choices=COLOUR_CHOICES,max_length =20,db_column = 'Colour')
    tag = models.TextField(max_length=35)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.tag
    
    
class Books(models.Model):
	isbn = models.IntegerField(primary_key=True,db_column='ISBN')
	name = models.CharField(db_column='Book Name', max_length=30)
	author = models.CharField(db_column = 'Author Name',max_length=20)
	date_issued = models.DateField(db_column='Date of Issue')
	date_of_return = models.DateField(db_column='Date of Return')
	user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
	
	
class Feedback(models.Model):
	customer_name = models.CharField(max_length=50,db_column='Name')
	email = models.EmailField()
	details = models.TextField()
	happy = models.BooleanField()
	date = models.DateField(auto_now_add = True)
	user = models.ForeignKey(User, on_delete = models.CASCADE, default=None)


class Fitness(models.Model):
    RUN = "Run"
    CYCLE = "Cycle Ride"
    BALL = "Basketball"
    YOGA = "Yoga"
    TENNIS = "Tennis"
    FOOTBALL = "Football"
    CRICKET =  "Cricket"
    BADMINTON  = "Badminton"
    CROSSFIT = "CrossFit"
    WEIGHTS = "Weight Lifting"
    JUMP_ROPE = "Jump Rope"
    SWIM = "Swimming"

    CATEGORY_CHOICES = (
            (RUN , "Run"),
            (CYCLE , "Cycle Ride"),
            (BALL ,"Basketball"),
            (YOGA , "Yoga"),
            (TENNIS , "Tennis"),
            (FOOTBALL , "Football"),
            (CRICKET , "Cricket"),
            (BADMINTON  , "Badminton"),
            (CROSSFIT , "CrossFit"),
            (WEIGHTS , "Weight Lifting"),
            (JUMP_ROPE , "Jump Rope"),
            (SWIM , "Swimming"),
    )
    
    user = models.ForeignKey(User, on_delete = models.CASCADE, default=None)
    duration = models.IntegerField()
    weight = models.FloatField(validators = [MinValueValidator(1)])
    calories = models.FloatField()
    category = category = models.CharField(choices=CATEGORY_CHOICES,max_length =20,blank=False,db_column = 'Category')
    created_date = models.DateTimeField(
    default=timezone.now)
    

    def __str__(self):
        return str((self.created_date, self.calories))
