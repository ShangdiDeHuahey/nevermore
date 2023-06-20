from django import forms
from .models import ContactModel

class ContactForm(forms.ModelForm):
    class Meta:
      model = ContactModel
      fields = ['first_name', 'email_address', 'phone_number', 'message',]
      widgets={
        'first_name': forms.TextInput(attrs={'placeholder': 'Имя'}),
        'email_address': forms.TextInput(attrs={'placeholder': 'Email'}),
        'phone_number': forms.TextInput(attrs={'placeholder': 'Номер телефона'}),
        'message': forms.TextInput(attrs={'placeholder': 'Сообщение'})
      }
      labels = {
            'first_name': '',
            'last_name': '',
            'email_address': '',
            'phone_number': '',
            'message': '',
        }
      required_css_class = 'contact__form'