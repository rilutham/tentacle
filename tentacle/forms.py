from django import forms
from .models import Activity

class AddActivityForm(forms.Form):
    name = forms.CharField(max_length=20)
    description = forms.CharField(max_length=140)
    parent = forms.ModelChoiceField(queryset=Activity.objects.filter(parent_activity_id=0), initial={0:''})

class EditActivityForm(forms.Form):
    name = forms.CharField(max_length=20, label="Activity name")
    description = forms.CharField(max_length=140, label="Description")

class IncreaseHourForm(forms.Form):
    CHOICES = [('pos', 'Add'), ('neg', 'Sub')]
    choice_field = forms.ChoiceField(widget=forms.RadioSelect(), choices=CHOICES, initial='pos')
    num = forms.CharField(max_length=4)
    note = forms.CharField(max_length=140, required=False)



