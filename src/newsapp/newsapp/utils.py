from rest_framework.response import Response
from rest_framework.views import exception_handler


class CustomResponse(Response):
    def __init__(
        self,
        data=None,
        status=None,
        template_name=None,
        headers=None,
        exception=False,
        content_type=None,
    ):
        super().__init__(
            data=data,
            status=status,
            template_name=template_name,
            headers=headers,
            exception=exception,
            content_type=content_type,
        )
        self.data["success"] = True


def apply_custom_response(func):
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        if isinstance(response, Response):
            return CustomResponse(response.data, response.status_code)
        return response

    return wrapper


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        response.data["success"] = False
    return response
