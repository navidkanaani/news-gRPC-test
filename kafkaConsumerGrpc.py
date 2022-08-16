import grpc
from concurrent import futures
import newsGrpc_pb2, newsGrpc_pb2_grpc
from kafka import KafkaConsumer


class KafkaConsumerServicer(newsGrpc_pb2_grpc.KafkaBroker):
    def Consumer(self, request, context):
        """
        Kafka consumer rpc. Consume messages related to requested topic from kafka borker.
        """
        # print(f"Request: {request}")
        consumer = KafkaConsumer(request.topic_name, bootstrap_servers="localhost:9092")
        # print(f"Consumer: {consumer}")
        for messages in consumer:
            kafka_message = messages.value # Contines the searched headline
            # print(f"Kafka message: {kafka_message}")
            yield newsGrpc_pb2.NewsHeadline(headline=kafka_message)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    newsGrpc_pb2_grpc.add_KafkaBrokerServicer_to_server(KafkaConsumerServicer(), server)
    server.add_insecure_port("[::]:50052")
    server.start()
    print("Kafka Consumer gRPC server is running...")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()