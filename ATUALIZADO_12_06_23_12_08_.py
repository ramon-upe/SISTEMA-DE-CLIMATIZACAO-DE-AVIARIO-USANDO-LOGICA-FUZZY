import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Antecedentes (entradas)
# Definindo a variável de entrada temperatura com valores entre 0 e 45 graus Celsius
temperatura = ctrl.Antecedent(np.arange(0, 45, 1), 'temperatura')

#____________________________________________________________________________

# Definindo a variável de entrada temperatura_ideal com valores entre 0 e 45 graus Celsius
temperatura_ideal = ctrl.Antecedent(np.arange(0, 45, 1), 'temperatura_ideal')


#_____________________________________________________________________________



# Definindo a variável de entrada umidade com valores entre 0 e 100%
umidade = ctrl.Antecedent(np.arange(0, 101, 1), 'umidade')

# Definindo a variável de entrada idade com valores entre 0 e 21 dias
idade = ctrl.Antecedent(np.arange(0, 22, 1), 'idade')

# Definindo a variável de entrada aquecimento necessário com valores sim ou não
aquecimento_necessario = ctrl.Antecedent(np.arange(0, 2, 1), 'aquecimento_necessario')
aquecimento_necessario.automf(names=['nao', 'sim'])

# Consequente (saída)
# Definindo a variável de saída ventilação com valores entre 0 e 100%
ventilacao = ctrl.Consequent(np.arange(0, 101, 1), 'ventilacao')

# Definindo a variável de saída aquecimento com valores entre 0 e 100%
aquecimento = ctrl.Consequent(np.arange(0, 101, 1), 'aquecimento')

# Nova saída
# Definindo a variável de saída tempo de funcionamento com valores entre 0 e 60 minutos
tempo_funcionamento = ctrl.Consequent(np.arange(0, 61, 1), 'tempo_funcionamento')

# Funções de pertinência para temperatura
# Definindo as funções de pertinência baixa, ideal e alta para a variável de entrada temperatura
temperatura['baixa'] = fuzz.trimf(temperatura.universe, [0, 0, 22])
temperatura['ideal'] = fuzz.trimf(temperatura.universe, [18, 24, 30])
temperatura['alta'] = fuzz.trimf(temperatura.universe, [28, 44, 44])

#________________________________________________________________________________


# Definindo os conjuntos fuzzy para a variável temperatura_ideal
temperatura_ideal['primeira_semana'] = fuzz.trimf(temperatura_ideal.universe, [0, 0, 32])
temperatura_ideal['segunda_semana'] = fuzz.trimf(temperatura_ideal.universe, [0, 32, 29])
temperatura_ideal['terceira_semana'] = fuzz.trimf(temperatura_ideal.universe, [29, 29, 27])
temperatura_ideal['quarta_semana'] = fuzz.trimf(temperatura_ideal.universe, [27, 27, 24])

#________________________________________________________________________________


# Funções de pertinência para umidade
# Definindo as funções de pertinência baixa, ideal e alta para a variável de entrada umidade
umidade['baixa'] = fuzz.trimf(umidade.universe, [0, 0, 50])
umidade['ideal'] = fuzz.trimf(umidade.universe, [30, 50, 70])
umidade['alta'] = fuzz.trimf(umidade.universe, [50, 100, 100])



#*****__________________________________________________________________*****

# Funções de pertinência para idade
idade['jovem'] = fuzz.trimf(idade.universe, [0, 0, 15])
idade['adulto'] = fuzz.trimf(idade.universe, [15, 21, 21])

#*****__________________________________________________________________*****



# Funções de pertinência para aquecimento
aquecimento['baixo'] = fuzz.trimf(aquecimento.universe, [0, 0, 50])
aquecimento['medio'] = fuzz.trimf(aquecimento.universe, [0, 50, 100])
aquecimento['alto'] = fuzz.trimf(aquecimento.universe, [50, 100, 100])


# Funções de pertinência para ventilação
ventilacao['desligado'] = fuzz.trimf(ventilacao.universe, [0, 0, 50])
ventilacao['baixo'] = fuzz.trimf(ventilacao.universe, [0, 50, 100])
ventilacao['alto'] = fuzz.trimf(ventilacao.universe, [50, 100, 100])


# Funções de pertinência para tempo de funcionamento
tempo_funcionamento['curto'] = fuzz.trimf(tempo_funcionamento.universe, [0, 0, 30])
tempo_funcionamento['medio'] = fuzz.trimf(tempo_funcionamento.universe, [0, 30, 60])
tempo_funcionamento['longo'] = fuzz.trimf(tempo_funcionamento.universe, [30, 60, 60])


#______________________________________________________________________________

regra1 = ctrl.Rule(idade['primeira_semana'] & (temperatura < temperatura_ideal['primeira_semana']), aquecimento['alto'])
regra2 = ctrl.Rule(idade['segunda_semana'] & (temperatura < temperatura_ideal['segunda_semana']), aquecimento['medio'])
regra3 = ctrl.Rule(idade['terceira_semana'] & (temperatura < temperatura_ideal['terceira_semana']), aquecimento['baixo'])
regra4 = ctrl.Rule(idade['quarta_semana'] & (temperatura < temperatura_ideal['quarta_semana']), aquecimento['desligado'])

regra5 = ctrl.Rule(idade['primeira_semana'] & (temperatura > temperatura_ideal['primeira_semana']), ventilacao['alta'])
regra6 = ctrl.Rule(idade['segunda_semana'] & (temperatura > temperatura_ideal['segunda_semana']), ventilacao['media'])
regra7 = ctrl.Rule(idade['terceira_semana'] & (temperatura > temperatura_ideal['terceira_semana']), ventilacao['baixa'])
regra8 = ctrl.Rule(idade['quarta_semana'] & (temperatura > temperatura_ideal['quarta_semana']), ventilacao['desligada'])

#_______________________________________________________________________________

# Regras
rule1 = ctrl.Rule(temperatura['baixa'] & umidade['baixa'], ventilacao['desligado'])
rule2 = ctrl.Rule(temperatura['baixa'] & umidade['ideal'], ventilacao['desligado'])
rule3 = ctrl.Rule(temperatura['baixa'] & umidade['alta'], ventilacao['baixo'])
rule4 = ctrl.Rule(temperatura['ideal'] & umidade['baixa'], ventilacao['desligado'])
rule5 = ctrl.Rule(temperatura['ideal'] & umidade['ideal'], ventilacao['desligado'])
rule6 = ctrl.Rule(temperatura['ideal'] & umidade['alta'], ventilacao['baixo'])
rule7 = ctrl.Rule(temperatura['alta'] & umidade['baixa'], ventilacao['alto'])
rule8 = ctrl.Rule(temperatura['alta'] & umidade['ideal'], ventilacao['alto'])
rule9 = ctrl.Rule(temperatura['alta'] & umidade['alta'], ventilacao['alto'])

# Novas regras
rule10 = ctrl.Rule(temperatura['baixa'] & umidade['baixa'], tempo_funcionamento['curto'])
rule11 = ctrl.Rule(temperatura['baixa'] & umidade['ideal'], tempo_funcionamento['curto'])
rule12 = ctrl.Rule(temperatura['baixa'] & umidade['alta'], tempo_funcionamento['medio'])
rule13 = ctrl.Rule(temperatura['ideal'] & umidade['baixa'], tempo_funcionamento['curto'])
rule14 = ctrl.Rule(temperatura['ideal'] & umidade['ideal'], tempo_funcionamento['curto'])
rule15 = ctrl.Rule(temperatura['ideal'] & umidade['alta'], tempo_funcionamento['medio'])
rule16 = ctrl.Rule(temperatura['alta'] & umidade['baixa'], tempo_funcionamento['longo'])
rule17 = ctrl.Rule(temperatura['alta'] & umidade['ideal'], tempo_funcionamento['longo'])
rule18 = ctrl.Rule(temperatura['alta'] & umidade['alta'], tempo_funcionamento['longo'])


rule19 = ctrl.Rule(aquecimento_necessario['sim'], aquecimento['alto'])

rule = ctrl.Rule(idade['jovem'] & temperatura['baixa'], aquecimento['alto'])



# Adicionando novas regras ao sistema de controle
ventilation_ctrl = ctrl.ControlSystem([rule1, rule2, rule3,
                                       rule4, rule5, rule6,
                                       rule7, rule8, rule9,
                                       rule10, rule11, rule12,
                                       rule13, rule14, rule15,
                                       rule16, rule17, rule18])

ventilation = ctrl.ControlSystemSimulation(ventilation_ctrl)



rule1 = ctrl.Rule(idade['jovem'] & temperatura['baixa'], aquecimento['alto'])
rule2 = ctrl.Rule(idade['adulto'] & temperatura['baixa'], aquecimento['medio'])

aquecimento_ctrl = ctrl.ControlSystem([rule1, rule2])
aquecimento = ctrl.ControlSystemSimulation(aquecimento_ctrl)


# Exemplo de entrada de dados
ventilation.input['temperatura'] = 30
ventilation.input['umidade'] = 60

# Computação do resultado
ventilation.compute()

# Saída
print(ventilation.output['ventilacao'])
ventilacao.view(sim=ventilation)

print(f'Tempo de Funcionamento: {ventilation.output["tempo_funcionamento"]}')

# Testando o sistema de controle com diferentes entradas
for temp in [20, 25, 30]:
    for hum in [40, 60, 80]:
        ventilation.input['temperatura'] = temp
        ventilation.input['umidade'] = hum
        ventilation.compute()
        print(f'Temperatura: {temp}Cº, Umidade: {hum}%, Ventilação: {ventilation.output["ventilacao"]}%P, Tempo de Funcionamento: {ventilation.output["tempo_funcionamento"]} min')
