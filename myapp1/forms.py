from django import forms
from .models import Person, Person2


class CreatePersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'


class CreatePerson2Form(forms.ModelForm):
    class Meta:
        model = Person2
        fields = '__all__'

class Update2Form(forms.ModelForm):
    class Meta:
        model = Person2
        fields = '__all__'




        



