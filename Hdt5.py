#------------------------------------------------------------------
#Universidad del Valle de Guatemala
#Hoja de traba 5. Simulacion, colas
#Autores: Gladys de la Roca 15755
#         Jackeline Hidalgo 15776
#         Luis Sierra 131074
#Fecha: 22 de agosto de 2016
#------------------------------------------------------------------

import random
import simpy

RANDOM_SEED = 42
NEW_CLIENT = 5
INTERVALO = 10
minP = 1
maxP = 3

def source(env, NEW_CLIENT, intervalo, RAM, CPU,WAITING ):
    """Source generates customers randomly"""
    for i in range(NEW_CLIENT):
        instruc = random.randint(1,10)
        memoria = random.randint(1,10)
        c = proceso(env, 'proceso%03d' % i, memoria, RAM, CPU, WAITING, instruc)
        env.process(c)
        t = random.expovariate(1.0 / intervalo)
        yield env.timeout(t)
