const ws = new WebSocket('ws://127.0.0.1:8000/ws/status/');

ws.addEventListener("open", (event) => {
    console.log("Connected");
})

ws.addEventListener("close", (event) => {
    console.log("Disconnected");
})