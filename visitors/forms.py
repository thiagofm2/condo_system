from django import forms
from visitors.models import Visitor

class VisitorsForm(forms.ModelForm):        ## Criamos uma classe que será subclasse do forms.ModelForm padrão do Django.
    class Meta:
        model = Visitor                     ## Indicamos o modelo que deve se basear para gerar os campos do formulário
        fields = [                          ## Iremos indicar os campos que queremos que apareça através de uma lista contendo os nomes dos atributos
            "complete_name",
            "document",
            "birthdate",
            "home_number",
            "license_plate"
        ]
        error_messages = {
            "complete_name": {
                "required": "That field is required."
            },
            "document": {
                "required": "That field is required."
            },
            "birthdate": {
                "required": "That field is required.",
                "invalid": "The format of birthdate is wrong. The format expected is dd/mm/yyyy"
            },
            "home_number": {
                "required": "That field is required."
            }
        }
