# Transmi-Admin

## Integrantes
- Jaime Calderon - 
- Octavio Velasco - 

## Módulos
- flota: TipoBus, Bus, Conductor
- rutas: Portal, Ruta, HorarioRuta
- estaciones: Estacion, TaquillaCarga, IncidenciaEstacion
- usuarios: TipoTarjeta, UsuarioTullave, RecargaTarjeta
- mantenimiento: TipoMantenimiento, OrdenMantenimiento, Repuesto, DetalleMantenimiento

## Instalación
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
