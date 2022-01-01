import re

class Telefone:
#Valida numeros de celular e telefone fixo atráves de uma factory
    @staticmethod
    def celular_ou_fixo(self, numero):
        if len(numero) == 11 or len(numero) == 13 :
            return Celular(numero)
        elif len(numero) == 10 or len(numero) == 12:
            return Fixo(numero)
        else:
            raise ValueError ("Numero invalido.")


class Celular:

# region - Definindo a construtora e validando o numero de telefone celular.
    def __init__(self, numero):
        if self.valida_telefone(numero):
            self._numero = numero
        else:
            raise ValueError ('Numero incorreto!!')
#endregion
#region - Função que faz a validação.
    def valida_telefone(self, numero):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{5})([0-9]{4})"
        tel_padrao = re.search(padrao, numero)
        if tel_padrao:
            return True
        else:
            return False
#endregion
#region - Encapsulamento do objeto.
    @property
    def numero(self):
        return self._numero
#endregion
#region -  criando a máscara para formatar o número.
    def mask_telefone(self):

        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{5})([0-9]{4})"
        tel_padrao = re.search(padrao, self.numero)

        if tel_padrao.group(1) == None:
            mascara =  (f'({tel_padrao.group(2)}){tel_padrao.group(3)}-{tel_padrao.group(4)}')

        else:
            mascara =  (f'+{tel_padrao.group(1)}({tel_padrao.group(2)}){tel_padrao.group(3)}-{tel_padrao.group(4)}')

        return mascara
#endregion

# - chamando o método str para fazer o print do telefone já formatado e validado.
    def __str__(self):
        return self.mask_telefone()

class Fixo:

# region - Definindo a construtora e validando o numero de telefone celular.
    def __init__(self, numero):
            if self.valida_telefone(numero):
                self._numero = numero
            else:
                raise ValueError ('Numero incorreto!!')
#endregion
#region - Função que faz a validação.
    def valida_telefone(self, numero):
            padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4})([0-9]{4})"
            tel_padrao = re.search(padrao, numero)
            if tel_padrao:
                return True
            else:
                return False
#endregion
#region - Encapsulamento do objeto.
    @property
    def numero(self):
        return self._numero
#endregion
#region -  criando a máscara para formatar o número.
    def mask_telefone(self):

        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4})([0-9]{4})"
        tel_padrao = re.search(padrao, self.numero)

        if tel_padrao.group(1) == None:
                mascara =  (f'({tel_padrao.group(2)}){tel_padrao.group(3)}-{tel_padrao.group(4)}')

        else:
           mascara =  (f'+{tel_padrao.group(1)}({tel_padrao.group(2)}){tel_padrao.group(3)}-{tel_padrao.group(4)}')

        return mascara
#endregion
#- chamando o método str para fazer o print do telefone já formatado e validado.
    def __str__(self):
        return self.mask_telefone()





