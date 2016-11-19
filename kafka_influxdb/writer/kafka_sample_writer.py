from kafka import KafkaProducer
import random
import logging


class KafkaWriterException(Exception):
    pass


class KafkaSampleWriter(object):
    """
    KafkaSampleWriter can be used to write sample messages into Kafka for
    benchmark purposes
    """

    def __init__(self, host, port, topic):
        logging.info("Connecting to Kafka broker at %s:%s", host, port)
        self.kafka_client = KafkaProducer(bootstrap_servers="{}:{}".format(host, port))
        self.topic = topic

        self.sample_messages = [
            b"""26f2fc918f50.load.load.shortterm 0.05 1436357630
            26f2fc918f50.load.load.midterm 0.05 1436357630
            26f2fc918f50.load.load.longterm 0.05 1436357630""",
            b"26f2fc918f50.cpu-0.cpu-user 30364 1436357630",
            b"26f2fc918f50.memory.memory-buffered 743657472 1436357630"
        ]

    def produce_messages(self, num_messages=1000000):
        """
        Produce Kafka sample messages
        :param batches: number of message batches
        :param batch_size: messages per batch
        :return:
        """
        for i, message in enumerate(random.choice(self.sample_messages)):
            if i > num_messages:
                break
            print(message)
            result = self.kafka_client.send(self.topic, message)
            print(result)
        self.kafka_client.flush()
