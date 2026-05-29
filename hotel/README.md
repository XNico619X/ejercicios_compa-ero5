# Sistema de Gestión de Reservas de Hotel

## Información General

- **Aignado por:** Daniela
- **Fecha de Entrega:** Mayo 29, 2026
- **Objetivo:** Desarrollar un sistema en Python que permita administrar las reservas de un hotel con interfaz de menú interactivo.

---

## Descripción del Proyecto

Este es un sistema completo de gestión de reservas para un hotel, implementado siguiendo el patrón de arquitectura **MVC (Model-View-Controller)**. El programa permite registrar, consultar, modificar y cancelar reservas de habitaciones de forma interactiva.

---

## Estructura del Proyecto

```
hotel/
├── main.py           # Punto de entrada del programa
├── model.py          # Lógica de negocio y acceso a datos (SQLite)
├── vista.py          # Interfaz de usuario (menú en consola)
├── controller.py     # Controlador que maneja la lógica de interacción
└── hotel_reservas.db # Base de datos SQLite (se crea automáticamente)
```

### Descripción de Archivos

- **`main.py`**: Punto de entrada del programa. Inicializa el modelo, la vista y el controlador.
- **`model.py`**: Contiene la clase `HotelReservas` que gestiona todas las operaciones de base de datos y validaciones.
- **`vista.py`**: Contiene la clase `HotelVista` que maneja la presentación del menú y solicitud de datos al usuario.
- **`controller.py`**: Contiene la clase `HotelControlador` que coordina las acciones entre el modelo y la vista.

---

## Requerimientos del Sistema

### 1. **Registrar Reserva**
Permite registrar una nueva reserva en el sistema. El usuario debe ingresar:
- Nombre del cliente
- Número de habitación (1-10)
- Cantidad de noches
- Precio por noche

**Validaciones:**
- La habitación no debe estar ocupada
- El número de habitación debe estar entre 1 y 10
- La cantidad de noches debe ser mayor a cero
- El precio por noche debe ser mayor a cero

### 2. **Mostrar Habitaciones Disponibles**
Muestra un listado de todas las habitaciones que están libres y disponibles para reservar. El hotel cuenta con 10 habitaciones numeradas del 1 al 10.

**Características:**
- Verifica el estado de ocupación en la base de datos
- Muestra solo las habitaciones que no tienen reservas activas

### 3. **Consultar Reservas Realizadas**
Muestra todas las reservas registradas en el sistema con información detallada de cada una.

**Información mostrada por reserva:**
- ID de reserva
- Nombre del cliente
- Número de habitación
- Cantidad de noches
- Precio por noche
- **Total a pagar** (cantidad de noches × precio por noche)

**Información adicional:**
- Valor total acumulado de todas las reservas

### 4. **Cancelar una Reserva**
Permite cancelar una reserva existente ingresando su ID.

**Funcionalidad:**
- Busca la reserva por ID
- Elimina la reserva de la base de datos
- Libera la habitación para futuras reservas
- Valida que el ID exista

### 5. **Salir**
Cierra el programa de forma ordenada.

---

## Características Técnicas

### Base de Datos
- **Sistema:** SQLite3
- **Archivo:** `hotel_reservas.db`
- **Tabla `reservas`:**
  - `id` (INTEGER PRIMARY KEY AUTOINCREMENT)
  - `nombre` (TEXT)
  - `numero_habitacion` (INTEGER)
  - `numero_noches` (INTEGER)
  - `precio_noche` (REAL)

### Validaciones Implementadas
 No se pueden reservar habitaciones ocupadas
 Números de habitación válidos (1-10)
 Datos numéricos correctos (noches > 0, precio > 0)
 Nombres de cliente no vacíos
 Manejo de errores y excepciones

### Menú Interactivo
El programa utiliza un ciclo `while` infinito que:
- Muestra opciones al usuario
- Procesa la selección
- Ejecuta la acción correspondiente
- Vuelve al menú después de completar cada operación

---

## Cómo Ejecutar

1. **Requisitos:**
   - Python 3.6 o superior
   - SQLite3 (incluido en Python)

2. **Ejecución:**
   ```bash
   python main.py
   ```

3. **Uso:**
   - Selecciona una opción del menú (1-5)
   - Ingresa los datos solicitados
   - El sistema mostrará el resultado de la operación
   - Vuelve al menú para otra operación

---

## Ejemplo de Uso

```
=== Menú de Reserva de Hotel ===
1. Registrar reserva
2. Mostrar habitaciones disponibles
3. Consultar reservas realizadas
4. Cancelar una reserva
5. Salir
Seleccione una opción: 1

Ingrese el nombre del cliente: Juan Pérez
Ingrese el número de habitación (1-10): 5
Ingrese la cantidad de noches: 3
Ingrese el precio por noche: 100
Reserva registrada con éxito.
```

---

## Tecnologías Utilizadas

- **Lenguaje:** Python 3
- **Base de Datos:** SQLite3
- **Arquitectura:** Patrón MVC
- **Interfaz:** Menú de consola con entrada estándar

---

## Notas Finales

Este sistema implementa correctamente los principios de programación orientada a objetos (POO) con:
- Separación de responsabilidades (MVC)
- Encapsulación de datos
- Validación robusta de entrada
- Manejo de excepciones
- Persistencia de datos en base de datos

---

**Asignado por:** Daniela  
**Implementado por:** Equipo de Desarrollo  
**Última actualización:** Mayo 29, 2026
