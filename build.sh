#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate

# Criar administrador inicial somente quando solicitado
if [ "$CREATE_ADMIN" = "true" ]; then
    python manage.py criar_admin
fi