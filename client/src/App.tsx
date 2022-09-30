import { useEffect } from 'react';
import './App.css';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from './pages/home';
import GetRoute from './pages/route';

const API = process.env.REACT_APP_API_ENDPOINT

function App() {

  useEffect(() => {
    fetch(API + '/api/test')
      .then(response => response.json())  // convert response to json format
      .then(data => console.log(data));   // log the data to the console
  }, [])

  return (
    <>
        <Router>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/route" element={<GetRoute />} />
        </Routes>
        </Router>
    </>
  );
}

export default App;
