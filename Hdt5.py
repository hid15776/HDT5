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
        
        def cliente (env, nombre, contador, esp):
    llego = env.now
    print('%7.4f %s: Entrada' % (llego, nombre)

    with contador.request() as req:
        paciencia = random.uniform(minP, maxP)
        resultado = yield req | env.timeout(paciencia)

        espero = env.now - llego

        if req in resultado:
            print ('7.4f %s: Espero %6.3f' % (env.now, nombre, espero))


            tib = random.expovariate(1.0 / esp)
            yield env.timeout(tib)
            print('%7.4f %s: Finished' % (env.now, nombre))

        else:
            print('%7.4f %s: RENEGED after %6.3f' % (env.now, nombre, espero))


random.seed(RANDOM_SEED)
env = simpy.Environment()
contador = simpy.Resource(env, capacidad = 1)

CPU = simpy.Resource(env, capacity=1)
RAM= simpy.Container(env,init=100,capacity=100)
WAITING = simpy.Resource(env,capacity=1)
env.process(source(env, NEW_CLIENTE,INTERVALO,RAM, CPU,WAITING ))
tiempop = 0
env.run()# Setup and start the simulation

print('TIEMPO PROMEDIO: %6.3f' % (tiempop/new_process))
print('DESVIACION STANDARD PROMEDIO: %6.3f' % ())

