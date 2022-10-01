import { useEffect } from 'react';
import './App.css';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from './pages/home';
import GetRoute from './pages/route';

function App() {

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
