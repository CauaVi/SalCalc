print("--Calculadora de salario bruto por hora V0.02--")

#Coleta de informações
vph = float(input(">> Digite o quanto você recebe por hora: "))
htm = float(input(">> Digite o numero de horas trabalhadas esse mês sem minutos: "))
ms = float(input(">> Agora digite os minutos: "))

#Calculos
vmt = float(ms*0.016666667)
thm = float(vmt+htm)
sbm = float(thm*vph)

#Informando o usuario dos resultados
print(">> Você tem como pagamento bruto o total de R$",sbm)
print(">> Caso existam mais de dois digitos nos centavos, arredonde para cima")

#Coleta de dados sobre os descontos
hf = float(input(">> Agora digite o seu total de minutos de falta: "))

#Calculos de descontos e exibição da informação para o usuario
tf = float(hf*0.016666667)
dtf = float(tf*vph)
print(">> O total de desconto por falta é de R$",dtf)
scd = float(sbm-dtf)
print(">> Total liquido contando apenas horas trabalhadas de R$",scd)
print(">> Considere que existem outros fatores de desconto e de ganho. \n>> O valor apresentado não é condizente ao salario com todos os descontos e adiçoes")


