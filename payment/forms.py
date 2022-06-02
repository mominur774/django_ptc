from django import forms
from payment.models import Subscribed


class SubscribedForm(forms.ModelForm):
    class Meta:
        model = Subscribed
        fields = ('trxid', )

        labels = {
            'trxid': 'TrxID'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'placeholder': 'Enter TrxId here...',
            })
