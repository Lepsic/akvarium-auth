"""Service layer."""

from dependency_injector import containers, providers

from app.internal.repository import Repositories, postgresql
from app.internal.client import Clients
from app.internal.services.user_service import UserService
from app.internal.services.auth_service import AuthService
from app.internal.services.crypto_service import CryptoService
from app.pkg.settings import settings

__all__ = [
    "Services",
]


class Services(containers.DeclarativeContainer):
    """Containers with services."""
    clients: Clients = providers.Container(
        Clients
    )
    repositories: postgresql.Repositories = providers.Container(
        Repositories.postgres,
    )
    crypto_service: CryptoService = providers.Factory(
        CryptoService,
        secret_key=settings.SECRET.PASSWORD_CRYPTO_KEY
    )

    user_service: UserService = providers.Factory(
        UserService,
        transaction_client=clients.transaction_client,
        user_repository=repositories.user_repository,
        crypto_service=crypto_service,
    )

    auth_service: AuthService = providers.Factory(
        AuthService,
        user_service=user_service,
        crypto_service=crypto_service,
    )
