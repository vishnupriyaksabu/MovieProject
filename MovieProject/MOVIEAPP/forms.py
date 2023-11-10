from django import forms
from . models import Movie
class movie_form(forms.ModelForm):
    class Meta:#used to include field with inthe class and used for return
        model=Movie
        fields=['Name','Desc','Year','Img']#to be edited
        
