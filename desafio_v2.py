def filtrar_user(cpf, user):
  for user in user:
    if user['cpf'] == cpf:
      return user
    else:
      None

def criar_usuario(user):
  cpf = input("Digite seu CPF [SOMENTE NÚMEROS]: ")
  user = filtrar_user(cpf, user)

  if user:
    print("Usuário já cadastrado")
    return

  nome = input("Nome completo: ")
  data_nascimento = input("Data de nascimento: ")
  endereco = input("Endereço: ")

  user.append({"nome": nome, "cpf": cpf,"data_nascimento": data_nascimento, "endereco": endereco})
  print("Usuário cadastrado!")


def criar_conta(agencia, numero_conta, user):
  cpf = input("Digite seu CPF [SOMENTE NÚMEROS]: ")
  user = filtrar_user(cpf, user)

  if user:
    print("Conta cadastrada!")
    return {"agencia": agencia, "numero_conta": numero_conta, "usuario": user}

  print("Usuário não foi encontrado.")


def deposito(saldo, valor, extrato, /):
  if valor < 0:
    print("Operação inválida.")
  else:
    print("Depósito realizado com sucesso!")
    saldo += valor
    extrato += f"Depósito:\tR$ {valor:.2f}\n"
  return saldo, extrato


def saque(*, valor, saldo, limite, numero_saques, limite_saques, extrato):
  if valor > saldo:
    print("Saldo insuficiente.")
  elif valor > limite:
    print("Limite diário excedido!")
  elif numero_saques >= LIMITE_SAQUES:
    print("Você excedeu o número de saques")
  elif valor > 0:
    print("Saque realizado com sucesso!")
    saldo -= valor
    extrato += f"Saque:\t\tR$ {valor:.2f}\n"
    numero_saques += 1
  else:
    print("Operação inválida, tente novamente!")
  return saldo, extrato


def mostrar_extrato(saldo, /, *, extrato):
  print("\nEXTRATO\n")
  if not extrato:
    print("Sem movimentações encontradas")
  else:
    print(extrato)
    print(f"Saldo é de: R$ {saldo:.2f}\n")
