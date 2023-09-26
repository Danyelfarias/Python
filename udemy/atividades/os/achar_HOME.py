import os

# Obtém o diretório de trabalho do usuário atual
diretorio_usuario = os.getenv('USERPROFILE')

print(f'O diretório de trabalho do usuário é: {diretorio_usuario}')




# .......... paramentro do getenv:......................

# 'USERPROFILE': O caminho para o diretório de perfil do usuário atual.
# 'TEMP' ou 'TMP': O caminho para o diretório temporário do sistema.
# 'PATH': O caminho de pesquisa para executáveis no sistema.
# 'USERNAME': O nome de usuário atual.
# 'COMPUTERNAME': O nome do computador.
# 'OS': O nome do sistema operacional.