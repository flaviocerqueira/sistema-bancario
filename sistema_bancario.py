

def deposito(valor, saldo_da_conta, extrato_da_conta):
    saldo_da_conta += valor
    extrato_da_conta += f"\nDepósito no valor de R${valor}"
    print('\nDepósito concluído com sucesso')
    return saldo_da_conta, extrato_da_conta


def saque(valor, saldo_da_conta, extrato_da_conta, saques):
    saldo_da_conta -= valor
    saques += 1
    extrato_da_conta += f"\nSaque no valor de R${valor}"
    print('\nSaque concluído com sucesso')
    return saldo_da_conta, extrato_da_conta, saques


def extrato(saldo_da_conta, extrato_da_conta):
    print(f'{extrato_da_conta}')
    print(f'Saldo atualizado: {saldo_da_conta}')


LIMITE_SAQUE_DIARIO = 2
LIMITE_VALOR_DO_SAQUE = 500.00

saldo_da_conta = 0.00
extrato_da_conta = " "
saques = 0

while True:
    print(
        """
        ------ SISTEMA BANCÁRIO -----
        1. DEPÓSITO
        2. SAQUE
        3. EXTRATO
        4. SAIR
        """
    )
    opcao = int(input('Digite a opção correspondente: '))

    if opcao == 1:
        valor = float(input('Informe o valor do depósito: '))
        if valor >= 0 :
            saldo_da_conta, extrato_da_conta = deposito(valor, saldo_da_conta, extrato_da_conta)
        else:
            print('\nValor inválido. Reinicie a operação.')
    elif opcao == 2:
        valor = float(input('Informe o valor do saque: '))
        if valor > LIMITE_VALOR_DO_SAQUE:
            print('\nO valor requistado excede o limite diário. Tente novamente.')
        elif saques > LIMITE_SAQUE_DIARIO:
            print('\nLimite de saques diários excedido')
        elif valor > saldo_da_conta:
            print('\nSaldo insuficiente para realizar a operação')
        else:
            saldo_da_conta, extrato_da_conta, saques = saque(valor, saldo_da_conta, extrato_da_conta, saques)
    elif opcao == 3:
        extrato(saldo_da_conta, extrato_da_conta)
    elif opcao == 4:
        print('\nFinalizando o sistema...')
        break
