# ==============================================================
# PROJETO: Classificação de Consumo de Água
# CURSO: Técnico em Desenvolvimento de Sistemas
# ALUNO: (coloque seu nome aqui)
# DESCRIÇÃO: Classifica o perfil de consumo de água dos imóveis
#            e emite alertas educativos aos moradores.
# ==============================================================

# Exibe o título do programa
print("----------------------------------------")
print("  CLASSIFICAÇÃO DE CONSUMO DE ÁGUA")
print("----------------------------------------")

# Solicita o tipo de imóvel ao usuário
tipo = input("Digite o tipo de imóvel (comercial / casa / apartamento): ")

# Solicita o consumo mensal em metros cúbicos
consumo = float(input("Digite o consumo mensal de água (m³): "))

# Verifica o tipo de imóvel e o consumo para emitir o alerta correto
if tipo == "comercial":
    # Imóveis comerciais recebem tarifa específica
    print("Tarifa comercial aplicada – consulte o plano corporativo.")

elif tipo == "apartamento" and consumo < 10:
    # Apartamento com consumo abaixo de 10 m³ -> econômico
    print("Consumo econômico – excelente controle de água!")

elif (tipo == "apartamento" or tipo == "casa") and consumo <= 25:
    # Apartamento ou casa com consumo até 25 m³ -> moderado
    print("Consumo moderado – dentro do padrão residencial.")

else:
    # Qualquer outro caso -> excessivo
    print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")