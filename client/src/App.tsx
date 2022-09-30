import { useEffect } from 'react';
import './App.css';

function App() {

  const API = process.env.API_ENDPOINT

  useEffect(() => {
    fetch(API + '/api/test')
      .then(response => response.json())  // convert response to json format
      .then(data => console.log(data));   // log the data to the console

  }, [])

  return (
    <div className="App">
      <header className="App-header">
        <p>
          Edit <code>src/App.tsx</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
