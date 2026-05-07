# Transmi-Admin

Sistema de Gestión Administrativa para TransMilenio — Bogotá, Colombia.

## Integrantes

- Jaime Calderon
- Octavio Velasco

## Stack

- **Backend:** Django 6.x + Python 3
- **Base de datos:** SQLite (desarrollo)
- **Frontend:** Bootstrap 5.3 + Bootstrap Icons (CDN)
- **Sin dependencias externas** adicionales

## Características implementadas

- **5 apps Django** separadas con arquitectura limpia
- **UUID como primary key** en todos los modelos
- **FBV y CBV** — vistas basadas en función y en clase
- **CRUDs completos** en todas las apps
- **Formularios** con `forms.Form`, `forms.ModelForm`, widgets, placeholders y validaciones `clean()`
- **Búsqueda, filtros y paginación** en todas las listas
- **Messages framework** para feedback al usuario
- **Template inheritance** — `base.html` con navbar, sidebar, footer reutilizables
- **`{% extends %}`, `{% block %}`, `{% include %}`, `{% load static %}`**, loops y condicionales
- **Admin personalizado** con inlines, filtros y búsqueda para todos los modelos
- **Archivos estáticos** configurados correctamente (CSS + JS propios)
- **Métodos custom** en modelos (`@property`, `__str__`, helpers de badge)

## Módulos

| App | Modelos | Funcionalidades |
|---|---|---|
| `flota` | TipoBus, Bus, Conductor | CRUD buses (FBV) + CRUD conductores (CBV) + tipos |
| `rutas` | Portal, Ruta, HorarioRuta | CRUD rutas (FBV) + horarios anidados + CRUD portales (CBV) |
| `estaciones` | Estacion, TaquillaCarga, IncidenciaEstacion | CRUD estaciones + taquillas + incidencias |
| `usuarios` | TipoTarjeta, UsuarioTullave, RecargaTarjeta | CRUD usuarios + recarga de saldo + tipos tarjeta (CBV) |
| `mantenimiento` | TipoMantenimiento, OrdenMantenimiento, Repuesto, DetalleMantenimiento | CRUD órdenes (FBV) + CRUD repuestos (CBV) + alerta stock |

## Instalación y ejecución

```bash
# 1. Clonar e instalar dependencias
pip install -r requirements.txt

# 2. Aplicar migraciones
python3 manage.py migrate

# 3. (Opcional) Crear superusuario para el panel admin
python3 manage.py createsuperuser

# 4. Correr el servidor
python3 manage.py runserver
```

Luego abre: **http://127.0.0.1:8000/**

## Estructura del proyecto

```
Transmi-Admin/
├── Transmi_Admin/          # Configuración principal
│   ├── settings.py
│   ├── urls.py
│   └── views.py            # Handlers de error 404/500
├── templates/              # Templates globales
│   ├── base.html
│   ├── includes/
│   │   ├── navbar.html
│   │   ├── sidebar.html
│   │   ├── footer.html
│   │   └── messages.html
│   └── errors/
│       ├── 404.html
│       └── 500.html
├── static/
│   ├── css/main.css
│   └── js/main.js
├── flota/
├── rutas/
├── estaciones/
├── usuarios/
└── mantenimiento/
```

## URLs principales

| URL | App | Descripción |
|---|---|---|
| `/` | — | Redirect a flota |
| `/flota/` | flota | Dashboard con estadísticas |
| `/flota/buses/` | flota | Lista de buses |
| `/flota/conductores/` | flota | Lista de conductores |
| `/rutas/` | rutas | Lista de rutas |
| `/rutas/portales/` | rutas | Lista de portales |
| `/estaciones/` | estaciones | Lista de estaciones |
| `/usuarios/` | usuarios | Lista de usuarios Tullave |
| `/mantenimiento/` | mantenimiento | Lista de órdenes |
| `/mantenimiento/repuestos/` | mantenimiento | Inventario de repuestos |
| `/admin/` | Django Admin | Panel administrativo |
