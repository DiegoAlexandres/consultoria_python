#%%
dados = 2
dados1 = 3
print(dados + dados1)

#%%
salario_atual = 1000
percentual_aumento = 10

valor_aumento = salario_atual * (percentual_aumento / 100)
novo_salario = salario_atual + valor_aumento
novo_salario

#%%
# Trabalhando com medias no python
notas1 = 5
notas2 = 7
notas3 = 3

media = (notas1 + notas2 + notas3) / 3
media

#%%
notas = [5 , 7, 3, 8, 2]
media_nova = sum(notas) / len(notas)
media_nova


#%%
novas_notas = [5 , 7, 3, 8, 2, 8, 1]

for nota in notas:
    if nota >=7:
        print(f"A nota {nota} foi aprovado")
    else:
        print(f"A nota {nota} foi reprovado")

#%%
idade = 12

if idade < 13:
    categoria = "Criança"
elif idade < 18:
    categoria = "Adolescente"
elif idade < 65:
    categoria = "Adulto"
else:
    categoria = "Idoso"
    
print(f"Com {idade} anos, a pessoa esta na categoria {categoria}")


#%%
nota_final = 8.0
frequencia = 0.85

if nota_final >= 7.0 and frequencia >= 0.75:
    status = "Aprovado"
elif nota_final >= 5.0 and frequencia >= 0.75:
    status = "Recuperação"
else:
    status = "Reprovado"
    
print(f"O status do aluno é {status}")
    








