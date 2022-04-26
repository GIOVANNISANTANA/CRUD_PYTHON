#Giovanni Almeida Santana

from time import sleep


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def linha(tam = 42):
    return "-" * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))       #centralizando um texto
    print(linha())


def menu(lista):
    cabeçalho("MENU PRINCIPAL")
    c = 1
    for item in lista:
        print(f"\033[33m{c}\033[m - \033[33m{item}\033[m ")
        c += 1
    print(linha())
    opc = leiaInt("Sua Opção: ")
    return opc


def menu_(lista):
    cabeçalho("RELATÓRIOS")
    c = 1
    for item in lista:
        print(f"\033[33m{c}\033[m - \033[33m{item}\033[m ")
        c += 1
    print(linha())
    opc = leiaInt("Sua Opção: ")
    return opc


def relatorios():
    while True:
        resposta = menu_(["Listar Todos", "Listar Maior Média", "Listar Reprovados", "Listar Aprovados", "Voltar para Menu Anterior"])
        if resposta == 1:
            lerArquivo(arq)
        elif resposta == 2:
            cabeçalho("opção 2")
        elif resposta == 3:
            cabeçalho("Opção 3")
        elif resposta == 4:
            cabeçalho("Opção 4")
        elif resposta == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            print("ERRO! Digite uma opção válida")  

def arqExiste(nome):
    try:
        a = open(nome, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, "wt+")
        a.close()
    except:
        print("Houve um ERRO na criação do arquivo!")
    else:
        print(f"Arquivo {nome} criado com sucesso!")


def lerArquivo(nome):
    try: 
        a = open(nome, "rt")
    except:
        print("Erro ao ler o arquivo")
    else:
        cabeçalho("ALUNOS CADASTRADOS")
        for linha in a:
            dado = linha.split(";")
            dado[1] = dado[1].replace("\n", "")
            print(a.read())
    finally:
        a.close()


def cadastrar(arq, nome, curso, nota1, nota2, nota3, faltas):
    try:
        a = open(arq, "at")
    except:
        print("Houve um ERRO na abertura do arquivo!")
    else:
        try:
            a.write(f"{nome};{curso};{nota1};{nota2};{nota3};{faltas}\n")    
        except:
            print("Houve um ERRO na hora de escrever os dados!")
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            cabeçalho(f"Novo registro de {nome} adicionado.")
            sleep(1.5)
            a.close()


def excluir(nome):
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        with open('banco_de_dados.txt', 'r') as fr:
            lines = fr.readlines()
    
            with open('banco_de_dados.txt', 'w') as fw:
                for line in lines:
                    if line.find(nome) == -1:
                        fw.write(line)
        print("Excluindo...")
        sleep(1)
    except:
        print("Oops! someting error")
    
    print("Exclusão feita com sucesso!")
    sleep(1)


def maiorMed():
    import csv
    lista = []
    try:
        a = open(arq, "at")
    except:
        print("Houve um ERRO na abertura do arquivo!")
    else:
        try:
            a.write(f"{nome};{curso};{nota1};{nota2};{nota3};{faltas}\n")    
        except:
            print("Houve um ERRO na hora de escrever os dados!")
        else:
            print(f"Novo registro de {nome} adicionado.")
            sleep(1)
            a.close()



arq = "banco_de_dados.txt"          #define o nome do arquivo

if not arqExiste(arq):
    criarArquivo(arq)

import os
while True:
    resposta = menu(["Inserir Aluno", "Excluir Aluno", "Relatórios", "Sair"])
    if resposta == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Novo Aluno")
        nome = str(input("Nome: "))
        curso = str(input("Curso: "))
        nota1 = leiaInt("1ª nota: ")
        nota2 = leiaInt("2ª nota: ")
        nota3 = leiaInt("3ª nota: ")
        faltas = leiaInt("Quantidade de faltas: ")
        cadastrar(arq, nome, curso, nota1, nota2, nota3, faltas)
        os.system('cls' if os.name == 'nt' else 'clear')
    elif resposta == 2:
        nome = str(input("Nome de quem deseja excluir: "))
        excluir(nome)
        os.system('cls' if os.name == 'nt' else 'clear')
    elif resposta == 3:
        cabeçalho("Opção 3")
        os.system('cls' if os.name == 'nt' else 'clear')
        relatorios()
    elif resposta == 4:
        os.system('cls' if os.name == 'nt' else 'clear')
        cabeçalho("Saindo do sistema")
        break
    else:
        print("ERRO! Digite uma opção válida")

