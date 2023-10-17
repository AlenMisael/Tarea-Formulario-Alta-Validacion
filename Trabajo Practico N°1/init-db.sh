#!/bin/bash

if [ ! -f /var/lib/postgresql/data/PG_VERSION ]; then
    echo "Inicializando la base de datos..." 
    pg_restore -U postgres -d pacientesALyP < backup.sql
    echo "Base de datos inicializada desde el backup."
else
    echo "La base de datos ya ha sido inicializada anteriormente. No se ejecuta el backup"


