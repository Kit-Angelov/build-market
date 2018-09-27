from django import template

register = template.Library()


def days_format(value):
    value_list = list(str(value))
    result = ''
    if value_list[0] == '1': result += 'пн '
    if value_list[1] == '1': result += 'вт '
    if value_list[2] == '1': result += 'ср '
    if value_list[3] == '1': result += 'чт '
    if value_list[4] == '1': result += 'пт '
    if value_list[5] == '1': result += 'сб '
    if value_list[6] == '1': result += 'вс '
    return result


register.filter('days_format', days_format)