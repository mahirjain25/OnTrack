from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Clothes(models.Model):
    TEES = 'TEEs'
    PANTS = 'PANTS'
    JEANS = 'JEANS'
    SHIRTS = 'SHIRT'
    SHORTS = 'SHORTS'
    UNDERGARMENTS = 'UNDERGARMENTS'
    SOCKS = 'SOCKS'
    ETHNICTOP = 'ETHNIC TOP'
    ETHNICBOTTOM = 'ETHNIC BOTTOM'
    TOP = 'TOP'
    SKIRT = 'SKIRT'
    LEGGINGS = 'LEGGINGS'
    DRESS = 'DRESS'
    
    FORMAL = 'FORMAL'
    CASUAL = 'CASUAL'
    SEMIFORMAL = 'SEMI-FORMAL'
    NIGHTWEAR = 'NIGHT-WEAR'
    
    TYPE_CHOICES = (
    	(TEES,'Tee(s)'),
    	(PANTS,'Pants'),
    	(JEANS,'Jeans'),
    	(SHIRTS,'Shirt(s)'),
    	(SHORTS,'Shorts)'),
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
    ('Other','Other'),
    )
    quantity = models.IntegerField(db_column = 'Qty')
    types = models.CharField(choices=TYPE_CHOICES,max_length =10,blank=False,db_column = 'Type')
    category = models.CharField(choices=CATEGORY_CHOICES,max_length =10,blank=False,db_column = 'Category')
    colour = models.CharField(choices=COLOUR_CHOICES,max_length =10,db_column = 'Colour')
    tag = models.TextField(max_length=20)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.tag
    
    
class Books(models.Model):
	isbn = models.IntegerField(primary_key=True,db_column='ISBN')
	name = models.CharField(db_column='Book Name', max_length=30)
	author = models.CharField(db_column = 'Author Name',max_length=20)
	date_issued = models.DateField(db_column='Date of Issue')
	date_of_return = models.DateField(db_column='Date of Return')
    
    
