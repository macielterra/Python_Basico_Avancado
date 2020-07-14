#'w' sobrescreve o que ja esta no arquivo caso ele nao seja novo
#arquivo  = open('teste.txt','w')

def escrever_arquivo(nome_arquivo,texto):
    #diretorio = caminho   
    #open(diretorio,'w')
    arquivo  = open(nome_arquivo,'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo,texto):
    arquivo = open(nome_arquivo,'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo,'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo,'r')
    aluno_nota = arquivo.read()
    #print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')#quebra pelo enter
    #print(aluno_nota)
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        #print(aluno)
        #print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        #print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})#lista de dicionarios
    return lista_media

def copia_arquivo(nome_arquivo):
    import shutil
    shutil.copy(nome_arquivo,'/home/tamara-louzada/Documentos/')

def move_arquivo(nome_arquivo):
    import shutil
    caminho = '/home/tamara-louzada/Documentos/teste'
    shutil.move(nome_arquivo,caminho)
   


if __name__ == "__main__":
    #copia_arquivo('notas.txt')
    move_arquivo('notas.txt')
    #medias = media_notas('notas.txt')
    #print(medias)
    #escrever_arquivo('Primeira linha. \n')
    #aluno = 'Jose, 8, 10, 5,9\n'
    #atualizar_arquivo('notas.txt',aluno)
    #ler_arquivo('teste.txt')