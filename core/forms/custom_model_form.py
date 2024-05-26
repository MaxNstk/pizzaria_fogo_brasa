from django.forms import ModelForm


class CustomModelForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def set_fields_to_filter(self):
        return []
