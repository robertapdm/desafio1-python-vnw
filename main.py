"""# MISSAO 1

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
    elif 80 <= nota_prova < 89 :
         return "Muito bem, você tirou B."
    elif 70 <= nota_prova < 79 :
         return "Bom trabalho, você tirou C."
    elif 60 <= nota_prova < 69 :
         return "Fique atento, você tirou D."
    else:
         return "Estude um pouco mais, você tirou F."
    
nota_prova = float(input("Insira a sua nota: "))
resultado_prova = classificacao(nota_prova)
print(f"{resultado_prova}")
"""

# MISSAO 4 

