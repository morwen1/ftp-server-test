from django import forms

class Uploadform(forms.Form):
	filename = forms.CharField(max_length = 100)
	docfile = forms.FileField( label= 'selecciona un archivo ')

