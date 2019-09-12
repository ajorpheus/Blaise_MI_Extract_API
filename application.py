import blaise_mi_extract_api
from blaise_mi_extract_api.util.service_logging import log

log.info("application started")
app = blaise_mi_extract_api.create_app()
