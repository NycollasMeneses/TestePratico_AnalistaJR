import asyncio
import time

async def chamada_rede(id, tempo):
    print(f"Iniciando chamada {id}...")
    await asyncio.sleep(tempo)  
    print(f"Chamada {id} concluída em {tempo} segundos")
    return tempo

async def executar_chamadas():
    inicio = time.time()  

    tarefas = [
        chamada_rede(1, 2),
        chamada_rede(2, 3),
        chamada_rede(3, 1)
    ]
    await asyncio.gather(*tarefas)  

    fim = time.time()  
    tempo_total = fim - inicio
    print(f"\nTempo total de execução: {tempo_total:.2f} segundos")
    return tempo_total

asyncio.run(executar_chamadas())
