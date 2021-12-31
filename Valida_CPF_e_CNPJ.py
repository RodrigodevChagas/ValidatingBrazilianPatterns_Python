from validate_docbr import CPF, CNPJ

class Documento:

    #region - Factory que cria um método estático para retornar a classe CPF ou CPNJ
    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return Cpf(documento)
        elif len(documento) == 14:
            return Cnpj(documento)
        else:
            return ValueError ("Numero de digitos não é compátivel com CPF ou CNPJ.")
    #endregion

class Cpf:
    #region -  Construtor que recebe o numero do CPF como parâmetro e valida
    def __init__ (self, documento):
        if self.valida_cpf(documento):
            self._documento = documento
        else:
            raise ValueError("CPF invalido")

    #endregion

    #region - Encapsulamento com getter
    @property
    def documento(self):
        return self._documento

    # endregion

    #region -  Chamando o método len
    def __len__(self):
        return len(self.documento)

    # endregion

    # region - Validador do CPF
    def valida_cpf(self, documento):
        cpf = CPF()
        return cpf.validate(documento)

    # endregion

    # region -  Cria a máscara com a formatação do CPF no padrão BR.
    def __str__(self):
        cpf = CPF()
        cpf_format = cpf.mask(self.documento)
        return f'{cpf_format}'
    # endregion

class Cnpj:
    # region - Construtor que recebe o numero do CNPJ como parâmetro e valida
    def __init__ (self, documento):
        if self.valida_cnpj(documento):
            self._documento = str(documento)
        else:
            raise ValueError("CNPJ invalido")
    # endregion

    #region - Encapsulamento com getter
    @property
    def documento(self):
        return self._documento
    # endregion

    #region - Chamando o método len
    def __len__(self):
        return len(self.documento)
    # endregion

    # region - Validador do CNPJ
    def valida_cnpj(self, documento):
        cnpj = CNPJ()
        return cnpj.validate(documento)
    # endregion

    # region -  Cria a máscara com a formatação do CPF no padrão BR.
    def __str__(self):
        cnpj = CNPJ()
        cnpj_format = cnpj.mask(self.documento)
        return f'{cnpj_format}'
    # endregion
