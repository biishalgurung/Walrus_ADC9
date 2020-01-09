from django import forms
from .models import Calc

#DataFlair
class CalcCreate(forms.ModelForm):

    class Meta:
        model = Calc
        fields = '__all__'