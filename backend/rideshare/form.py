from django import forms
from django.forms import ModelForm, widgets
from .models import *

class userRegForm(forms.ModelForm):
    class Meta:
      model=user
      fields='__all__'
      widgets={
          "uname":forms.TextInput(attrs={"type":"text" ,"id":"userName", "placeholder":"User Name", "autocomplete":"off"}),
          "email_id":forms.TextInput(attrs={"type":"email","id":"email", "placeholder":"Email Id","name":"email", "autocomplete":"off"}),
          "password":forms.TextInput(attrs={"type":"password","id":"password", "placeholder":"Password","name":"password", "autocomplete":"off"}),
      }
      