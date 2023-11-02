from django import forms

class DieCreationForm(forms.Form):
    Estilo=forms.CharField(max_length=60)
    Caras=forms.IntegerField()
    Numeros=forms.CharField(max_length=40)

class BagCreationForm(forms.Form):
    Material=forms.CharField(max_length=60)
    Capacidad=forms.IntegerField()
    Color=forms.CharField(max_length=40)

class TrayCreationForm(forms.Form):
    Material=forms.CharField(max_length=60)
    Tamaño=forms.IntegerField()
    Color=forms.CharField(max_length=40)