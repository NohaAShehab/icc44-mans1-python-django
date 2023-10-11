

from django import  forms
from tracks.models import Track
from django.core.exceptions import ValidationError



class TrackForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField(required=False)
    image = forms.ImageField(required=False)

    # define validation rule in forms.py

    def clean_name(self):

        # cleaned data
        found = Track.objects.filter(name=self.cleaned_data['name']).exists()
        if found:
            raise ValidationError("Track name already exists")
        return self.cleaned_data['name']


