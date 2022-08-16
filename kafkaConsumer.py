import grpc
import newsGrpc_pb2, newsGrpc_pb2_grpc


def run():
    topic = "ENTERTAINMENT"
    with grpc.insecure_channel("localhost:50052") as channel:
        stub = newsGrpc_pb2_grpc.KafkaBrokerStub(channel)
        response = stub.Consumer(newsGrpc_pb2.Topic(topic_name=topic))
        print(f"User's headline search log for topic {topic}: ")
        for p_message in response:
            print(p_message.headline)

if __name__ == "__main__":
    # topic = input("Enter the topic you want to streaming: ")
    run()
