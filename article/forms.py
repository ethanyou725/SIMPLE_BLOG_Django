from django import forms


class SearchForm(forms.Form):
    q=forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}),
        max_length=50,
        required=False,label="")

