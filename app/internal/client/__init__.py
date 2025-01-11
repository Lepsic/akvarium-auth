from dependency_injector import containers, providers
from app.pkg.settings import settings
from app.internal.client.transaction import TransactionClient



class Clients(containers.DeclarativeContainer):
	transaction_client = providers.Factory(
		TransactionClient,
		url=settings.TRANSACTION.URL,
		client_name="transaction-client",
		access_token=settings.TRANSACTION.TOKEN,
	)
