from django import template

register = template.Library()

@register.filter(name='is_saved')
def is_saved(book,save):
    keys = save.keys()
    for id in keys:
        if int(id) == book.id:
            return True
    return False