import React, {useEffect, useState} from 'react';
import {io} from 'socket.io-client';
import './Chat.css'

import {Message} from './Message';


export const Chat = ({isLogged}) => {

    const [socket, setSocket] = useState(null);
    const [chatId, setChatId] = useState('');
    const [isConnected, setIsConnected] = useState(false);
    const [messages, setMessages] = useState([]);
    const [message, setMessage] = useState('');

    useEffect(() => {

        if (isLogged && !socket) {
            console.log('start ws connecting', process.env.REACT_APP_SERVER_URL, process.env.REACT_APP_WS_PATH,);
            const newSocket = io(process.env.REACT_APP_SERVER_URL, {
                path: process.env.REACT_APP_WS_PATH,
                secure: true,
                transports: ['websocket'],
                rejectUnauthorized: false,
                autoConnect: false,
            });

            setSocket(newSocket);
            newSocket.connect()
            console.log('end ws connecting');

            newSocket.on('connect', () => {
                setIsConnected(newSocket.connected);
            });

            newSocket.on('disconnect', () => {
                setIsConnected(newSocket.connected);
            });

            newSocket.on('srv_new_message', (data) => {
                console.log(data);
                setMessages((prevMessages) => [...prevMessages, data]);
            });

            // newSocket.on('srv_new_message', (data) => {
            //     setMessages((prevMessages) => [...prevMessages, {...data, type: 'chat'}]);
            // });

        }

        if (!isLogged && socket) {
            socket.disconnect();
            setSocket(null);  // Обнуляем сокет
            console.log('Socket disconnected due to logout');
        }

    }, [isLogged, socket]);

    return (
        <>
            <div className="chat" style={{ pointerEvents: isConnected ? 'auto' : 'none', opacity: isConnected ? 1 : 0.5 }}>
                <h2>status: {isConnected ? 'connected' : 'disconnected'}</h2>

                <input
                    type={'text'}
                    id='chatId'
                    onChange={(event) => {
                        const value = event.target.value.trim();
                        setChatId(value);
                    }}
                    placeholder={'chat_id'}
                />

                <div className="dialog">
                    {messages.map((message, index) => (
                        <Message message={message} key={index}/>
                    ))}
                </div>


                <input
                    type={'text'}
                    placeholder={'message'}
                    id='message'
                    onChange={(event) => {
                        const value = event.target.value.trim();
                        setMessage(value);
                    }}
                />

                <button
                    className='send-btn'
                    onClick={() => {
                        if (message && message.length) {
                            socket.emit('cl_new_message', {'text': message, 'chat_id': chatId});
                        }
                        const messageBox = document.getElementById('message');
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
