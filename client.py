from fileinput import close
import grpc
import redis
import json
import sys
import newsGrpc_pb2, newsGrpc_pb2_grpc
import kafkaProducer


def show_titles(id, news):
    """
    Show a brief summary of the news.
    A client could choose one of them and see its details.
    """
    print("News id --> {}".format(id))
    print("News title --> {}".format(news["headline"]))
    print("News category --> {}".format(news["category"]))
    print("-"*100)


def show_news_detail(news_id):
    """
    Show all the exisiting information about a given news id.
    """
    redis_client = redis.Redis("localhost", 6379, db=0)
    news_obj = redis_client.get(news_id)  # get all information of a news from cached memory.
    news = json.loads(news_obj)
    for key, info in news.items():
        print(f"{str(key).capitalize()}: {info}")
    print("")
    return news


def cache_news(news_id, news_obj):
    """
    Given a news obj and its relative id, cache them in redis server.
    """
    # Connect to redis
    redis_client = redis.Redis("localhost", 6379, db=0)
    redis_client.set(news_id, json.dumps(news_obj))
    redis_client.expire(news_id, 300)   # set TTL


def run(search_txt):
    # Search gRPC client setup
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = newsGrpc_pb2_grpc.newsGrpcStub(channel)
        response = stub.Search(newsGrpc_pb2.News(headline=search_txt))
        id = 0  # Define an id to make retrieving news easier for user (It's not existed in the DB!)
        for news in response.News:
            id += 1
            news_id = f"news:{str(id).zfill(3)}"
            news_obj = {
                "headline": news.headline,
                "category": news.category,
                "date": news.date,
                "authors": news.authors,
                "short_description": news.short_description,
                "link": news.link
            }
            show_titles(news_id, news_obj)  # Show a list of relative news.
            # save all news with details in cache memory
            cache_news(news_id, news_obj)

    while True:
        look_for_id = input(">> Which news do you want to see? (Enter news id) ")
        if look_for_id != "0":  # If input == 0 close the script
            news_detail = show_news_detail(look_for_id)
            # Send the details of the news that client read to the Kafka producer
            kafkaProducer.kafka_producer(news_detail)
        else:
            sys.exit()
            break


if __name__ == "__main__":
    searched_headline = input(">> Enter the headline you're looking for: ")
    run(searched_headline)
