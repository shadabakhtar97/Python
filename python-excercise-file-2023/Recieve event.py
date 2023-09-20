import asyncio
from azure.eventhub.aio import EventHubConsumerClient
from azure.eventhub.extensions.checkpointstoreblobaio import BlobCheckpointStore

async def on_event(partition_context, event):
    print("Received the event: \"{}\" from the partition with ID: \"{}\"".format(event.body_as_str(encoding='UTF-8'), partition_context.partition_id))

    await partition_context.update_checkpoint(event)

async def main():
    checkpoint_store = BlobCheckpointStore.from_connection_string("DefaultEndpointsProtocol=https;AccountName=checkpointblob1234;AccountKey=ULOrl4CCJzwV51bdOH378wGxF6RcyojaOeZbPPwrP/wMNoqJbe/Ivx56Lrr1fiM4IFiqJNWI20A1+Aq/apkkhw==;EndpointSuffix=core.windows.net", "checkpointblob")

    client = EventHubConsumerClient.from_connection_string("Endpoint=sb://pluralsighthub.servicebus.windows.net/;SharedAccessKeyName=Listen;SharedAccessKey=Zr9E7IDe2cTEPOgvCT9Ql/nSksFZ+XEQ9K7xLFiktRA=;EntityPath=mainhub", consumer_group="$Default", eventhub_name="mainhub", checkpoint_store=checkpoint_store)
    async with client:
        await client.receive(on_event=on_event)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main()) 