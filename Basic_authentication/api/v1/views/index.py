#!/usr/bin/env python3
""" Module for views, handling 401(unauthorized) error
"""
from flask import jsonify, abort
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """ GET /api/v1/status
    Return:
      - the status of the API
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats/', strict_slashes=False)
def stats() -> str:
    """ GET /api/v1/stats
    Return:
      - the number of each objects
    """
    from models.user import User
    stats = {}
    stats['users'] = User.count()
    return jsonify(stats)


@app_views.route('/unauthorized', strict_slashes=False)
def unauthorized() -> str:
    """ GET /api/v1/unauthorized/
    Return:
      - abort(401)
    """
    abort(401)


@app_views.route('/forbidden', strict_slashes=False)
def forbidden() -> str:
    """ GET /api/v1/forbidden/
    Return:
      - abort(403)
    """
    abort(403)#!/usr/bin/env python3
""" Module for views, handling 401 (Unauthorized) and 403 (Forbidden) errors
"""
from flask import jsonify, abort
from api.v1.views import app_views

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """ 
    GET /api/v1/status
    Return:
      - JSON response indicating the status of the API
    """
    return jsonify({"status": "OK"})

@app_views.route('/stats/', strict_slashes=False)
def stats() -> str:
    """ 
    GET /api/v1/stats
    Return:
      - JSON response with the number of each type of object
    """
    from models.user import User
    stats = {}
    stats['users'] = User.count()
    return jsonify(stats)

@app_views.route('/unauthorized', strict_slashes=False)
def unauthorized() -> str:
    """ 
    GET /api/v1/unauthorized
    Return:
      - Triggers a 401 Unauthorized error
    """
    abort(401)

@app_views.route('/forbidden', strict_slashes=False)
def forbidden() -> str:
    """ 
    GET /api/v1/forbidden
    Return:
      - Triggers a 403 Forbidden error
    """
    abort(403)
