# MISSAO 1

def verificar_aprovacao (nota):
    if  nota >= 6 :
        return ("Aprovado")
    else:
        return ("Reprovado")

nota = float(input("Insira a nota do aluno: "))
resultado = verificar_aprovacao (nota)
print(f"O Aluno está {resultado}.")

# MISSAO 2
 
def elegibilidade_votacao (idade):
    if idade >= 16:
        return ("pode votar")
    else:
        return ("não pode votar")

idade = int(input("Insira a sua idade: "))
resultado_voto = elegibilidade_votacao(idade)
print(f"O aluno {resultado_voto}.")

# MISSAO 3

def classificacao (nota_prova):
    if 90 <= nota_prova <= 100 :
        return "Parabéns, você tirou A!"
    elif 80 <= nota_prova < 90 :
         return "Muito bem, você tirou B."
    elif 70 <= nota_prova < 80 :
         return "Bom trabalho, você tirou C."
    elif 60 <= nota_prova < 70 :
         return "Fique atento, você tirou D."
    else:
         return "Estude um pouco mais, você tirou F."
    
nota_prova = float(input("Insira a sua nota: "))
resultado_prova = classificacao(nota_prova)
print(f"{resultado_prova}")

# MISSAO 4 

A = int(input("Insira um número inteiro:"))
B = int(input("Insira outro número inteiro:"))

soma = A+B
print(f"A soma é", soma)

# MISSAO 5

def verificar_senha (senha) :
    if senha == "Python123" :
        return "Acesso concedido"
    else:
        return "Acesso negado"
    
senha = input("Insira a senha:")
print(f"{verificar_senha(senha)}")

# MISSAO 6

contador = 1
while contador <= 10:
    print(contador)
    contador += 1

# MISSAO 7

numeros = [8, 3, 10, 1, 5]
numeros.sort()
print("Números organizados:", numeros)

# MISSAO 8

alunos = ("Ana", "Bruno", "Carla", "Daniel", "Eduardo")
print("Primeiro aluno:", alunos[0])
print("Último aluno:", alunos[-1])

# MISSAO 9

def dobrar (numero) :
    return numero * 2

numero = int(input("Insira um número inteiro:"))
print("O dobro é", dobrar(numero))

# MISSAO 10 

def contar_letras(nome):
    return f"O nome {nome} tem {len(nome)} letras."

nome = input("Digite um nome: ")
print(contar_letras(nome))