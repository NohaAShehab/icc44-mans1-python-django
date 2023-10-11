

from django import forms
from tracks.models import Track


class StudentForm(forms.Form):
    name = forms.CharField(label='Student Name')
    age = forms.IntegerField( required=False)
    email = forms.EmailField(required=False)
    image = forms.CharField(required=False)
    track  = forms.ModelChoiceField(Track.get_all_tracks(), required=False)


