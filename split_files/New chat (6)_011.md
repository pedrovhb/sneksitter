---
file: /home/pedro/Documents/chatgpt_export/Markdown/New chat (6).md
heading_stack: <root> -> 939419cd-1f9a-4b14-a5c4-f8c686c546c7 -> System -> cf7ce9cd-1485-4499-8db2-790cdb33bfa5 -> System -> aaa28ed6-cb96-4b34-83e2-1af608c1efe6 -> User -> 39c1f41f-bbb3-4e15-a1fd-7c423cdab44b -> Assistant -> 1. **Understanding the Protocol Specifications:** -> 2. **Setup a Socket Connection:** -> 3. **Message Encoding/Decoding:**
---
### 3. **Message Encoding/Decoding:**
   - Messages exchanged are typically JSON RPC formatted, and they must be prefixed with a Content-Length header.

```python
import json

def send_message(sock: socket.socket, message: dict) -> None:
    message_str = json.dumps(message)
    message_bytes = message_str.encode('utf-8')
    headers = f"Content-Length: {len(message_bytes)}\r\n\r\n"
    sock.sendall(headers.encode('utf-8') + message_bytes)

def receive_message(sock: socket.socket) -> dict:
    # Receive headers first
    headers_data = b""
    while not headers_data.endswith(b"\r\n\r\n"):
        headers_data += sock.recv(1)
    headers = headers_data.decode('utf-8').split('\r\n')
    content_length = int(headers[0].split(': ')[1])
    
    # Receive the actual message content
    message_data = sock.recv(content_length)
    return json.loads(message_data.decode('utf-8'))
```

