import AIChat from "../AiBot/AiBot";
import AIConsultationHeader from "../AIConsultationHeader/AIConsultationHeader";
import Navbar from "../Navbar/Navbar"

function AiPage(){
    return(
        <div>
            <Navbar/>
            <AIConsultationHeader/>
            <AIChat/>
        </div>
    )
}

export default AiPage;