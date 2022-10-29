from crispy_forms.helper import FormHelper

class FormHandlerMixin():

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.layout = self.get_layout()

    def get_layout(self):
        return None
