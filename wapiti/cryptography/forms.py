from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms


class CaesarCipherForm(forms.Form):
    key_field = forms.IntegerField(label='Enter a key')
    text_field = forms.CharField(label='Enter a text to cipher', max_length=100)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            'key_field',
            'text_field',
            Submit('submit', 'Submit', css_class='btn-success')
        )


class CaesarDecipherForm(forms.Form):
    text_field = forms.CharField(label='Enter a text to decipher', max_length=100)
    key_field = forms.IntegerField(label='Enter a key')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            'text_field',
            'key_field',
            Submit('submit', 'Submit', css_class='btn-success')
        )


class OneTimePadForm(forms.Form):
    mask_field = forms.CharField(label='Enter a mask')
    text_field = forms.CharField(label='Enter a text to cipher', max_length=100)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            'mask_field',
            'text_field',
            Submit('submit', 'Submit', css_class='btn-success')
        )


class OneTimePadDecipherForm(forms.Form):
    text_field = forms.CharField(label='Enter a text to cipher', max_length=100)
    mask_field = forms.CharField(label='Enter a mask', max_length=100)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            'text_field',
            'mask_field',
            Submit('submit', 'Submit', css_class='btn-success')
        )


class RsaForm(forms.Form):
    text_field = forms.CharField(label='Enter a text to cipher', max_length=100)
