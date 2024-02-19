# new
from django.forms import ModelForm,TextInput,EmailInput
from .models import Customer

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
            'name' : TextInput(attrs={'class':'form-control'}),
            'email' : EmailInput(attrs={'class':'form-control'}),
            'username' : TextInput(attrs={'class':'form-control'}),
            'password' : TextInput(attrs={'class':'form-control'})
        }