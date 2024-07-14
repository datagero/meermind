import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import './App.css';
import Dashboard from './pages/Dashboard';
import Upload from './pages/Upload';
import ResponsiveAppBar from './components/ResponsiveAppBar';
import NotePage from './pages/NotePage';

function App() {
  return (
    <React.Fragment>
        <ResponsiveAppBar />
        <Routes>
         <Route path="/" element={<Dashboard/>} />
        <Route path="/upload" element={<Upload/>} />
        <Route path="note/:id" element={<NotePage />}
        />
       </Routes>
    </React.Fragment>
  );
}

export default App;
