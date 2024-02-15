
# ████████╗██╗    ██████╗  ██████╗     ███████╗███████╗██████╗  ██████╗ 
# ╚══██╔══╝██║    ██╔══██╗██╔═══██╗    ╚══███╔╝██╔════╝██╔══██╗██╔═══██╗
#    ██║   ██║    ██║  ██║██║   ██║      ███╔╝ █████╗  ██████╔╝██║   ██║
#    ██║   ██║    ██║  ██║██║   ██║     ███╔╝  ██╔══╝  ██╔══██╗██║   ██║
#    ██║   ██║    ██████╔╝╚██████╔╝    ███████╗███████╗██║  ██║╚██████╔╝
#    ╚═╝   ╚═╝    ╚═════╝  ╚═════╝     ╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ 
# Módulo: Introdução à Linguagem de programação                                                                      

import os # Importa os módulos responsáveis por interagir com o sistema operacional

def criar_pasta_e_arquivos(nome_pasta):
    # Verificar se a pasta já existe
    if not os.path.exists(nome_pasta):
        # Criar a pasta
        os.makedirs(nome_pasta)

        # Criar os arquivos dentro da pasta
        with open(os.path.join(nome_pasta, 'arquivo1.txt'), 'w') as arquivo1:
            arquivo1.write("Conteúdo do arquivo 1")

        with open(os.path.join(nome_pasta, 'arquivo2.txt'), 'w') as arquivo2:
            arquivo2.write("Conteúdo do arquivo 2")

        print(f"Pasta '{nome_pasta}' criada com sucesso e contém os arquivos 'arquivo1.txt' e 'arquivo2.txt'")
    else:
        print(f"A pasta '{nome_pasta}' já existe.")

# Nome da pasta que você quer criar
nome_da_pasta = 'minha_pasta'

# Chamar a função para criar a pasta e os arquivos
criar_pasta_e_arquivos(nome_da_pasta)
