from django import forms

class FeedbackFilterForm(forms.Form):
    name = forms.CharField(max_length=100, required=False, label='Name')
    email = forms.EmailField(required=False, label='Email')
    message = forms.CharField(widget=forms.Textarea, required=False, label='Message')