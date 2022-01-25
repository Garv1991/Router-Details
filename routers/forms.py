from django import forms
from .models import router_details


class router_details_form(forms.ModelForm):
    class Meta:
        model = router_details
        fields = [
            'Sapid',
            'Hostname',
            'Loopback',
            'Mac_address'
        ]

        widgets = {
            'Sapid' : forms.TextInput(attrs={'class': 'form-control'}),
            'Hostname' : forms.TextInput(attrs={'class': 'form-control'}),
            'Loopback' : forms.TextInput(attrs={'class' : 'form-control'}),
            'Mac_address' : forms.TextInput(attrs={'class' : 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(router_details_form, self).__init__(*args, **kwargs)