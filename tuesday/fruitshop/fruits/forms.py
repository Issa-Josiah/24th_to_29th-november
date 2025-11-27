from django.forms import ModelForm #helps create the model form
from .models import fruit  #importing the fruit of the model

class FruitForm(ModelForm):
    class Meta:
        model = fruit
        fields = '__all__' # or name,description and file








