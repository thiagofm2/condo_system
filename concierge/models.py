from django.db import models


class Concierge(models.Model):
    
    user = models.OneToOneField(                        ## Usamos o campo OneToOneField, que faz uma referência de 1 para 1 com outra tabela, ou seja, para existir um porteiro, precisa existir um usuário
        "users.User",                                   ## Fazemos a referência o modelo que desejamos fazer a relação, no caso ela está presente em users.User
        verbose_name="User",
        on_delete=models.PROTECT                        ## Método para proteger as informações de serem deletadas.
    )
    
    complete_name = models.CharField(                   ## O CharField é um tipo de campo que recebe um texto pequeno.
        verbose_name = "Name and lastname",
        max_length=200
    )
    
    document = models.CharField(
        verbose_name = "Concierge document (CPF)",
        max_length=11
    )    
    
    phone = models.CharField(
        verbose_name = "Concierge phone",
        max_length=11
    )

    birthdate = models.DateField(                       ## O DateField é um tipo de campo que representa datas no padrão Python
        verbose_name="Concierge birthdate",
        auto_now=False,                                 ## Passamos como False esse atributo, pois ele não será atualizado toda vez que alterarmos as informações de um porteiro
        auto_now_add=False                              ## Passamos como False esse atributo, pois ele salva no banco a data atual da criação, mas queremos salvar a data de nascimento. 
    )
    
    class Meta:
        verbose_name="Concierge"
        verbose_name_plural="Concierges"
        db_table="concierge"
        
    def __str__(self):
        return self.complete_name
    