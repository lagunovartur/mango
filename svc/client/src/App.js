import {Chat} from './Chat';
import {Login} from "./Login";
import {useState} from "react";

function App() {
    const [isLogged, setIsLogged] = useState(false);

    return (
        <>
            <div style={{display: 'flex', flexDirection: 'column', padding: '50px', width: '50%'}}>
                <h1>Socket.io app</h1>
                <Login setIsLogged={setIsLogged}/>
                <Chat isLogged={isLogged}/>
            </div>
        </>
    );
}

export default App;
