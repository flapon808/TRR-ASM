from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms






# class OrderForm(ModelForm):
# 	class Meta:
# 		model = Order
# 		fields = '__all__'

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
		widgets = {
            'Name' : forms.TextInput(attrs={'class':'form-control','required':'True', 'placeholder':"Full Name"}),
            'Email' : forms.EmailInput(attrs={'class':'form-control', 'required':'True'}),
            'Gender' : forms.Select(attrs={'class':'form-control', 'required':'True'}),
            'Date_of_Birth' : forms.DateInput(attrs={'class':'form-control', 'type':'date', 'required':'True'}),
		}
