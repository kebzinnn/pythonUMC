# Uma empresa concederá um aumento de salário aos seus funcionários (variável de acordo com o cargo), conforme a tabela abaixo. 
# Faça um algoritmo que leia o salário e o cargo de um funcionário e calcule o novo salário.

# Se o cargo do funcionário não estiver na tabela, ele deverá receber 40% de aumento.

# Mostre o salário antigo, o novo salário e a diferença.

# Tabela de cargos e percentuais:

# 101 – Gerente – 10%
# 102 – Engenheiro – 20%
# 103 – Técnico – 30%

sal = int(input("Digite o salário: "))

print("Tabela de aumento: ")
print("101 - Gerente - 10%")
print("102 - Engenheiro - 20%")
print("103 - Técnico - 30%")
cargo = int(input("Digite o caro"))