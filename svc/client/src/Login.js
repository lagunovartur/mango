import React, {useState} from 'react';
import './Login.css'


export const Login = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const  onLogin = async () => {

        const creds = {
            username: username,
            password: password,
        };

        try {
            const resp = await fetch(process.env.REACT_APP_API_URL + '/auth/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(creds),
            });

            if (!resp.ok) {
                // Если сервер вернул ошибку
                throw new Error('Login failed!');
            }

            const json = await resp.json();
            console.log('Login successful:', json);

        } catch (error) {
            console.error('Error:', error);
        }
    };


    return (
        <>
            <div className="container">
                <div className="form-group">
                    <label htmlFor='username'>login</label>
                    <input type={'text'} id="username" onChange={(e) => setUsername(e.target.value)}></input>
                </div>
                <div className="">
                    <label htmlFor='password'>password</label>
                    <input type={'text'} id='password' onChange={(e) => setPassword(e.target.value)}></input>
                </div>
                <button className="btn btn-primary" onClick={onLogin}>Login</button>
            </div>
        </>
    );
};
