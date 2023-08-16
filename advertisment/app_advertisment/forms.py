from django import forms


class AdvertisementForm(forms.Form):
    title = forms.CharField( max_length=64)
    description = forms.CharField(widget= forms.Textarea)
    price = forms.DecimalField()
    auction = forms.BooleanField(required=False)
    image = forms.ImageField(required= False)
