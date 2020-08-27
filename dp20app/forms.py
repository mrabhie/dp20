from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
import re

def vname(name):
    m=re.match('[a-zA-Z]+',name)
    if m.group()!=name:
        raise ValidationError("Name is not valid")
    return name


class SampleForm(forms.Form):
    name=forms.CharField(max_length=30,required=True,label="Name :",
    validators=[vname])

    email=forms.EmailField(max_length=100,required=True,label="Email :",
    validators=[validators.MinLengthValidator(10)])

    cemail=forms.EmailField(max_length=100,required=True,label="Confirm Email :")

    ipadrs=forms.CharField(max_length=100,required=True,label="IP Address :",
    validators=[validators.validate_ipv4_address])

    pwd=forms.CharField(max_length=50,required=True,label="Password :",widget=forms.PasswordInput(attrs={'placeholder':"password"}))

    propic=forms.ImageField(required=True,label="Profile Picture :")

    def clean(self,*args,**kwargs):
        cleaned_data=super().clean() #getting all the data that is filled in the form
        email=cleaned_data.get("email")
        cemail=cleaned_data.get("cemail")
        if email==cemail:
            return cleaned_data
        self.add_error('cemail',"Both the emails are not same") #this method will decide to which field we need to show the error
        #self.add_error("fieldname",error message)


    # def clean(self,*args,**kwargs):
    #     cleaned_data=super().clean()#getting all the data that is filled in the form
    #     email=cleaned_data.get("email")
    #     cemail=cleaned_data.get("confirm_email")
    #     if email!=cemail:
    #         raise ValidationError("Emails are not same")#application has got the confussion that 
    #     #to which field we need to display error
    #     return cleaned_data