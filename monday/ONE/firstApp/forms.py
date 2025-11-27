from django import ModelForm
from .models import Fruits

class FruitsForm(ModelForm):
    class Meta:
        model = Fruits
        fields = '__all__'