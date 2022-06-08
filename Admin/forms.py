from django import forms
from .models import server


class server(forms.ModelForm):
    class Meta:
        model = serverForm
        fields = [
            'name',
            'server_type',
            'processor_numb',
            'memory_capacity',
            'storage_capacity',
        ]