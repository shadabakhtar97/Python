import asyncio, time
from random import random
from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub import EventData

async def run():
    producer = EventHubProducerClient.from_connection_string(conn_str="Endpoint=sb://pluralsighthub.servicebus.windows.net/;SharedAccessKeyName=SendEvents;SharedAccessKey=Yjl2YqCyRL3/ECiIpsICbMClwiWE0DXBlla87MmwI6I=", 
                                                             eventhub_name="mainhub")
    async with producer:
        event_data_batch = await producer.create_batch()

        event_data_batch.add(EventData('{ "sensor": "temperature", "value": "' + str(int(random() * 100)) + '" }'))


        await producer.send_batch(event_data_batch)

loop = asyncio.get_event_loop()

while(True):
    loop.run_until_complete(run())
    time.sleep(0.25)

    print("Event submitted!")