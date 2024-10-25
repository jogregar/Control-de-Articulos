from django import template

register = template.Library()

@register.filter
def custom_floatformat(value):
    # Asegúrate de que sea un número y luego reemplaza el punto por una coma
    return f'{value:,.2f}'.replace(",", "X").replace(".", ",").replace("X", ".")
