import pandas as pd
from rich import print

class Cpf:
    def __init__(self, numero):
        self.numero = numero

    def validar_cpf(self):
        cpf = ''.join(filter(str.isdigit, str(self.numero))) # Tira os pontos e hífens do CPF, caso houver

        if len(cpf) != 11:
            return False

        if cpf == cpf[0] * 11:
            return False
        
        # Calculando os números verificadores
        # Primeiro dígito
        soma = 0
        for i in range(9):
            soma += int(cpf[i]) * (10 - i)

        dig1 = (soma * 10) % 11
        if dig1 == 10:
            dig1 = 0

        # Segundo dígito
        soma = 0
        for i in range(10):
            soma += int(cpf[i]) * (11 - i)

        dig2 = (soma * 10) % 11
        if dig2 == 10:
            dig2 = 0

        return cpf[-2:] == f"{dig1}{dig2}"


df = pd.read_csv('cpfs.csv')
df['status'] = ""

for i, cpf in enumerate(df['cpf']):
    obj = Cpf(cpf)

    if obj.validar_cpf():
        print(f"[green]CPF Válido - {cpf}[/green]")
        df.loc[i, "status"] = "CPF Válido"
    else:
        print(f"[red]CPF Inválido - {cpf}[/red]")
        df.loc[i, "status"] = "CPF Inválido"

# Cria novo arquivo com o resultado, pra não substituir o antigo
df.to_csv("resultado.csv", index=False)