# INCLUINDO INPUTS PARA BOAS VINDAS
print("Bem-vindo ao aplicativo de pedidos de Açaí e Cupuaçu do Leandro Geroto Soares!")
print("---------------------Cardápio---------------------")
print("------| Tamanho | Cupuaçu (CP) | Açaí (AC) |------")
print("------|    P    |   R$ 10,00   |  R$ 12,00 |------")
print("------|    M    |   R$ 15,00   |  R$ 17,00 |------")
print("------|    G    |   R$ 19,00   |  R$ 21,00 |------")
print("--------------------------------------------------")

# CÓDIGO INICIAL PARA DEFINIR AS VARIÁVEIS INICIAIS
totalPedido = 0
pedidoAtual = ""

# CÓDIGO DO LOOP
while True:
    sabor = input("Entre com o sabor desejado (CP para Cupuaçu, AC para Açaí): ").upper()

    if sabor not in ['CP', 'AC']:
        print("Sabor inválido. Tente novamente.")
        continue

    tamanho = input("Entre com o tamanho desejado (P/M/G): ").upper()

# CÓDIGO PARA VERIFICAR O TAMANHO DIGITADO
    if tamanho not in ['P', 'M', 'G']:
        print("Tamanho inválido. Tente novamente.")
        continue

# CÓDIGO PARA VERIFICAR O PEDIDO FEITO
    if sabor == 'CP':
        tipoProduto = "Cupuaçu"
    elif sabor == 'AC':
        tipoProduto = "Açaí"
    pedidoAtual = f"Você pediu {tipo_produto} no tamanho: {tamanho}"

# CÓDIGO PARA CALCULAR O VALOR DO PEDIDO
    if sabor == 'CP':
        if tamanho == 'P':
            valorPedido = 10.00
        elif tamanho == 'M':
            valorPedido = 15.00
        elif tamanho == 'G':
            valorPedido = 19.00
    elif sabor == 'AC':
        if tamanho == 'P':
            valorPedido = 12.00
        elif tamanho == 'M':
            valorPedido = 17.00
        elif tamanho == 'G':
            valorPedido = 21.00

# CÓDIGO PARA EXIBIR O VALOR DO PEDIDO E FINALIZAR
    totalPedido += valorPedido
    print(f"{pedidoAtual} R${valorPedido:.2f}")
    continuar = input("Deseja pedir mais alguma coisa? (S/N): ").upper()
    if continuar != 'S':
        break

# CÓDIGO PARA EXIBIR A CONCLUSÃO DO PEDIDO
print(f"O valor total a ser pago: R${totalPedido:.2f}")
