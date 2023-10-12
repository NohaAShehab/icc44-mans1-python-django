
from django import forms
from tracks.models import Track
from students.models import  Student

class StudentForm(forms.Form):
    name = forms.CharField(label='Student Name')
    age = forms.IntegerField( required=False)
    email = forms.EmailField(required=False)
    image = forms.CharField(required=False)
    track  = forms.ModelChoiceField(Track.get_all_tracks(), required=False)




class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'  # ignore created_at , updated_at
