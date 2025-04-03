import React from 'react';
import './App.css'
import CustomRoutes from './Routes/CustomRoutes';
import { AuthProvider } from './context/AuthContext';

function App() {
  return (
    <AuthProvider>
      <CustomRoutes />
    </AuthProvider>

  );
}

export default App
