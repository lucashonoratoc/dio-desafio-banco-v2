def filtrar_usuario(cpf, usuarios):
  for usuario in usuarios:
    if usuario['cpf'] == cpf:
      return usuario
    else:
      None

def criar_usuario(usuarios):
  cpf = input("Digite seu CPF (apenas números): ")
  usuario = filtrar_usuario(cpf, usuarios)

  if usuario:
    print("Usuário já cadastrado")
    return

  nome = input("Nome completo: ")
  data_nascimento = input("Data de nascimento (dd-mm-aaaa): ")
  endereco = input("Endereço (logradouro, nro - bairro - cidade/sigla estado): ")

  usuarios.append({"nome": nome, "cpf": cpf,"data_nascimento": data_nascimento, "endereco": endereco})
  print("Usuário cadastrado com sucesso.")


def criar_conta(agencia, numero_conta, usuarios):
  cpf = input("Digite seu CPF (apenas números): ")
  usuario = filtrar_usuario(cpf, usuarios)

  if usuario:
    print("Conta criada com sucesso.")
    return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

  print("Usuário não encontrado.")
#Argumentos posicionais
def deposito(saldo, valor, extrato, /):
  if valor < 0:
    print("Operação inválida")
  else:
    print("Depósito realizado com sucesso!")
    saldo += valor
    extrato += f"Depósito:\tR$ {valor:.2f}\n"
  return saldo, extrato

#Argumentos por nome (keyword)
def saque(*, valor, saldo, limite, numero_saques, limite_saques, extrato):
  if valor > saldo:
    print("Não é possível sacar o dinheiro pois não tem saldo suficiente")
  elif valor > limite:
    print("Você excedeu o limite de saque diário")
  elif numero_saques >= LIMITE_SAQUES:
    print("Você excedeu o número de saques")
  elif valor > 0:
    print("Saque realizado com sucesso!")
    saldo -= valor
    extrato += f"Saque:\t\tR$ {valor:.2f}\n"
    numero_saques += 1
  else:
    print("Operação inválida")
  return saldo, extrato

#Argumentos posicionais e por nome
def mostrar_extrato(saldo, /, *, extrato):
  print("\nEXTRATO\n")
  if not extrato:
    print("Não foram efetuadas movimentações.")
  else:
    print(extrato)
    print(f"Saldo:\t\tR$ {saldo:.2f}\n")