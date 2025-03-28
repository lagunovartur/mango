import React, {useState} from 'react';
import './Login.css'


export const Login = ({setIsLogged, isLogged}) => {
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
                credentials: "include",
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(creds),
            });

            if (!resp.ok) {
                // Если сервер вернул ошибку
                throw new Error('Login failed!');
            }
            setIsLogged(true);

            const json = await resp.json();
            console.log('Login successful:', json);

        } catch (error) {
            console.error('Error:', error);
        }
    };


    const  onLogout = async () => {
        try {
            const resp = await fetch(process.env.REACT_APP_API_URL + '/auth/logout', {
                method: 'POST',
                credentials: "include",
                headers: {
                    'Content-Type': 'application/json',
                },
            });

            if (!resp.ok) {
                throw new Error('Logout failed!');
            }
            setIsLogged(false);

            console.log('Logout successful:');

        } catch (error) {
            console.error('Error:', error);
        }
    };

    return (
        <>
            <div className="container">
                <div className="blocked" style={{ pointerEvents: !isLogged ? 'auto' : 'none', opacity: !isLogged ? 1 : 0.5 }}>
                    <input type={'text'} id="username" placeholder={"username"}
                           onChange={(e) => setUsername(e.target.value)}></input>
                    <input type={'password'} id='password' placeholder={"password"}
                           onChange={(e) => setPassword(e.target.value)}></input>
                    <button className="btn" onClick={onLogin}>Login</button>
                </div>
                <button className="btn" onClick={onLogout}>Logout</button>
            </div>
        </>
    );
};
