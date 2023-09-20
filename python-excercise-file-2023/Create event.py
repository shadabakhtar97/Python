import asyncio
from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub import EventData

async def run():
    producer = EventHubProducerClient.from_connection_string(conn_str="Endpoint=sb://shadabnamespace1.servicebus.windows.net/;SharedAccessKeyName=send1;SharedAccessKey=nWZWvg91NJt0qEgpxZEglt9AJFuw/t6KT+AEhCW35K8=;EntityPath=shadab-event-hub1", 
                                                             eventhub_name="shadab-event-hub1")
    async with producer:
        event_data_batch = await producer.create_batch()

        event_data_batch.add(EventData('{ "sensor": "temperature", "value": "88" }'))
        event_data_batch.add(EventData('{ "sensor": "humidity", "value": "0.5" }'))

        await producer.send_batch(event_data_batch)

loop = asyncio.get_event_loop()
loop.run_until_complete(run())

print("Event submitted!")