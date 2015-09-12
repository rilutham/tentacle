from django import forms

class IncreaseHourForm(forms.Form):
    CHOICES = [('pos', 'Add'), ('neg', 'Sub')]
    choice_field = forms.ChoiceField(widget=forms.RadioSelect(), choices=CHOICES, initial='pos')
    num = forms.CharField(max_length=4)
    #note = forms.CharField(max_length=140)

