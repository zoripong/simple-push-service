import abc
import dataclasses
import datetime

from grpc._server import _Context

from app.rpc.push_pb2 import PushInstantlyResponse, PushInstantlyRequest
from app.rpc.push_pb2_grpc import PushServiceServicer


@dataclasses.dataclass(frozen=True)
class PushMessage:
    content: str

    send_at: datetime.datetime

    sender_id: int

    receiver_id: int


class PushClient(abc.ABC):
    @abc.abstractmethod
    def send(self, message: PushMessage):
        ...


class PushServiceImpl(PushServiceServicer):

    def __init__(self, client: PushClient):
        self.client = client

    def PushInstantly(self, request: PushInstantlyRequest, context: _Context):
        self.client.send(
            PushMessage(
                content=request.content,
                sender_id=request.sender_id,
                send_at=datetime.datetime.utcfromtimestamp(request.send_at),
                receiver_id=request.receiver_id,
            )
        )
        return PushInstantlyResponse(success=True)
