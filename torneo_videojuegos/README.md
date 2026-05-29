# Sistema de Gestión de Torneos de Videojuegos

## Información General

- **Asignado por:** Daniela
- **Fecha de Entrega:** Mayo 29, 2026
- **Objetivo:** Desarrollar un sistema en Python que permita administrar un torneo de videojuegos con registro de jugadores, puntajes y ranking.

---

## Descripción del Proyecto

Este es un sistema completo de gestión de torneos de videojuegos, implementado siguiendo el patrón de arquitectura **MVC (Model-View-Controller)** con interfaz **Tkinter** y almacenamiento de datos en **SQLite3**. El programa permite registrar jugadores, gestionar puntajes acumulados, consultar rankings y buscar jugadores de forma intuitiva.

---

## Estructura del Proyecto

```
torneo_videojuegos/
├── main.py              # Punto de entrada del programa
├── model.py             # Lógica de negocio y acceso a datos (SQLite)
├── vista.py             # Interfaz gráfica (Tkinter)
├── controlador.py       # Controlador que maneja las interacciones
└── torneo_videojuegos.db # Base de datos SQLite (se crea automáticamente)
```

### Descripción de Archivos

- **`main.py`**: Punto de entrada del programa. Inicializa la interfaz Tkinter y el controlador.
- **`model.py`**: Contiene la clase `ModeloTorneo` que gestiona todas las operaciones de base de datos, validaciones y lógica de negocio.
- **`vista.py`**: Contiene la clase `VistaTorneo` que define la interfaz gráfica con Tkinter.
- **`controlador.py`**: Contiene la clase `ControladorTorneo` que coordina las acciones entre el modelo y la vista.

---

## Requerimientos del Sistema

### 1. **Registrar Jugador**
Permite agregar un nuevo jugador al torneo. El usuario debe ingresar:
- Nombre del jugador
- Videojuego favorito
- Puntaje inicial (opcional, por defecto 0)

**Validaciones:**
- El nombre no puede estar vacío
- El videojuego no puede estar vacío
- El puntaje inicial debe ser un número entero válido y no negativo
- Los IDs se generan automáticamente (no se repiten)

### 2. **Mostrar Jugadores Registrados**
Muestra una tabla con todos los jugadores registrados en el sistema.

**Información mostrada:**
- ID del jugador
- Nombre
- Videojuego favorito
- Puntaje acumulado

**Características:**
- Tabla interactiva con interfaz Tkinter
- Datos ordenados por ID ascendente

### 3. **Registrar Puntajes**
Permite actualizar el puntaje de un jugador después de cada partida.

**Funcionalidad:**
- Ingresa el ID del jugador
- Ingresa los puntos ganados en la partida
- El sistema suma automáticamente los puntos al puntaje acumulado
- Muestra el nuevo puntaje total

**Validaciones:**
- El ID del jugador debe existir
- Los puntos deben ser números enteros válidos
- Los puntos no pueden ser negativos

### 4. **Mostrar Ranking de Jugadores**
Muestra todos los jugadores ordenados de mayor a menor puntaje.

**Características:**
- Tabla con datos ordenados por puntaje descendente
- En caso de empate, se ordena alfabéticamente por nombre
- Facilita ver el desempeño de cada jugador

### 5. **Buscar Jugador por Nombre**
Permite buscar uno o varios jugadores por nombre.

**Funcionalidad:**
- Acepta búsqueda parcial (no requiere nombre exacto)
- Busca sin distinción de mayúsculas/minúsculas
- Muestra todos los resultados que coincidan

**Características:**
- Búsqueda flexible y amigable
- Muestra todos los datos del jugador encontrado

### 6. **Salir**
Cierra la aplicación de forma ordenada.

---

## Características Técnicas

### Interfaz Gráfica
- **Framework:** Tkinter
- **Componentes:**
  - Campos de entrada (Entry) para datos del jugador
  - Tabla interactiva (Treeview) para mostrar datos
  - Botones para cada funcionalidad
  - Separadores visuales para mejor organización

### Base de Datos
- **Sistema:** SQLite3
- **Archivo:** `torneo_videojuegos.db`
- **Tabla `jugadores`:**
  - `id` (INTEGER PRIMARY KEY AUTOINCREMENT)
  - `nombre` (TEXT NOT NULL)
  - `videojuego` (TEXT NOT NULL)
  - `puntaje` (INTEGER NOT NULL DEFAULT 0)

### Validaciones Implementadas
✓ No se permiten nombres vacíos
✓ Los IDs se generan automáticamente y no se repiten
✓ El puntaje se valida como número entero y no negativo
✓ El puntaje se actualiza correctamente (suma acumulativa)
✓ Búsqueda flexible sin distinción de mayúsculas
✓ Ranking ordenado por puntaje descendente

### Interfaz de Usuario
- Formularios organizados por secciones
- Tabla Treeview para visualizar datos
- Botones intuitivos para cada acción
- Mensajes informativos y de error
- Campos se limpian después de cada operación exitosa

---

## Estructura de Datos

### Jugador (en base de datos)
```python
{
    'id': 1,                      # Identificador único (auto-generado)
    'nombre': 'Juan',             # Nombre del jugador
    'videojuego': 'Minecraft',    # Videojuego favorito
    'puntaje': 250                # Puntaje acumulado
}
```

---

## Cómo Ejecutar

1. **Requisitos:**
   - Python 3.6 o superior
   - Tkinter (incluido en Python)
   - SQLite3 (incluido en Python)

2. **Ejecución:**
   ```bash
   python main.py
   ```

3. **Uso:**
   - Se abrirá una ventana gráfica con el menú
   - Completa los campos requeridos
   - Haz clic en el botón correspondiente
   - La tabla se actualiza automáticamente con los cambios

---

## Ejemplo de Uso

1. **Registrar Jugador:**
   - Nombre: "Carlos"
   - Videojuego: "Valorant"
   - Puntaje inicial: 0
   - → Jugador registrado con ID: 1

2. **Registrar Puntajes:**
   - ID del jugador: 1
   - Puntos ganados: 150
   - → Puntaje actualizado. Nuevo puntaje: 150

3. **Mostrar Ranking:**
   - Se muestra tabla con jugadores ordenados por puntaje (mayor a menor)

4. **Buscar Jugador:**
   - Término: "Car"
   - → Muestra a "Carlos" con todos sus datos

---

## Flujo de Funcionamiento

```
┌─────────────────────────────────────┐
│    Iniciar Aplicación (main.py)     │
└────────────┬────────────────────────┘
             │
             ▼
┌─────────────────────────────────────┐
│   Cargar Base de Datos (SQLite)     │
└────────────┬────────────────────────┘
             │
             ▼
┌─────────────────────────────────────┐
│   Mostrar Interfaz Gráfica (Tkinter)│
└────────────┬────────────────────────┘
             │
    ┌────────┴──────────────────────────────────────┐
    │                                               │
    ▼                                               ▼
┌──────────────┐                          ┌─────────────────┐
│ Usuario hace │                          │ Controlador     │
│  selección   │◄────────────────────────►│ procesa acción  │
└──────────────┘                          └────────┬────────┘
    │                                               │
    │                                               ▼
    │                                      ┌─────────────────┐
    │                                      │ Modelo consulta │
    │                                      │ base de datos   │
    │                                      └────────┬────────┘
    │                                               │
    │                                               ▼
    │                                      ┌─────────────────┐
    │◄─────────────────────────────────────│ Vista actualiza │
    │                                      │ tabla/mensajes  │
    │                                      └─────────────────┘
    │
    └──────────────────► Volver al inicio
```

---

## Tecnologías Utilizadas

- **Lenguaje:** Python 3
- **Interfaz Gráfica:** Tkinter
- **Base de Datos:** SQLite3
- **Arquitectura:** Patrón MVC
- **Paradigma:** Programación Orientada a Objetos (POO)

---

## Notas Finales

Este sistema implementa correctamente los principios de desarrollo de software:
- Separación de responsabilidades (patrón MVC)
- Encapsulación de datos y funcionalidad
- Validación robusta de entrada
- Manejo de excepciones
- Persistencia de datos en base de datos
- Interfaz gráfica amigable y responsiva
- Código modular y reutilizable

---

**Asignado por:** Daniela  
**Implementado por:** Equipo de Desarrollo  
**Última actualización:** Mayo 29, 2026
