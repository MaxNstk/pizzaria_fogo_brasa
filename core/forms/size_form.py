

from core.models.size import Size


class SizeForm():
    class Meta:
        model=Size
        fields=['short_name', 'description','available']