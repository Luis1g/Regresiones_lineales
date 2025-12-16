import numpy as np
import matplotlib.pyplot as plt

# 1. Generamos datos de ejemplo (Simulación)
# Supongamos que X son "Horas de estudio" y Y es "Calificación"
np.random.seed(42) # Para reproducibilidad
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1) # y = 4 + 3x + ruido

# Aplanamos X e y para facilitar los cálculos (de matriz a vector 1D)
x_vals = X.flatten()
y_vals = y.flatten()

# ---------------------------------------------------------
# Regresión lineal OLS
# ---------------------------------------------------------

# Paso A: Calcular los promedios (x̄ y ȳ)
x_mean = np.mean(x_vals)
y_mean = np.mean(y_vals)

# Paso B: Calcular el numerador y el denominador de Beta 1
# Fórmula: β1 = Σ((x - x̄)(y - ȳ)) / Σ((x - x̄)²)

numerator = 0
denominator = 0

for i in range(len(x_vals)):
    numerator += (x_vals[i] - x_mean) * (y_vals[i] - y_mean)
    denominator += (x_vals[i] - x_mean) ** 2

# Paso C: Calcular los coeficientes (β1 y β0)
beta_1 = numerator / denominator
beta_0 = y_mean - (beta_1 * x_mean)

# ---------------------------------------------------------
# Resultados y Predicción
# ---------------------------------------------------------

print(f"La Intersección (beta_0) calculada es: {beta_0:.4f}")
print(f"La Pendiente (beta_1) calculada es: {beta_1:.4f}")
print(f"\nLa ecuación de la recta es: y = {beta_0:.2f} + {beta_1:.2f}x")

# Hacemos la predicción para dibujar la línea
y_pred = beta_0 + beta_1 * x_vals

# ---------------------------------------------------------
# Visualización
# ---------------------------------------------------------
plt.scatter(x_vals, y_vals, color='blue', alpha=0.5, label='Datos Reales')
plt.plot(x_vals, y_pred, color='red', linewidth=2, label='Línea de Regresión (OLS)')
plt.xlabel('Variable X (independiente)')
plt.ylabel('Variable Y (dependiente)')
plt.legend()
plt.title('Regresión Lineal OLS')
plt.show()