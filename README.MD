# Pruebas Automatizadas

Este repositorio contiene pruebas automatizadas para varios flujos de trabajo en los sitio web:


- utilizamos El comando **python -m pytest tests** para ejecutar todos los test
- si necesitas un reporte pdf como este **file:///CPycharmProjects/Pom-Automation/report.html)**
- usando este comando lo puedes hacer **python -m pytest tests --html=report.html**
### Lista de Enlaces

- (https://the-internet.herokuapp.com/login)
- (https://the-internet.herokuapp.com/inputs)
- (https://the-internet.herokuapp.com/hovers)
- (https://the-internet.herokuapp.com/dropdown)

"the-internet.herokuapp.com". Las pruebas se realizan utilizando Selenium y Python.

## Flujo de Trabajo: Login

### Caso de Prueba 1: Inicio de Sesión Válido

**Precondición:** Abrir la página de inicio de sesión.
**Acción:** Ingresar un nombre de usuario válido y una contraseña válida.
**Resultado Esperado:** El usuario debería iniciar sesión correctamente.

### Caso de Prueba 2: Inicio de Sesión Inválido

**Precondición:** Abrir la página de inicio de sesión.
**Acción:** Ingresar un nombre de usuario válido y una contraseña inválida.
**Resultado Esperado:** Debería mostrarse un mensaje de error de inicio de sesión.

## Flujo de Trabajo: Inputs

### Caso de Prueba 3: Ingresar Número Válido

**Precondición:** Abrir la página de inputs.
**Acción:** Ingresar un número válido en el campo de entrada.
**Resultado Esperado:** El número ingresado debería reflejarse en el campo.

### Caso de Prueba 4: Ingresar Texto Inválido

**Precondición:** Abrir la página de inputs.
**Acción:** Ingresar texto en lugar de un número en el campo de entrada.
**Resultado Esperado:** El campo debería mantenerse en blanco o mostrar un mensaje de error.

#Pruebas en Diferentes Tamaños de Pantalla


**Metodo para Monitor:** 
- driver.set_window_size(1920, 1080)

**Metodo para Tablet:** 
- driver.set_window_size(768, 1024)


**Metodo para Mobil:** 
- driver.set_window_size(375, 667)


### Métricas a Utilizar:

- Tiempo de ejecución de pruebas.
- Cantidad de casos de prueba exitosos y fallidos.
- Tiempo promedio de ejecución por caso de prueba.
