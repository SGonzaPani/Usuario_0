# mi_nuevo_blog/blog/templatetags/blog_filters.py

from django import template
import re # Importa el módulo de expresiones regulares

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """
    Permite acceder a un elemento de un diccionario en las plantillas.
    Uso: {{ my_dict|get_item:key }}
    """
    return dictionary.get(key)

@register.filter
def replace_youtube_url(url):
    """
    Transforma una URL de visualización de YouTube en una URL de embed para usar en iframes.
    Ej: https://www.youtube.com/watch?v=VIDEO_ID -> https://www.youtube.com/embed/VIDEO_ID
    Ej: https://youtu.be/VIDEO_ID -> https://www.youtube.com/embed/VIDEO_ID
    """
    if not url:
        return ""

    # Patrón para extraer el ID del video de URLs de YouTube
    # Captura tanto el formato watch?v= como youtu.be/
    match_watch = re.search(r'(?:youtube\.com/(?:[^/]+/.+/|(?:v|e(?:mbed)?)/|.*[?&]v=)|youtu\.be/)([^"&?/ ]{11})', url)
    
    if match_watch:
        video_id = match_watch.group(1)
        return f"https://www.youtube.com/embed/{video_id}"
    
    # Si ya es una URL de embed o no es de YouTube, la devuelve tal cual
    return url