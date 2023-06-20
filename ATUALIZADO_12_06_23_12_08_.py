import random

def controle_temperatura(temperatura=None, umidade=None, idade=None):
    if temperatura is None or umidade is None or idade is None:
        temperatura, umidade, idade = simular_clima()

    # Simulação dos dias restantes até completar o período de 45 dias
    for dia in range(idade + 1, 46):
        # Temperatura ideal baseada na idade das aves em dias
        temp_ideal = max(35 - 0.33 * (dia - 1), 20)

        # Diferença de temperatura
        dif_temp = temperatura - temp_ideal

        # Aquecimento
        if dif_temp < -0.2:
            forno_ligado = True
            tempo_forno = abs(dif_temp) / 0.33 * 60
        else:
            forno_ligado = False
            tempo_forno = 0

        # Ventilação e nebulização
        if dif_temp > 0.2:
            ventiladores_ligados = min(int((dif_temp / 0.2 + 1) // 2 * 2), 14)
            tempo_ventiladores = dif_temp / 0.33 * 60

            if temperatura > 29 and dia > 21:
                nebulizacao_ligada = True
                tempo_nebulizacao = dif_temp / 0.33 * 60
            else:
                nebulizacao_ligada = False
                tempo_nebulizacao = 0
        else:
            ventiladores_ligados = 0
            tempo_ventiladores = 0
            nebulizacao_ligada = False
            tempo_nebulizacao = 0

        # Nomeação dos ventiladores e indicação de quais foram acionados
        sequencia_ventiladores = ['VT0', 'VT1', 'VT6', 'VT7', 'VT10', 'VT11', 'VT4', 'VT5', 'VT8', 'VT9', 'VT2', 'VT3', 'VT12', 'VT13']
        ventiladores_acionados = sequencia_ventiladores[:ventiladores_ligados]

        # Resultados para cada dia da simulação
        print(f'\nDia {dia}:')
        print(f'Temperatura atual: {temperatura} °C')
        print(f'Umidade atual: {umidade} %')
        print(f'Idade das aves: {dia} dias')
        print(f'Temperatura ideal: {temp_ideal:.2f} °C')
        print(f'Diferença de temperatura: {dif_temp:.2f} °C')
        print(f'Forno ligado: {forno_ligado}')
        print(f'Tempo de funcionamento do forno: {tempo_forno:.2f} minutos')
        print(f'Ventiladores ligados: {ventiladores_ligados}')
        print(f'Ventiladores acionados: {ventiladores_acionados}')
        print(f'Tempo de funcionamento dos ventiladores: {tempo_ventiladores:.2f} minutos')
        print(f'Nebulização ligada: {nebulizacao_ligada}')
        print(f'Tempo de funcionamento da nebulização: {tempo_nebulizacao:.2f} minutos')


def simular_clima():
    temperatura = random.uniform(15, 35)
    umidade = random.uniform(40, 80)
    idade = random.randint(1, 45)
    return temperatura, umidade, idade


# Exemplo de uso da função
controle_temperatura()
