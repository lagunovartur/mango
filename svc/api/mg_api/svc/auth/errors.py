from mg_api.errors import ExcHttp


class ExcInvalidCreds(ExcHttp):
    message = "Введены неверные учетные данные"
    status_code = 401