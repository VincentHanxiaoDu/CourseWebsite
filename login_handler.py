from flask import session, redirect, url_for, request
from functools import wraps


def login_required(view_func):
    @wraps(view_func)
    def wrapper(*args, **kwargs):
        """
        Wraps up authentication and view function.
        :param request: request object
        :return: the view function passed in
        """
        if "user" in session:
            return view_func(*args, **kwargs)
        else:
            return redirect(url_for('views.login', request_url=request.path))
    return wrapper