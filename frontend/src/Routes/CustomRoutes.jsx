import { Route , Routes } from "react-router-dom";
import Home from "../Components/Home/Home";
import Login from "../Components/Login/Login";


function CustomRoutes(){
    return(
        <Routes>
            <Route path="/" element = {<Login/>}/>
        </Routes>
    );
}

export default CustomRoutes;