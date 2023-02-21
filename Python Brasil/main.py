from cpf_cnpj import Documento
from telefone_br import TelefoneBr
from data_br import DataBr
from acesso_cep import BuscaEndereco

cpf_um = Documento.cria_documento('12872491678', 'CPF')
cnpj_um = Documento.cria_documento('45753859000100', 'CNpJ')
telefone_um = TelefoneBr('31995375619')
cadastro_um = DataBr()
endereco_um = BuscaEndereco(39800151)


print(cpf_um)
print(cnpj_um)
print(telefone_um)
print(cadastro_um)
print(cadastro_um.tempo_cadastro())
print(endereco_um.acessa_via_cep())
