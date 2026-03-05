const http = require("http");
const socketio = require("socket.io");
const axios = require("axios");

const server = http.createServer();
const io = socketio(server, {
  cors: {
    origin: "http://127.0.0.1:8000", // Your Django server URL
    methods: ["GET", "POST"]
  }
});

const port = 3000;
const DJANGO_URL = "http://localhost:8000";

// Store connected users
const users = {};

io.on("connection", (socket) => {
  console.log("User connected:", socket.id);

  // Register user
  socket.on("register", (username) => {
    users[socket.id] = username;
    console.log(`${username} registered`);
    
    // Send list of connected users to everyone
    io.emit("users", Object.values(users));
  });

  // Handle private messages
  socket.on("private message", async ({ to, message }) => {
    const fromUser = users[socket.id];
    
    // Find target socket ID
    const targetSocketId = Object.keys(users).find(
      id => users[id] === to
    );

    // Save to Django
    try {
      await axios.post(`${DJANGO_URL}api/message/`, {
        message: message,
        created_date: new Date().toISOString(),
        from: fromUser,
        to: to
      });
    } catch (error) {
      console.log("Failed to save to Django:", error.message);
    }

    // Send to specific user
    if (targetSocketId) {
      io.to(targetSocketId).emit("private message", {
        from: fromUser,
        message: message,
        timestamp: new Date().toISOString()
      });
    }

    // Confirmation to sender
    socket.emit("message sent", {
      to: to,
      message: message,
      timestamp: new Date().toISOString()
    });
  });

  // Handle disconnection
  socket.on("disconnect", () => {
    if (users[socket.id]) {
      console.log(`${users[socket.id]} disconnected`);
      delete users[socket.id];
      io.emit("users", Object.values(users));
    }
  });
});

server.listen(port, () => {
  console.log(`Socket.io server running on port ${port}`);
});