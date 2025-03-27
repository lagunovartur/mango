import React, {useEffect, useState} from 'react';
import {io} from 'socket.io-client';
import './Chat.css'

import {Message} from './Message';


export const Chat = ({isLogged}) => {

    const [socket, setSocket] = useState(null);
    const [isConnected, setIsConnected] = useState(false);
    const [messages, setMessages] = useState([]);
    const [message, setMessage] = useState('');

    useEffect(() => {
        if (isLogged && !socket) {
            const socket = io(process.env.REACT_APP_API_URL, {
                path: process.env.REACT_APP_WS_PATH,
            });
            setSocket(socket);
            console.log('Logged in!!!!!!!!!!!!!!');

            socket.on('connect', () => {
                setIsConnected(socket.connected);
            });

            socket.on('disconnect', () => {
                setIsConnected(socket.connected);
            });

            socket.on('join', (data) => {
                setMessages((prevMessages) => [...prevMessages, {...data, type: 'join'}]);
            });

            socket.on('chat', (data) => {
                setMessages((prevMessages) => [...prevMessages, {...data, type: 'chat'}]);
            });

        }

    }, [isLogged, socket]);

    return (
        <>
            <div className="chat">


                <h2>status: {isConnected ? 'connected' : 'disconnected'}</h2>

                <div className="dialog">
                    {messages.map((message, index) => (
                        <Message message={message} key={index}/>
                    ))}
                </div>
                <input
                    type={'text'}
                    id='message'
                    onChange={(event) => {
                        const value = event.target.value.trim();
                        setMessage(value);
                    }}
                ></input>
                <button
                    onClick={() => {
                        if (message && message.length) {
                            socket.emit('chat', message);
                        }
                        var messageBox = document.getElementById('message');
                        messageBox.value = '';
                        setMessage('');
                    }}
                >
                    Send
                </button>
            </div>
        </>
    );
};
