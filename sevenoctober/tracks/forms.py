

from django import  forms


class TrackForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField()
    image = forms.ImageField()


