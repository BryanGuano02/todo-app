# Transformador de Moneda en Java con Swing

Integrantes:
- **Sebastián Correa**
- **Bryan Guano**

Este proyecto es un conversor de monedas simple que convierte USD a EUR, COP y PEN. Se utilizó Java con Swing para la interfaz gráfica y se aplicaron principios de Clean Code inspirados en [Clean Code JavaScript](https://github.com/andersontr15/clean-code-javascript-es).

## Principios aplicados

| Principio                                | Aplicación                                                        | Archivo                    |
|------------------------------------------|-------------------------------------------------------------------|----------------------------|
| Nombres significativos                   | Clases y variables como `ConversorMoneda`, `txtCantidad`          | Todos                     |
| SRP (Single Responsibility Principle)    | Separación entre UI y lógica de conversión                        | `ConversorMoneda.java`     |
| Evitar strings mágicos                   | Uso de `enum Moneda` en lugar de strings duros                    | `Moneda.java`              |
| Código autoexplicativo                   | Métodos como `realizarConversion()` en lugar de comentarios       | `ConversorSwing.java`      |
| Funciones pequeñas y claras              | Cada método hace solo una cosa (crear panel, convertir, etc.)     | `ConversorSwing.java`      |
| Manejo de errores claro                  | Validación con mensajes específicos para el usuario               | `ConversorSwing.java`      |

## Cómo ejecutar

1. Clona o descarga este proyecto.
2. Asegúrate de tener Java configurado.
3. Ejecuta la clase `ConversorSwing` como aplicación Java.

---


