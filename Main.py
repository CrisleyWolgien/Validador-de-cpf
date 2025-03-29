from logging.config import stopListening

cpf = input("coloque o cpf")
separador = ''
cpf_split = cpf.split('-')

print(cpf_split)

cpf_concatenado = separador.join(cpf_split).strip()
tamanho_cpf = len(cpf_concatenado)
print(tamanho_cpf)


if tamanho_cpf != 11 or not cpf_concatenado.isdigit():
    print("CPF errado")
    exit()
else:
    print("CPF válido")


cpf_em_lista = list(cpf_concatenado)
print(cpf_em_lista)
i = 0
n1 = 0
n2 = 10
n3 = 0
for valor in cpf_em_lista:
    i += 1
    if i == 10:
        i = 0
        break
    # print(int(valor), n2 , n1)
    n1 = int(valor) * n2 + n1
    n2 -=1



valor_n1_cpf = 0
calculo_n1_cpf = 11 -(n1 % 11)
if calculo_n1_cpf > 9:
  valor_n1_cpf = 0
else:
    valor_n1_cpf = calculo_n1_cpf
print(valor_n1_cpf)

y = 11
for valor2 in cpf_em_lista:
    i += 1
    if i == 11:
        n3 = valor_n1_cpf * y + n3
        break
    n3 = int(valor2) * y + n3
    # print(int(valor2) , y , n3)
    y -= 1



calculo_n2_cpf = 11 -(n2 % 11)
valor_n2_cpf = 0

if calculo_n2_cpf > 9:
  valor_n2_cpf = 0
else:
    valor_n2_cpf = calculo_n2_cpf
print(valor_n2_cpf)

print (f'valores do cpf {valor_n1_cpf} {valor_n2_cpf}')