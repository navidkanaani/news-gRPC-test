import grpc
from concurrent import futures
from elasticsearch import Elasticsearch
import newsGrpc_pb2, newsGrpc_pb2_grpc
import kafkaAdmin


def create_elsClient():
    """
    Connect and return an Elastic client. (locally)
    """
    ELASTIC_PASSWORD = "na1234"
    els_client = Elasticsearch(
        "https://localhost:9200", basic_auth=("elastic", ELASTIC_PASSWORD), verify_certs=False)
    return els_client


def search_news_query(els_client, headline):
    """
    Giving an els client, a headline and a category. 
    Search for that headline and category in elasticsearch and returns its appropriate query result.
    """
    query = els_client.search(index="news_headlines", body={
        "query": {
            "match": {
                "headline": {
                    "query": str(headline),
                    "operator": "and"
                }
            }
        }
    })
    query_result = query["hits"]["hits"]
    return query_result


def clean_query_result(query_result):
    """
    Clean the result of a query and extracts its important data.
    """
    cleaned_news = {}
    for news in query_result:
        news_data = news["_source"]  # retrieve considered values
        cleaned_news = {
            "headline": news_data["headline"],
            "category": news_data["category"],
            "date": news_data["date"],
            "authors": news_data["authors"],
            "link": news_data["link"],
            "short_description": news_data["short_description"]
        }
        yield cleaned_news  # Return cleaned news


def get_categories(els_client):
    """
    Retrieve all categories to create their corresponding topics in the Kafka admin.
    """
    categories = [] # List of categories
    # Query a list of categories from elastic search client
    topics_agg = els_client.search(index="news_headlines", body={"aggs": {
        "by_category": {
            "terms": {
                "field": "category",
                "size": 200
            }
        }
    }})
    # Retrieve categories from elastic query output
    cats_temp = topics_agg["aggregations"]["by_category"]["buckets"]
    for cat in cats_temp:
            categories.append(cat["key"])
    return categories

# News gRPC for search in elasticsearch
class newsGrpcServicer(newsGrpc_pb2_grpc.newsGrpcServicer):
    def Search(self, request, context):
        els_client = create_elsClient() # Create elasticsearch client
        els_query = search_news_query(els_client, request.headline) # Search for required headline
        cleaned_result = clean_query_result(els_query)  # Clean result
        return newsGrpc_pb2.ListOfNews(News=cleaned_result) # Return a list of news


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    newsGrpc_pb2_grpc.add_newsGrpcServicer_to_server(
        newsGrpcServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    # Retrieve all categories and send them to kafka admin to create topics (Just for first time!)
    els_client = create_elsClient()
    topics = get_categories(els_client)
    kafkaAdmin.create_topic(topics) # Create relative topics in kafka
    # Run grpc server
    serve()

