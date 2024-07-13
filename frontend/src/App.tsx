import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import './App.css';
import Dashboard from './pages/Dashboard';
import Upload from './pages/Upload';
import ResponsiveAppBar from './components/ResponsiveAppBar';

function App() {
  return (
    <React.Fragment>
        <ResponsiveAppBar />
        <Routes>
         <Route path="/" element={<Dashboard/>} />
        <Route path="/upload" element={<Upload/>} />
       </Routes>
    </React.Fragment>
  );
}

export default App;
