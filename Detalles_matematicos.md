# **Formulación matemática**

## **Regresiones lineales**

### **Mínimos cuadrados ordinarios (OLS)**

Para un conjunto de datos con $\eta$ observaciones, tenemos una variable independiente $y$, que es dependiente de $x$. Queremos encontrar una relación lineal de la forma:

$$
\begin{equation}
    y_i = \beta_0 + \beta_1 x  _i + \varepsilon_i
\end{equation}
$$

donde:

* $y_i$ es la variable dependiente (observado).
* $x_i$ la variable independiente.
* $\beta_0$ la intersección.
* $\beta_1$ la pendiente.
* $\varepsilon_i$ es el residuo o término de error.

### Residuos

En la práctica los puntos no siempre caen perfectamente sobre una línea recta, siempre habrá una diferencia entre el valor real $(y_i)$ y el valor que se predice $\hat{y_i}$. A esta diferencia se le conoce como residuo ($\varepsilon_i$):

$$
\begin{equation}
    \varepsilon_i = y_i - \hat{y_i}
\end{equation}
$$

De (1) encontramos la igualdad $\hat{y} = \beta_0 + \beta_1 x_1$ que sustituimos en (2)
$$
\begin{equation}
    \varepsilon = y_i - (\beta_0 + \beta_1 x_i)
\end{equation}
$$

El objetivo de OLS es minimizar los residuos.

![Regresión lineal](Imagenes/Regresión_OLS.png)
### Función de costo (Suma de errores cuadráticos)

Este es un método de optimización. Definimos a la función de costo como $S$. Esta función depende de los parámetros desconocidos $\beta_0$ y $\beta_1$

$$
\begin{equation}
    S(\beta_0,\beta_1) = \sum_{i=1}^n (y_i - \hat{y}_i)^2
\end{equation}
$$

Sustituyendo la 3 en 4:

$$
\begin{equation}
    S(\beta_0,\beta_1) = \sum_{i=1}^n (y_i - (\beta_0 + \beta_1 x_i))^2
\end{equation}
$$

### Optimización
Para encontrar los valores óptimos de $\beta_0$ y $\beta_1$ para la función de costo, usamos sus derivadas parciales respecto a cada coeficiente e igualamos a cero.

1. Derivada respecto a $\beta_0$:

$$
\begin{equation}
\frac{\partial S}{\partial \beta_0} = \frac{\partial \left( \displaystyle\sum_{i=1}^n \left(y_i - \left(\beta_0 + \beta_1 x_i\right)\right)^2\right)}{\partial \beta_0}
\end{equation}
$$

Resolviendo la derivada tenemos:
$$
\begin{equation}
\frac{\partial S}{\partial \beta_0} =-2 \sum_{i=1}^{n}(y_i -\beta_0 - \beta_1 x_i)
\end{equation}
$$

Igualamos a cero y simplificamos

$$
    -2 \sum_{i=1}^{n}(y_i -\beta_0 - \beta_1 x_i) = 0
$$

$$
    \sum_{i=1}^{n}y_i -n\beta_0 - \beta_1 \sum_{i=1}^n x_i = 0
$$

***Recordatorio***: $\displaystyle\sum _{i=1}^{n} \beta_0 = n\beta_0$