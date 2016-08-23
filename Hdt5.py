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
insMax = 3

def source(env, NEW_CLIENT, INTERVALO, RAM, CPU,WAITING ):
    """Source generates customers randomly"""
    for i in range(NEW_CLIENT):
        instrucciones = random.randint(1,10)
        memoria = random.randint(1,10)
        c = proceso(env, 'proceso%03d' % i, memoria, RAM, CPU, WAITING, instrucciones)
        env.process(c)
        t = random.expovariate(1.0 / intervalo)
        yield env.timeout(t)
        
def cliente (env, nombre, memoria, RAM, CPU, WAITING, instrucciones):
    llego = env.now
    print('%7.4f %s: NEW. Esperando memoria. Entrada' % (llego, nombre)

    with RAM.get(memoria) as req:
        yield req 

        espero = env.now - llego
        print('%7.4f %s: Espero por memoria %6.3f' % (env.now, nombre, espero))

        while instrucciones > 0:
            with CPU.request() as reqCPU:
                yield reqCPU
                print('%7.4f %s: RUNNING. Instrucciones %6.3f' % (env.now,nombre,espero))
                yield env.timeout(1)
                if instrucciones > insMax:
                    instrucciones = instrucciones - insMax
                else:
                    instrucciones = 0
                if instrucciones > 0:
                        siguiente = random.choice(["ready","waiting"])
                        if siguiente == "waiting":
                            with WAITING.request() as reqWAITING:
                                yield reqWAITING
                                print ('%7.4f %s: WAITING' % (env.now,nombre))
                                yield env.timeout(1)
                        print ('%7.4f %s: READY' % (env.now,nombre))
    tiempoProceso = env.now-llego
    global tiempoproc
    tiempoproc = tiempoproc + tiempoProceso
    print ('%7.4f %s: TERMINATED. Tiempo de ejecucion %s' % (env.now,nombre,tiempoProceso))
    with RAM.put(memoria) as reqDevolverRAM:
        yield reqDevolverRAM
        print ('%7.4f %s: regresando RAM %s' % (env.now,nombre,memoria))

random.seed(RANDOM_SEED)
env = simpy.Environment()

CPU = simpy.Resource(env, capacity=1)
RAM= simpy.Container(env,init=100,capacity=100)
WAITING = simpy.Resource(env,capacity=1)
env.process(source(env, NEW_CLIENTE,INTERVALO,RAM, CPU,WAITING ))
tiempoproc = 0
env.run()# Setup and start the simulation

print('TIEMPO PROMEDIO: %6.3f' % (tiempoproc/NEW_CLIENTE))
print('DESVIACION STANDARD PROMEDIO: %6.3f' % ())

                    
