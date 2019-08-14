from flask import Blueprint, render_template, request, url_for
from flask_login import login_required
from blaise_mi_extract_api.models import ApiKey
from blaise_mi_extract_api.extensions import login_manager
from blaise_mi_extract_api.functions import search_db
import base64


api_view = Blueprint('api_views', __name__, url_prefix="/", template_folder='templates')


@api_view.route('/example_route', methods=['GET'])
@login_required
def example_route():
    name = request.args.get('name', '')
    message = search_db()
    return 'Hello ' + name


@login_manager.request_loader
def load_user_from_request(api_request):

    # first, try to login using the api_key url arg
    api_key_lookup = api_request.args.get('api_key')
    if api_key_lookup:
        api_key = ApiKey.query.filter_by(api_key=api_key_lookup).first()
        if api_key:
            return api_key

    # next, try to login using Basic Auth
    api_key_lookup = api_request.headers.get('Authorization')
    if api_key_lookup:
        api_key_lookup = api_key_lookup.replace('Basic ', '', 1)
        try:
            api_key_lookup = base64.b64decode(api_key_lookup)
            api_key_lookup = api_key_lookup.decode().split(":")[-1]
        except TypeError:
            pass
        api_key = ApiKey.query.filter_by(api_key=api_key_lookup).first()
        if api_key:
            return api_key

    # finally, return None if both methods did not login the user
    return None