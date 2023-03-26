from django import forms
from .models import Note
from django.contrib.auth.models import User

# ------- TO DO LIST SECTION ------------- #
class CreateNewList(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    check = forms.BooleanField(required=False)
# ---------------------------------------- #

#---------Journal-------------------------------#
class NoteCreationForm(forms.ModelForm):
    class Meta:
        model=Note
        fields=['title','description']

class NoteUpdateForm(forms.ModelForm):
    class Meta:
        model=Note
        fields=['title','description']

class AccountSettingsForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name']

#-----------------------------------------------#