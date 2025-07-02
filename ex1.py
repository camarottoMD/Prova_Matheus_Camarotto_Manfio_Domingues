#criar tres listas
#funcao recebe tres listas e retorna 1 dict
#chaves são os nomes dos dep. e os values são tuplas com os nomes dos funcionarios do setor
#nao pode ter 2 ou menos funcionarios
#funcao com nome em ordem alfabetica, independente do setor

funci_Admnistrativo = ['emanuel', 'rodrigo']
funci_Operacional = ['emanuel', 'rodrigo', 'thiago']
funci_Tecnico = ['emanuel', 'rodrigo', 'thiago', 'andre']
dicionario = {}

def tornaDict(adm, ope, tec): 

    dicionario['Adminstrativo']=(
        adm
    )

    dicionario['Operacional']=(
        ope
    )

    dicionario['Técnico']=(
        tec
        )
    """    
    for participantes in dicionario['Adminstrativo']:
        print(participantes)"""

    return dicionario

tornaDict(funci_Admnistrativo, funci_Operacional, funci_Tecnico)

dicionario2 = list(filter(lambda x: x if len(x) > 2 else 0, dicionario['Adminstrativo']))

print(dicionario2)



def nomes():
    pass#nomes = dicionario[]