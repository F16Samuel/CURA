import { Route , Routes } from "react-router-dom";
import SignupPage from "../Components/Pages/Signup_page";


function CustomRoutes(){
    return(
        <Routes>
            <Route path="SignUp" element = {<SignupPage/>}/>
        </Routes>
    );
}

export default CustomRoutes;