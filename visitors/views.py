from django.contrib import messages
from django.shortcuts import (
    render, redirect, get_object_or_404
)

from visitors.models import Visitor
from visitors.forms import VisitorsForm

def register_visitor(request):
    form = VisitorsForm()
    
    if request.method == 'POST':                    ## Verificamos de o método da requisição é POST
        form = VisitorsForm(request.POST)           ## Caso seja, utilizaremos os campos do nosso modelo como body da requisição
        if form.is_valid():                         ## Conferimos se os campos estão preenchidos e válidos
            
            visitor = form.save(commit=False)       ## Criamos uma variável que recebe o método save, usando o argumento de commit=False, que salva o corpo da requisição, mas que não envia pro servidor ainda.
            
            visitor.concierge_responsible = request.user.concierge              # Passamos as informações do porteiro logado na sessão para serem utilizadas como concierge responsável pelo cadastro.
            visitor.save()                                                      ## Só depois disso salvamos de fato para enviar para o servidor.
            
            messages.success(                                   ## Mensagem de sucesso caso a requisição dê certo.
                request,
                "Visitor has been succesful registred"
            )
            
            return redirect("index")
            
    context =  {
        "page_name":"Register Visitor",
        "form": form
    }
    return render(request, "registrar_visitante.html", context)



def visitor_info(request, id):
    find_visitor = get_object_or_404(
        Visitor,
        id=id
    )
    
    context = {
        "page_name":"Visitor's Info",
        "visitor_response":find_visitor
    }
    
    return render(request, "informacoes_visitante.html", context)
