    const socket = io();

    // Define the room name
    const room = "{{ doctor.username }}_{{ current_user.username }}";
    console.log('Joining room:', room);
    socket.emit('join_room', room);

    // Debug connection
    socket.on('connect', () => {
        console.log('Connected to WebSocket server');
    });

    // Handle received messages
    socket.on('receive_message', function(data) {
        console.log('Message received:', data);
        const chatHistory = document.getElementById('chat-history');
        chatHistory.innerHTML += `<p><strong>${data.user}:</strong> ${data.message}</p>`;
        chatHistory.scrollTop = chatHistory.scrollHeight;
    });

    // Handle send button click
    document.getElementById('send-btn').addEventListener('click', function() {
        const messageInput = document.getElementById('message');
        const message = messageInput.value;
        if (message.trim()) {
            console.log('Sending message:', message);
            socket.emit('send_message', { room: room, message: message });
            messageInput.value = '';
        }
    });

    // Handle Enter key press
    document.getElementById('message').addEventListener('keypress', function(event) {
        if (event.key === 'Enter') {
            event.preventDefault();
            document.getElementById('send-btn').click();
        }
    });

    // Handle errors
    socket.on('error', function(data) {
        console.error('Error:', data.msg);
    });
