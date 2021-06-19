from app.service import PushClient, PushMessage


class PushClientImpl(PushClient):
    def __init__(self, url: str):
        self.url = url

    def send(self, message: PushMessage):
        print(
            f'[{self.url}]: '
            f'{message.sender_id}가 {message.receiver_id}에게 '
            f'{message.content}에 {message.content} 전송'
        )
