from app.pkg.connectors.http import HttpRequest
from app.pkg import models


class TransactionClient(HttpRequest):

	async def create_balance(self, cmd: models.app.transaction.CreateBalance):
		await self.request(
			cmd=cmd,
			method="POST",
			path="balance",
		)
