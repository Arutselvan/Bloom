from django import forms
from .models import MyUploads

class UploadForm(forms.ModelForm):
    class Meta:
        model = MyUploads
        fields = ['title', 'file_path']
