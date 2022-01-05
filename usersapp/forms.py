from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from django.forms import fields

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Dirección de Email'}))
    first_name = forms.CharField(help_text="Ingrese su primer nombre" ,label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese su Nombre' }))
    last_name = forms.CharField(help_text="Ingrese su primer apellido" ,label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese su Apellido'}))


    class Meta:#la clase Meta se utiliza para señalar al modelo y las tablas del modelo
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    #widget de imagen de los campos del formulario en forms.py
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].label = ''
        self.fields['username'].help_text = ''

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Ingrese su Clave'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = 'Ingrese su clave con los parametros exigidos'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirme su Clave'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = 'Confirme su clave sin error'


class EditProfileForm(UserChangeForm):
    password = forms.CharField(label="", widget=forms.TextInput(attrs={'type':'hidden' })) #esto desaparece el link de password en edit_profile.html
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password',)
