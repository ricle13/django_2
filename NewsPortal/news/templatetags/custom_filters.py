from django import template

register = template.Library()

@register.filter()
def censor(value):
    censor_list = ('cricket', 'ball', 'soccer')
    value = value.split()
    cens_value = ''
    for val in value:
        if val.lower() not in censor_list:
            cens_value = cens_value + val + ' '
        else:
            cens_value = cens_value + val.replace(val[1::], '*'*(len(val)-1)) + ' '


    return f'{cens_value}'