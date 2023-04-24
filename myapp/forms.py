from django import forms
from .models import Komentar

class KomentarForm(forms.ModelForm):
    class Meta:
        model = Komentar
        fields = ['nama', 'isi_komentar', 'parent']
        widgets = {
            'nama': forms.TextInput(attrs={'class': 'form-control'}),
            'isi_komentar': forms.Textarea(attrs={'class': 'form-control'}),
            'parent': forms.HiddenInput(),
        }