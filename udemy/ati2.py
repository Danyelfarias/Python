import os
diretorio_atual=os.getcwd()
print(diretorio_atual)



print(os.path.basename(diretorio_atual))
print(os.path.dirname(diretorio_atual))


completo=os.path.join(os.path.basename(diretorio_atual),os.path.dirname(diretorio_atual))

print(completo)