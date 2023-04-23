from django import forms
from .models import Komentar

class KomentarForm(forms.ModelForm):
    class Meta:
        model = Komentar
        fields = ['nama', 'isi_komentar']