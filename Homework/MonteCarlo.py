import numpy as np
import matplotlib.pyplot as plt

# Simulación Monte Carlo para una inversión de retiro.
# Se realizan 100 simulaciones de una inversión de $10,000
# durante 10 años utilizando rendimientos aleatorios.

capital_inicial = 10000

# Almacenará el valor final de cada simulación
capitales_finales = []

plt.figure(figsize=(11, 5))

# range(100) genera números del 0 al 99
# El ciclo for repetirá las instrucciones internas 100 veces
for simulacion in range(100):

    # Genera 10 rendimientos aleatorios entre -5% y +15%
    rendimientos = np.random.uniform(-0.05, 0.15, 10)

    # np.cumprod() permite aplicar crecimiento compuesto
    # acumulando los rendimientos año tras año
    capitales = capital_inicial * np.cumprod(1 + rendimientos)

    # Agrega el capital inicial como año 0
    trayectoria = np.insert(capitales, 0, capital_inicial)

    # Guarda el capital al final de los 10 años
    capitales_finales.append(trayectoria[-1])

    plt.plot(trayectoria, alpha=0.8)

plt.title("Simulación Monte Carlo para una Inversión de Retiro")
plt.xlabel("Años")
plt.ylabel("Capital ($)")
plt.grid(True, linestyle="-.", alpha=1.0)

plt.show()

# Obtiene percentiles de los capitales finales
p10 = np.percentile(capitales_finales, 10)
p50 = np.percentile(capitales_finales, 50)
p90 = np.percentile(capitales_finales, 90)

# Imprime texto en pantalla mediante una f-string.
# :,.2f indica:
# ,  -> separador de miles
# .2 -> mostrar 2 decimales
# f  -> formato de número decimal
print(f"Percentil 10 (Escenario Pesimista): ${p10:,.2f}")
print(f"Percentil 50 (Mediana): ${p50:,.2f}")
print(f"Percentil 90 (Escenario Optimista): ${p90:,.2f}")
