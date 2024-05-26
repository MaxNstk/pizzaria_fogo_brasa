from crispy_forms.helper import FormHelper

class FormHandlerMixin():

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = self.build_layout()

    def build_layout(self):
        return None
