from concurrent import futures

from grpc import server

from app.client import PushClientImpl
from app.rpc.push_pb2_grpc import add_PushServiceServicer_to_server
from app.service import PushServiceImpl


def serve():
    app = server(futures.ThreadPoolExecutor(max_workers=10))
    add_PushServiceServicer_to_server(
        PushServiceImpl(PushClientImpl('https://localhost:2020/push')), app
    )
    app.add_insecure_port('[::]:50051')
    app.start()
    app.wait_for_termination()


if __name__ == '__main__':
    serve()
