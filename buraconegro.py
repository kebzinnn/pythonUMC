# SIMULADOR DE BURACO NEGRO EM PYTHON PURO

# 1. Constantes Físicas (Valores simplificados para a simulação)
G = 6.674e-11  # Constante gravitacional (m^3 kg^-1 s^-2)
M = 2.0e30     # Massa do buraco negro (Aprox. a massa do nosso Sol)
C = 3.0e8      # Velocidade da luz (m/s)

# 2. Cálculo do Horizonte de Eventos (Raio de Schwarzschild)
Rs = (2 * G * M) / (C ** 2)

# 3. Condições Iniciais do Objeto (Estrela ou planeta)
x = Rs * 5     # Começa a uma distância de 5 vezes o horizonte de eventos
y = 0.0
vx = 0.0       # Velocidade inicial no eixo X
vy = 1.6e5     # Velocidade inicial no eixo Y (Velocidade tangencial)

# 4. Parâmetros da Simulação
dt = 0.01      # Tamanho do passo de tempo em segundos
passos = 1500  # Quantidade de iterações do tempo

print(f"Massa do Buraco Negro: {M} kg")
print(f"Raio do Horizonte de Eventos (Rs): {Rs:.2f} metros")
print("-" * 50)
print("Iniciando simulação da órbita...\n")

# 5. Loop de Simulação
for i in range(passos):
    # Calcula a distância geométrica do objeto ao centro (0,0)
    # Equivalente a math.sqrt(x^2 + y^2)
    distancia = (x**2 + y**2) ** 0.5
    
    # Verifica se o objeto cruzou o horizonte de eventos
    if distancia <= Rs:
        print(f"\n[!] PASSO {i}: O objeto cruzou o Horizonte de Eventos a {distancia:.2f}m do centro.")
        print("    O objeto foi absorvido pelo Buraco Negro!")
        break
        
    # Calcula a aceleração gravitacional (a = G*M / d^2)
    # Decompondo a força nos eixos X e Y usando semelhança de triângulos
    # Isso evita o uso de trigonometria (seno/cosseno) do módulo math
    ax = -G * M * x / (distancia ** 3)
    ay = -G * M * y / (distancia ** 3)
    
    # Atualiza a velocidade (Velocidade = Velocidade Anterior + Aceleração * Tempo)
    vx += ax * dt
    vy += ay * dt
    
    # Atualiza a posição (Posição = Posição Anterior + Velocidade * Tempo)
    x += vx * dt
    y += vy * dt
    
    # Imprime o status da órbita a cada 250 passos para não poluir a tela
    if i % 250 == 0:
        print(f"Passo {i:04d} | Pos(x:{x:10.2f}, y:{y:10.2f}) | Distância: {distancia:10.2f}m")

# Executa caso o loop termine sem o "break" (O objeto não caiu)
else:
    print(f"\nSimulação concluída. O objeto sobreviveu à órbita! Distância final: {distancia:.2f}m")