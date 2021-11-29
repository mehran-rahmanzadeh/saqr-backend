from django import template

register = template.Library()


@register.simple_tag(name="query_params")
def query_params(params):
    EMPTY_PARAM = str()
    AND_PARAM = '&'
    url_params = [f'{key}={value}' for key, value in params.items() if (key != 'page' and key != 'paginate_by')]
    if url_params:
        return AND_PARAM + AND_PARAM.join(url_params)
    return EMPTY_PARAM
