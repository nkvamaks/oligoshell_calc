from django import template

register = template.Library()


@register.filter
def get_item(list_, index):
    """
    Retrieves the item from the list at the specified index.
    Usage in template: {{ list|get_item:index }}
    """
    try:
        return list_[index]
    except (IndexError, TypeError):
        return None


@register.filter
def times(number):
    """
    Generates a range from 0 to 'number' - 1.

    Usage in template:
        {% for _ in 10|times %}
            <div class="calc-item-invis"></div>
        {% endfor %}
    """
    try:
        return range(int(number))
    except (ValueError, TypeError):
        return range(0)
