import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import './App.css';
import Dashboard from './pages/Dashboard';
import Upload from './pages/Upload';

function App() {
  return (
    <div className="App">
        <Link to="/">Home</Link>
        <Link to="/upload">Upload</Link>
        <Routes>
         <Route path="/" element={<Dashboard/>} />
        <Route path="/upload" element={<Upload/>} />
       </Routes>
    </div>
  );
}

export default App;
