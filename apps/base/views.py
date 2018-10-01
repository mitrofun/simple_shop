from django.views import defaults


def page_not_found(*args, **kwargs):
    kwargs['template_name'] = '404.html'
    return defaults.page_not_found(*args, **kwargs)


def server_error(*args, **kwargs):
    kwargs['template_name'] = '500.html'
    return defaults.server_error(*args, **kwargs)


def bad_request(*args, **kwargs):
    kwargs['template_name'] = '400.html'
    return defaults.bad_request(*args, **kwargs)
