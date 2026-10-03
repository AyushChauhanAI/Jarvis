from fastapi import APIRouter, WebSocket, WebSocketDisconnect

router = APIRouter()


@router.websocket("/voicechat")
async def voicechat(websocket: WebSocket):
    print("Request received")
    await websocket.accept()
    print("WebSocket connected!")

    try:
        while True:
            audio_chunk = await websocket.receive_bytes()
            print(len(audio_chunk))
            await websocket.send_json({"status": "received"})
    except WebSocketDisconnect:
        print("Client disconnected")