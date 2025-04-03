import React from "react";
import { Routes, Route } from "react-router-dom";
import HomePage from "../Components/HomePage/HomePage";
import LoginPage from "../Components/LoginPage/LoginPage";
import SignupPage from "../Components/SignupPage/SignupPage";
// import Dashboard from "../pages/Dashboard";
// import PrivateRoute from "../components/PrivateRoute";

const CustomRoutes = () => {
    return (
        <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/login" element={<LoginPage />} />
            <Route path="/signup" element={<SignupPage />} />
            <Route path="/dashboard" element={<Dashboard />} />
        </Routes>
    );
};

export default CustomRoutes;
