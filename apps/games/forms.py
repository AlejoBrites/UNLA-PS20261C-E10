from django import forms


class GameSearchForm(forms.Form):
    q = forms.CharField(required=False, label='Buscar juego', max_length=200)
