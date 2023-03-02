import json

with open('faturamento.json') as f:
    faturamento_diario = json.load(f)

# Remove os dias sem faturamento
faturamento_diario = [valor for valor in faturamento_diario if valor > 0]

# Cálculo das informações solicitadas
menor_valor = min(faturamento_diario)
maior_valor = max(faturamento_diario)
media_mensal = sum(faturamento_diario) / len(faturamento_diario)
dias_acima_media = len([valor for valor in faturamento_diario if valor > media_mensal])

# Impressão dos resultados
print("Menor valor de faturamento diário:", menor_valor)
print("Maior valor de faturamento diário:", maior_valor)
print("Número de dias com faturamento acima da média mensal:", dias_acima_media)
