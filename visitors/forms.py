from django import forms
from visitors.models import Visitor

class VisitorsForm(forms.ModelForm):        ## Criamos uma classe que será subclasse do forms.ModelForm padrão do Django.
    class Meta:
        model = Visitor                     ## Indicamos o modelo que deve se basear para gerar os campos do formulário
        fields = "__all__"                  ## Usaremos todos os campos de nosso modelo
