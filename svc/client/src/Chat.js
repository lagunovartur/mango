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
            console.log('start ws connecting');
            const newSocket = io(process.env.REACT_APP_API_URL, {
                path: process.env.REACT_APP_WS_PATH,
            });
            setSocket(newSocket);


            newSocket.on('connect', () => {
                setIsConnected(newSocket.connected);
                console.log('WS Connected!!!!!!!!!!!!!!!!!!');
            });

            newSocket.on('disconnect', () => {
                setIsConnected(newSocket.connected);
            });

            newSocket.on('join', (data) => {
                setMessages((prevMessages) => [...prevMessages, {...data, type: 'join'}]);
            });

            newSocket.on('chat', (data) => {
                setMessages((prevMessages) => [...prevMessages, {...data, type: 'chat'}]);
            });

        }

        if (!isLogged && socket) {
            socket.disconnect();
            setSocket(null);  // Обнуляем сокет
            console.log('Socket disconnected due to logout');
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
