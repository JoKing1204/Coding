from django import forms


class times(forms.Form):
    n = forms.IntegerField()
    term = forms.CharField(required=True)


class sumtin(forms.Form):
    X = forms.IntegerField(required=True)
    Y = forms.IntegerField(required=True)
    Z = forms.IntegerField(required=True)


class xyz(forms.Form):
    term = forms.CharField(required=True)


class cen(forms.Form):
    X = forms.IntegerField(required=True)
    Y = forms.IntegerField(required=True)
    Z = forms.IntegerField(required=True)
