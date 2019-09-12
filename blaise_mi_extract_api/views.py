import base64

from blaise_mi_extract_api.util.service_logging import log
from flask import Blueprint, jsonify, abort
from flask_login import login_required

from blaise_mi_extract_api.extensions import login_manager
from blaise_mi_extract_api.functions import map_to_management_info
from blaise_mi_extract_api.models import ApiKey

api_view = Blueprint('api_views', __name__, url_prefix="/", template_folder='templates')


@api_view.errorhandler(404)
@login_required
def data_not_found(e):
    return jsonify(error=str(e)), 404


@api_view.route('/management_information/<survey_tla>/<field_period>', methods=['GET'])
@login_required
def management_information(survey_tla, field_period):
    log.info("Requesting management information for survey_tla=" + survey_tla + " and field_period=" + field_period)

    management_info_out = map_to_management_info(survey_tla, field_period)

    if management_info_out is None:
        log.warning('No management info found for ' + survey_tla + field_period)
        abort(404, description='Check that the survey_tla (' + survey_tla +
                               ') and the field period (' + field_period + ') are correct')
    log.info("Providing management information data")
    return management_info_out


@login_manager.request_loader
def load_user_from_request(api_request):
    # first, try to login using the api_key url arg
    api_key_lookup = api_request.args.get('api_key')
    if api_key_lookup:
        log.info("Checking database for api_key")
        api_key = ApiKey.query.filter_by(api_key=api_key_lookup).first()
        if api_key:
            log.info("api_key approved")
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
            log.info("api_key approved")
            return api_key

    log.warning('Authorization failed. Check the api_key')

    # finally, return None if both methods did not login the user
    return None
