from django import forms

class IncreaseHourForm(forms.Form):
    num = forms.CharField(max_length=4, label=False)

class DecreaseHourForm(forms.Form):
	num = forms.CharField(max_length=4, label=False)
