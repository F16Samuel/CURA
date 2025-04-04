import AIChat from "../AiBot/AiBot";
import AIConsultationHeader from "../AIConsultationHeader/AIConsultationHeader";
import Navbar from "../Navbar/Navbar"
import Footer from "../Footer/Footer";

function AiPage(){
    return(
        <div>
            <Navbar/>
            <AIConsultationHeader/>
            <AIChat/>
            <Footer/>
        </div>
    )
}

export default AiPage;