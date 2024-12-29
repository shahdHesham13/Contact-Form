from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 
                                    'placeholder': 'Your Name'}))
    email = forms.EmailField(required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control',
                                     'placeholder': 'Your Email'}))
    subject = forms.CharField(max_length=200, required=True,
        widget=forms.TextInput(attrs={'class': 'form-control',
                                    'placeholder': 'Subject'}))
    message = forms.CharField(required=True,
        widget=forms.Textarea(attrs={'class': 'form-control',
                                   'placeholder': 'Your Message',
                                   'rows': 4}))

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.strip():
            raise forms.ValidationError("Email is required")
        return email
