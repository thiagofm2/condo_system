from django.db import models

class Visitor(models.Model):
    complete_name = models.CharField(
        verbose_name="Visitor's name",  
        max_length=200
    )
    
    document = models.CharField(
        verbose_name="Visitor's document (CPF)",
        max_length=11
    )
    
    birthdate = models.DateField(
        verbose_name="Visitor's Birthdate",
        auto_now=False,
        auto_now_add=False
    )
    
    home_number = models.PositiveSmallIntegerField(                                 ## Este tipo de campo armazena um número pequeno positivo.
        verbose_name="Number of the house",
    )
    
    license_plate = models.CharField(
        verbose_name="Vehicle license plate",
        max_length=8,
        blank=True,                                                                 ## Este atributo permite que essa informação vá vazia no cadastro.
        null=True                                                                   ## Este atributo permite que essa informação vá nula no cadastro.  
    )
    
    arrival_time = models.DateTimeField(                                            ## Este tipo de campo armazena tanto a data quanto as horas de um evento.
        verbose_name="Arrival time on lobby",
        auto_now_add=True                                                           ## Queremos que o horário seja exatamente o mesmo que o visitante chegou a portaria
    )
    
    departure_time = models.DateTimeField(
        verbose_name="Departure time of condo",
        auto_now=False,                                                             ## O horário de saída do visitante não precisa ser exatamente o atual, mas sim um horário aleatório
        blank=True,             
        null=True
    )
    
    authorization_time = models.DateTimeField(
        verbose_name="The time when visitor is authorized to entry",
        auto_now=False,
        blank=True,
        null=True
    )
    
    responsible_resident = models.CharField(
        verbose_name="Name of the resident responsible of authorize the visitor",
        max_length=200,
        blank=True
    )
    
    concierge_responsible = models.ForeignKey(                                      ## Este tipo de campo permite referênciar outra tabela do banco como se fosse uma Foreign Key
        "concierge.Concierge",                                                      ## Precisamos específicar o modelo que queremos usar de Foreign Key
        verbose_name="Consierge responsible for register",
        on_delete=models.PROTECT
    )
    
    ## Criação dos métodos que retornam uma mensagem personalizada caso não haja dados que preencham atributos
    
    def get_departure_time(self):                               ## Os métodos são basicamente funções que fazem referência ao conteúdo da própria classe, passando o "self" como argumento
        if(self.departure_time):                                ## Como padrão de organização, os métodos que validam atributos começam com "get_", fazemos a verificação do campo e retornamos uma mensagem caso esteja vazio
            return self.departure_time
        else:
            return "Departure time not registred."
    
    def get_authorization_time(self):
        if(self.authorization_time):
            return self.authorization_time
        else:
            return "Visitor waiting authorization."
        
    def get_responsible_resident(self):
        if(self.responsible_resident):
            return self.responsible_resident
        else:
            return "Visitor waiting authorization"
        
    def get_license_plate(self):
        if(self.license_plate):
            return self.license_plate
        else:
            return "Vistior was not using a car."
    
    class Meta:
        verbose_name="Visitor"
        verbose_name_plural="Visitors"
        db_table = "visitor"
        
    def __str__(self):
        return self.complete_name
