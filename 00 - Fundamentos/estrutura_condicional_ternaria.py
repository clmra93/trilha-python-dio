saldo = 2000
saque = 500

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")

credito_especial = 450

if saque <= saldo : status = "Sucesso"
elif saque <= (saldo + credito_especial) : status = "Saque efetuado! Você entrou no cheque especial"
else : status = "Falha"

print("----")
print(f"{status} ao realizar o saque!")