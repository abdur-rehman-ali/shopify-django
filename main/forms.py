# Django Imports 
from django import forms
from django.contrib.auth.forms import (
  UserCreationForm,
  AuthenticationForm,
  PasswordChangeForm
)
from django.contrib.auth.models import User

# Local imports
from .models import Product

class CustomerRegistrationForm(UserCreationForm):
  """
    A custom registration form for customers.
  """
  password1 = forms.CharField(
    label='Password', 
    widget=forms.PasswordInput(attrs={'class': 'form-control'})
  )
  password2 = forms.CharField(
    label='Confirm Password(Again)', 
    widget=forms.PasswordInput(attrs={'class': 'form-control'})
  )
  email = forms.CharField(
    required=True,
    widget=forms.EmailInput(attrs={'class': 'form-control'})
  )

  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']
    labels = {'email': 'Email'}
    widgets= {'username': forms.TextInput(attrs= {'class': 'form-control'})}

class CustomerLoginForm(AuthenticationForm):
  """
    A custom login form for customers.
  """
  username = forms.CharField(
    widget=forms.TextInput(attrs={'class': 'form-control'})
  )
  password = forms.CharField(
    widget=forms.PasswordInput(attrs={'class': 'form-control'})
  )

class CustomerPasswordChangeForm(PasswordChangeForm):
  """
    A custom password change form for customers.
  """
  old_password = forms.CharField(
      label="Old Password",
      widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
  new_password1 = forms.CharField(
      label='New Password', 
      widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
  new_password2 = forms.CharField(
      label='New Password Confirmation', 
      widget=forms.PasswordInput(attrs={'class': 'form-control'})
    ) 

class AddressForm(forms.Form):
  """
    A adress form for user's addresses.
  """
  street = forms.CharField(
    max_length=255,
    widget=forms.TextInput(attrs={'class': 'form-control'})
  )
  state = forms.CharField(
    max_length=100,
    widget=forms.TextInput(attrs={'class': 'form-control'})
  )
  city = forms.CharField(
    max_length=100,
    widget=forms.TextInput(attrs={'class': 'form-control'})
  )
  country = forms.CharField(
    max_length=100,
    widget=forms.TextInput(attrs={'class': 'form-control'})
  )
  zip_code = forms.CharField(
    max_length=100,
    widget=forms.TextInput(attrs={'class': 'form-control'})
  )
  phone_number = forms.CharField(
    max_length=20,
    widget=forms.TextInput(attrs={'class': 'form-control'})
  )

CATEGORIES = (
  ('Mobile','Mobile'),
  ('Laptop','Laptop'),
  ('Top Wear','Top Wear'),
  ('Bottom Wear','Bottom Wear'),
)

class ProductForm(forms.Form):
  """
    A form for products.
  """
  title = forms.CharField(
    max_length=100,
    widget=forms.TextInput(attrs={'class': 'form-control'})
  )
  description = forms.CharField(
    widget=forms.Textarea(attrs={'class': 'form-control'})
  )
  selling_price = forms.FloatField(
    widget=forms.NumberInput(attrs={'class': 'form-control'})
  )
  discounted_price = forms.FloatField(
    widget=forms.NumberInput(attrs={'class': 'form-control'})
  )
  category = forms.ChoiceField(
    choices=CATEGORIES,
    widget=forms.Select(attrs={'class': 'form-control'})
  )
  brand = forms.CharField(
    max_length=100,
    widget=forms.TextInput(attrs={'class': 'form-control'})
  )
  product_image = forms.ImageField(
    widget=forms.FileInput(attrs={'class': 'form-control'})
  )

  def clean(self):
      cleaned_data = super().clean()
      selling_price = cleaned_data.get('selling_price')
      discounted_price = cleaned_data.get('discounted_price')
      if selling_price is not None and discounted_price is not None:
        if discounted_price > selling_price:
          raise forms.ValidationError("Discounted price cannot be greater than selling price.")

  def save(self):
    product_data = {
      'title': self.cleaned_data['title'],
      'description': self.cleaned_data['description'],
      'selling_price': self.cleaned_data['selling_price'],
      'discounted_price': self.cleaned_data['discounted_price'],
      'brand': self.cleaned_data['brand'],
      'category': self.cleaned_data['category'],
      'product_image': self.cleaned_data['product_image'],
    }
    product = Product(**product_data)
    product.save()
