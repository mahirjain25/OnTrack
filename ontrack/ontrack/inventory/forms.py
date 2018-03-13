from django import forms            
from inventory.models import Clothes


class AddClothesForm(forms.Form):
	 category = forms.ChoiceField(label='Category of cloth to be added.',choices = Clothes.CATEGORY_CHOICES,required = True)
	 types = forms.ChoiceField(label = 'Type of cloth to be added', choices = Clothes.TYPE_CHOICES,required = True)
	 colour = forms.ChoiceField(label = 'Colour', choices = Clothes.COLOUR_CHOICES,required = True)
	 quantity = forms.IntegerField(label = 'Quantity of such clothes',required = True)
	 tag = forms.CharField(label = 'Short, optional description of item', required = False,max_length=20)
	 
	

	

