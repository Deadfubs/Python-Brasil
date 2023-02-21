from validate_docbr import CPF, CNPJ


class Documento:

    @staticmethod
    def cria_documento(documento, tipo_documento: str):

        tipo_documento = tipo_documento.lower()
        tipo_documento = tipo_documento.strip()

        if tipo_documento == 'cpf':
            return DocCpf(documento)
        elif tipo_documento == 'cnpj':
            return DocCnpj(documento)
        else:
            raise ValueError('Tipo de documento inválido!!')


class DocCpf:

    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError('CPF inválido !!')

    def __str__(self):
        return self.format()

    @staticmethod
    def valida(documento):
        validador = CPF()
        return validador.validate(documento)

    def format(self):
        mascara = CPF()
        return mascara.mask(self.cpf)


class DocCnpj:

    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError('CNPJ inválido !!')

    def __str__(self):
        return self.format()

    @staticmethod
    def valida(documento):
        validador = CNPJ()
        return validador.validate(documento)

    def format(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)
