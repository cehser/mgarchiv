from django import template

register = template.Library()

@register.inclusion_tag("_inc_popoverjahre.html")
def popover_jahre(jahre):
  return {"jahre": jahre}
