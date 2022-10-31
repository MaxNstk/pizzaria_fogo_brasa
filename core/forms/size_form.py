from django.forms import ModelForm
from core.models.size import Size

class SizeForm(ModelForm):
    class Meta:
        model=Size
        fields=['short_name', 'description','available']