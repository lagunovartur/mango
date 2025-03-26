from mg_api.errors import ExcHttp


class ExcInvalidCreds(ExcHttp):
    message = "Введены неверные учетные данные"
    status_code = 401


class ExcNotAuth(ExcHttp):
    message = "Пользователь не авторизован"
    status_code = 401
