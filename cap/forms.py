from django.forms import ModelForm
from .models import CapData


class UploadFileForm(ModelForm):
    class Meta:
        model = CapData
        fields = ['title', 'file_path']
