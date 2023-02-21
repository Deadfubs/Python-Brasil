import re


class TelefoneBr:

    def __init__(self, telefone):
        if self.valida_telefone(telefone):
            self.numero = telefone
        else:
            raise ValueError('Número incorreto!!')

    def __str__(self):
        return self.format_numero()

    @staticmethod
    def valida_telefone(telefone):
        padrao = "(\\d{2,3})?(\\d{2})(\\d{4,5})(\\d{4})"
        resposta = re.search(padrao, telefone)
        if resposta:
            return True
        else:
            return False

    def format_numero(self):
        padrao = "(\\d{2,3})?(\\d{2})(\\d{4,5})(\\d{4})"
        resposta = re.search(padrao, self.numero)
        if resposta.group(1) is None:
            return f'+55({resposta.group(2)}){resposta.group(3)}-{resposta.group(4)}'
        else:
            return f'+{resposta.group(1)}({resposta.group(2)}){resposta.group(3)}-{resposta.group(4)}'
