from flask import Blueprint, render_template, request

# Blueprint obj, register in app.py to add all views to the website
bp = Blueprint('error_views', __name__, template_folder='templates/error_views')


@bp.app_errorhandler(404)
def status_404(error):
    # log the error here if there is corresponding logging policy

    # define params
    params = {
        'url' : request.path
    }
    return (render_template('error_views/status_404.html', **params), 404)

@bp.app_errorhandler(500)
def status_404(error):
    params = {
        'url': request.path
    }
    return (render_template('error_views/status_500.html', **params), 500)


@bp.app_errorhandler(Exception)
def all_exceptions(error):
    # log the error here if there is corresponding logging policy
    # define params
    params = {
        'url': request.path
    }
    return (render_template('error_views/exception.html', **params), 500)


