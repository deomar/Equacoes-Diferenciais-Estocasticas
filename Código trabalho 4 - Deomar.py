#!/usr/bin/env python
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

##Definição das variáveis
dt = 0.005 #Incremento de tempo
kb = 1.38/100000000000000000000000 #Constante de Boltzmann
dw = np.sqrt(dt)*np.random.normal(0, 1, 10000) #Processo de Wiener
V = [] #Lista que guarda as tensões
V0 = 0 #Tensão no tempo 0
V.append(V0) 
t = 0 #Tempo inicial
t_l = [] #Lista para guardar os tempos
t_l.append(t)
R = 1000000 #Resistência de 100 Mohm
C = 10/1000000 #Capacitância de 1uF
T = 300 #Temperatura de 300K
beta = np.sqrt(2*kb*T/(R*C*C)) #Constante beta para o circuito RC
A = 0.000001 #Amplitude da tensão da fonte

##Loop que calcula a solução numérica com ruído gaussiano
for i in np.arange(0,10000,1): #Loop que integra a tensão com ruído
    x = 0
    x = V[i] - (V[i] - A)*dt/(R*C) + beta*dw[i]
    V.append(x)
    t += dt
    t_l.append(t)
plt.plot(t_l, V) #Plot do resultado
plt.xlabel('Tempo (s)')
plt.ylabel('Tensão (V)')
import matplotlib.ticker as mticker #Coloca o eixo y em notação científica
f = mticker.ScalarFormatter(useOffset=False, useMathText=True)
g = lambda x,pos : "${}$".format(f._formatSciNotation('%1.10e' % x))
plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(g))
plt.tight_layout()
#plt.savefig('Numerico_com_tensao_1_micro_filtro.png', dpi=200)


##Loop que plota a solução analítica
z = [] #Define-se as variáveis novamente para o plot da solução analítica
t_l = []
A = 1
t = 0
f = 10
for i in np.arange(0,1000,1): #Loop que plota a função analítica
    y = 0
    y = A*(1 - np.exp(-t/(R*C)))
    z.append(y)
    t += dt
    t_l.append(t)
plt.plot(t_l,z)
plt.xlabel('Tempo (s)')
plt.ylabel('Tensão (V)')
#plt.savefig('Analitica_com_tensao.png', dpi=150)