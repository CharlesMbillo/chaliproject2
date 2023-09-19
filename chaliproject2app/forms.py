from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=10)
    email = forms.EmailField(max_length=254)

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('.com'):
            raise forms.ValidationError('Email address must end with .com')
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if not phone_number.isdigit() or len(phone_number) != 10:
            raise forms.ValidationError('Phone number must be a 10-digit number')
        return phone_number
