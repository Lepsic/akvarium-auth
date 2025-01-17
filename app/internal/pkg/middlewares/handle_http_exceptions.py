"""Handlers that handle internal error raise and returns ``http json``
response.

Examples:
    For example, if in some level in code you raise error inherited by
    :class:`.BaseAPIException`::

        >>> ...  # exceptions.py
        >>> class E(BaseAPIException):
        ...     status_code = status.HTTP_200_OK
        ...     message = "test error."

        >>> ...  # some_file.py
        >>> async def some_internal_function():
        ...     raise E

    When ``some_internal_function`` called, exception will process by
    ``handle_api_exceptions`` and returns a json object with status code 200::

        {
            "message": "test error."
        }
"""

from starlette import status
from starlette.requests import Request
from starlette.responses import JSONResponse

from app.pkg.logger import get_logger
from app.pkg.models.base import BaseAPIException

__all__ = [
    "handle_api_exceptions",
]

logger = get_logger(__name__)


def handle_api_exceptions(request: Request, exc: BaseAPIException):
    """Handle all internal exceptions that inherited from
    :class:`.BaseAPIException`.

    Args:
        request:
            ``Request`` instance.
        exc:
            Exception inherited from :class:`.BaseAPIException`.

    Returns:
        ``JSONResponse`` object with status code from ``exc.status_code``.
    """

    del request  # unused

    logger.info(exc)

    return JSONResponse(status_code=exc.status_code, content={"message": exc.message})


