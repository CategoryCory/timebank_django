from django import template

register = template.Library()


@register.inclusion_tag('forms/form_input.html')
def form_input(field, num_cols=None):
    return {'field': field, 'num_cols': num_cols}


@register.inclusion_tag('forms/form_checkbox.html')
def form_checkbox(field):
    return {'field': field}
