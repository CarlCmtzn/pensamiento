import numpy as np
import matplotlib.pyplot as plt

# Simulación Monte Carlo para una Inversión de Retiro
# Capital Inicial: $10,000
# Horizonte: 10 años
# Simulaciones: 100 Escenarios Posibles

capital_inicial = 10000

plt.figure(figsize=(11, 5))

# Ejecuta 100 Simulaciones Independientes
for simulacion in range(100):

    # Genera 10 Rendimientos Aleatorios
    # Entre -5% y +15% (uno por Año)
    rendimientos = np.random.uniform(-0.05, 0.15, 10)

    # Calcula el Crecimiento Compuesto del Capital
    capitales = capital_inicial * np.cumprod(1 + rendimientos)

    # Agrega el Capital Inicial al Inicio de la Trayectoria
    trayectoria = np.insert(capitales, 0, capital_inicial)

    # Dibuja la Trayectoria Obtenida
    plt.plot(trayectoria, alpha=0.8)

# Configuración del Gráfico
plt.title("Simulación Monte Carlo para una Inversión de Retiro")
plt.xlabel("Años")
plt.ylabel("Capital ($)")
plt.grid(True, linestyle="-.", alpha=1.0)

# Muestra todas las Simulaciones
plt.show()
