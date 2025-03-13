from app.database.config import database
from app.database.models import Client, Debt, Payment

import asyncio

await database.connect()


payments = await Payment.objects.all()


# await Debt.objects.delete(each=True)
# await Client.objects.delete(each=True)

print(payments)
