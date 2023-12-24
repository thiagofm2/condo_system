from django.db import models
from django.contrib.auth.models import (            ## Importamos as classes necessárias do Django para auxílio na criação de um modelo de autenticação
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin
)

class UserManager(BaseUserManager):                 ## Criamos a classe UserManager que será usada para sobrescrever o padrão do Django
    def create_user(self, email, password=None):    ## Criamos um método de criação de usuário, onde passamos o self, email e o password como parâmetro, sendo que o password nesse caso não é obrigatório.
        user = self.model(                         
            email=self.normalize_email(email)       ## Criamos um user e passamos o e-mail dele como normalized, ou seja, com caracteres normalizados para deixar padronizado em nosso banco de dados.
        )
        
        user.is_active = True                       ## User é ativo
        user.is_staff = False                       ## User padrão não é desenvolvedor
        user.is_superuser = False                   ## User padrão não é super usuário (admin)
        
        if password:                                ## Caso seja passado uma senha, nós usamos o método set_password para definir ela como senha.
            user.set_password(password)
        
        user.save()                                 ## Usamos o método save para salvar este usuário padrão e retornamos ele no final.
        
        return user


    def create_superuser(self, email, password):    ## Método usado para criação de um super usuário (admin)
        user = self.create_user(                    ## Usamos o método anterior para criação do nosso usuário, passando as informações necessárias.
            email=self.normalize_email(email),
            password=password
        )
        
        user.is_active = True                       ## Superusuário é ativo, dev, e superuser.
        user.is_staff = True
        user.is_superuser = True
        
        user.set_password(password)                 ## Um superusuário é obrigatório que tenha senha, então usamos o método para setar ela
        
        user.save()                                 ## Salvamos o superusuário e retornamos ele.
        
        return user 


class User(AbstractBaseUser, PermissionsMixin):     ## Criamos a classe User, que será a abstração da nossa tabela no Banco de dados
    email = models.EmailField(                      ## Criamos o atributo E-mail, e utilizamos o campo "EmailField" que vem junto da biblioteca models padrão do Django
        verbose_name="User E-mail",                 ## O verbose_name consiste no nome de label que será exibido, serve como identificador.
        max_length=200,                             ## Max-length consiste na quantidade de caracteres que será permitido o E-mail ter
        unique=True                                 ## Validação para afirmar que o E-mail deve ser único, não podendo haver dois iguais no banco.
    )
    
    is_active = models.BooleanField(                ## Criação de um campo boolean onde verificamos se o usuário é ativo ou não.
        verbose_name="User is active",
        default=True                                ## O padrão de criação será como True
    )
    
    is_staff = models.BooleanField(                  ## Criação de um campo boolean onde verificamos se o usuário é desenvolvedor ou não, para podermos dar permissões especiais.
        verbose_name="User is a dev",                ## O padrão na hora da criação será False
        default=False
    )
    
    is_superuser = models.BooleanField(              ## Criação de um campo boolean onde verificamos se o usuário é Superusuário (admin) ou não
        verbose_name="User is a superuser",
        default=False                                ## O padrão na hora da criação será False.
    )
    
    USERNAME_FIELD = "email"                         ## Informamos ao Django que o campo USERNAME, originalmente usado para a autenticação padrão do Framework receberá o valor do atributo E-mail.
    
    objects = UserManager()                          ## Sobrescrevemos o modelo padrão do Django com o manager que criamos acima.
    
    class Meta:                                      ## Classe padrão do Django onde passamos algumas informações extras (Metadados)
        verbose_name="User"                          ## Passamos um nome que ajudará a identificar, consequentemente este nome será o que irá aparecer no nosso Admin.
        verbose_name_plural="Users"                  ## Literalmente o plural, ou seja, o nome do grupo que armazenará todos os modelos criados através do User. 
        db_table="user"                              ## O nome que será exibido no nosso banco de dados, para que possamos organizar.
        
    def __str__(self):                               ## Método obrigatório, onde retorna o E-mail do usuário como string após a autenticação.
        return self.email
