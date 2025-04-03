import { Route , Routes } from "react-router-dom";
import SignupPage from "../Components/Pages/Signup_page";
import Home from "../Components/Pages/Home";
import LoginPage from "../Components/Pages/Login_page"
import AiPage from "../Components/Pages/AiPage";


function CustomRoutes() {
    return (
        <Routes>
            <Route path="/" element = {<Home/>}/>
            <Route path="/home" element = {<Home/>}/>
            <Route path="SignUp" element = {<SignupPage/>}/>
            <Route path="Login" element = {<LoginPage/>}/>
            <Route path="ai-consultation" element = {<AiPage/>}/>

        </Routes>
    );
};

export default CustomRoutes;
