import { Chat } from './Chat';
import {Login} from "./Login";

function App() {
  return (
      <>
          <div style={{ display: 'flex', flexDirection: 'column', padding: '50px', width: '50%' }}>
              <h1>Socket.io app</h1>
              <Login/>
              <Chat/>
          </div>
      </>
  );
}

export default App;
