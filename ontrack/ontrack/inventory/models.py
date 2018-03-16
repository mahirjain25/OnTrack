from django.db import models
from django.utils import timezone

# Create your models here.

class Clothes(models.Model):
    TEES = 'TEE'
    PANTS = 'PNT'
    JEANS = 'JNS'
    SHIRTS = 'SHR'
    SHORTS = 'SHT'
    UNDERGARMENTS = 'UNG'
    SOCKS = 'SCK'
    ETHNICTOP = 'ETT'
    ETHNICBOTTOM = 'ETB'
    TOP = 'TOP'
    SKIRT = 'SKT'
    LEGGINGS = 'LEG'
    DRESS = 'DRS'
    
    FORMAL = 'FL'
    CASUAL = 'CL'
    SEMIFORMAL = 'SF'
    NIGHTWEAR = 'NW'
    
    TYPE_CHOICES = (
    	(TEES,'Tees'),
    	(PANTS,'Pants'),
    	(JEANS,'Jeans'),
    	(SHIRTS,'Shirts'),
    	(SHORTS,'Shorts'),
    	(UNDERGARMENTS,'Undergarments'),
    	(SOCKS,'Socks'),
    	(ETHNICTOP,'Ethnic Top'),
    	(ETHNICBOTTOM,'Ethnic Bottom'),
    	(TOP,'Women\'s Top'),
    	(SKIRT,'Skirt'),
    	(LEGGINGS,'Leggings/Skins'),
    	(DRESS,'Women\'s Dress'),
    )
    
    CATEGORY_CHOICES = (
    (FORMAL,'Formal Wear'),
    (CASUAL, 'Casual Wear'),
    (SEMIFORMAL, 'Semi-Formal Wear'),
    (NIGHTWEAR,'Night Wear'),
    )
    
    COLOUR_CHOICES = (
	('WT','White'),    
    ('RD','Red'),
    ('BL','Black'),
    ('BE','Blue'),
    ('BR','Brown'),
    ('YL','Yellow'),
    ('OR','Orange'),
    ('PL','Purple'),
    ('GR','Green'),
    ('GY','Grey'),
    ('PK','Pink'),
    ('OT','Other'),
    )
    quantity = models.IntegerField(db_column = 'Qty')
    types = models.CharField(choices=TYPE_CHOICES,max_length=3,blank=False,db_column = 'Type')
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=2,blank=False,db_column = 'Category')
    colour = models.CharField(choices=COLOUR_CHOICES,max_length=2,db_column = 'Colour')
    tag = models.TextField(max_length=20)
    
    
class Books(models.Model):
	isbn = models.IntegerField(primary_key=True,db_column='ISBN')
	name = models.CharField(db_column='Book Name', max_length=30)
	author = models.CharField(db_column = 'Author Name',max_length=20)
	date_issued = models.DateField(db_column='Date of Issue')
	date_of_return = models.DateField(db_column='Date of Return')
    
    
