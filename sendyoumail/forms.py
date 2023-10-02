from django import forms

from sendyoumail.models import Client, mailingsettings


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ClientForm(StyleFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Client
        exclude = ('owner',)
        # fields = '__all__'




class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = mailingsettings
        fields = '__all__'
