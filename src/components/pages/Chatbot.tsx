//random
import React, { useState } from 'react';
import axios from 'axios';

const Chatbot = () => {
    const [chatHistory, setChatHistory] = useState([]);
    const [message, setMessage] = useState('');

    const sendMessage = async () => {
        if (message.trim() === '') return;

        const userMessage = { role: 'user', content: message };
        const newChatHistory = [...chatHistory, userMessage];

        try {
            const response = await axios.post('http://localhost:5000/chat', {
                message: message,
                chat_history: newChatHistory
            });

            const assistantReply = response.data.assistant_reply;
            setChatHistory([...newChatHistory, { role: 'assistant', content: assistantReply }]);
            setMessage('');
        } catch (error) {
            console.error("Error sending message:", error);
        }
    };

    return (
        <div>
            <div>
                {chatHistory.map((msg, index) => (
                    <div key={index} className={msg.role === 'user' ? 'user-message' : 'assistant-message'}>
                        {msg.content}
                    </div>
                ))}
            </div>
            <input
                type="text"
                value={message}
                onChange={(e) => setMessage(e.target.value)}
                placeholder="Type your message..."
            />
            <button onClick={sendMessage}>Send</button>
        </div>
    );
};

export default Chatbot;
