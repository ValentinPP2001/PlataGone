import os
from django.apps import apps
from django.db import models
from django.utils.text import slugify

def generar_ruta_comprobante(instance, filename):
    try:
        # 1. Obtenemos el ID de la FK directo de la instancia
        tipo_comprobante_id = instance.tipo_comprobante_id

        # 2. Traemos el modelo de forma dinámica usando el nombre de tu app (reemplaza 'comprobantes' por el nombre real de tu app)
        TipoComprobante = apps.get_model('comprobantes', 'TipoComprobante')

        # 3. Buscamos el registro para extraer su nombre
        tipo_comp = TipoComprobante.objects.get(id=tipo_comprobante_id)
        nombre_tipo = tipo_comp.nombre

    except Exception:
        # Respaldo de seguridad en caso de fallo
        nombre_tipo = "sin_tipo"

    # 4. Sanitizamos el nombre de la carpeta (ej: "Ticket Supermercado" -> "ticket_supermercado")
    carpeta_tipo = slugify(nombre_tipo).replace('-', '_')

    # 5. Retornamos la ruta final dentro de la carpeta 'comprobantes'
    return os.path.join(f"comprobantes/{carpeta_tipo}/", filename)