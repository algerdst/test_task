from django import template
from ..models import Menu

register = template.Library()


@register.simple_tag()
def get_menus():
    return Menu.objects.all()


@register.simple_tag()
def draw_menu(slug):
    return Menu.objects.get(slug=slug)
