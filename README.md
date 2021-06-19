
# Simple Push Service

push 보내는 척 하는 푸시 서비스
python으로 구현된 grpc 서버 구현체이다.

## how to run

```bash
$ python3 -m venv .venv
$ source ./.venv/bin/activate
$ poetry install
$ python run.py
```

## todo
- [ ] receiverId를 통해 푸시 토큰 가져올 수 있도록 수정
- [ ] 실제 푸시 발송
- [ ] 푸시 발송 내역 저장
- [ ] bulk 푸시 발송 API 추가
- [ ] grpc stub 떼어내기

## related repository
- go client: https://github.com/zoripong/simple-chat-service
- schema: https://github.com/zoripong/push-schema
