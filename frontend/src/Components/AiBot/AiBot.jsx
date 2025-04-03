import { useState, useEffect, useRef } from "react";
import { motion } from "framer-motion";
import "./AiBot.css";

const initialQuestions = [
  "What is your name?",
  "What is your age?",
  "What is your gender? (Male/Female/Other)",
  "What is your marital status?",
  "What is your height (in meters)?",
  "What is your weight (in kg)?",
  "Personal history: Are you a smoker or non-smoker?",
  "Alcohol/tobacco use and duration?",
  "Past medical history: Have you had a similar problem in the past or any surgery?",
  "Family history: Do you have a history of cancer, kidney stones, or headaches?",
  "Current complaints (C/C):"
];


const femaleSpecificQuestions = ["Is your menstrual cycle regular or irregular?"];

const AIChat = () => {
  const [messages, setMessages] = useState([]);
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [userResponses, setUserResponses] = useState({});
  const [questions, setQuestions] = useState(initialQuestions);
  const [input, setInput] = useState("");
  const [reportId, setReportId] = useState(null);
  const chatEndRef = useRef(null);

  useEffect(() => {
    if (messages.length === 0) {
      setTimeout(() => {
        setMessages([{ sender: "AI", text: questions[0] }]);
      }, 500);
    }
  }, [questions]);

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const handleSendMessage = () => {
    if (!input.trim()) return;

    const userMessage = { sender: "User", text: input };
    const updatedResponses = { ...userResponses, [questions[currentQuestionIndex]]: input };

    setMessages((prev) => [...prev, userMessage]);
    setUserResponses(updatedResponses);
    setInput("");

    let nextIndex = currentQuestionIndex + 1;

    // Logic to add female-specific questions
    if (currentQuestionIndex === 2) {
      if (input.toLowerCase() === "female" && !questions.includes(femaleSpecificQuestions[0])) {
        setQuestions((prev) => [...prev, ...femaleSpecificQuestions]);
      }
    }

    setTimeout(() => {
      if (nextIndex < questions.length) {
        setMessages((prev) => [...prev, { sender: "AI", text: questions[nextIndex] }]);
        setCurrentQuestionIndex(nextIndex);
      } else {
        setCurrentQuestionIndex(questions.length);
      }
    }, 1000);
  };

  const getCSRFToken = () => {
    const csrfToken = document.cookie
      .split(';')
      .find(cookie => cookie.trim().startsWith('csrftoken='))
      ?.split('=')[1];
    return csrfToken;
  };

  const handleSubmit = async () => {
    const responseFromML = "Predicted Condition: Fever"; // Replace with actual ML model response

    const finalData = {
      // user_id: "12345", // Replace with actual user ID
      responses: userResponses,
      mlResult: responseFromML,
    };

    const csrfToken = getCSRFToken();

    try {
      const res = await fetch("http://127.0.0.1:8000/api/save-consultation/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": csrfToken,  // Include CSRF token in request header
        },
        body: JSON.stringify(finalData),
      });

      if (res.ok) {
        const data = await res.json();
        console.log("API Response:", data);
        if (data.report_id) {
          setReportId(data.report_id);
        } else {
          alert("Error: No report_id received.");
        }
      } else {
        alert("Error submitting the form.");
      }
    } catch (error) {
      console.error("Submission Error:", error);
    }
  };

  return (
    <div id="chatbot-section" className="chat-container">
      <div className="chat-box">
        {messages.map((msg, index) => (
          <motion.div
            key={index}
            className={`message ${msg.sender === "AI" ? "ai-message" : "user-message"}`}
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.3 }}
          >
            {msg.text}
          </motion.div>
        ))}
        <div ref={chatEndRef}></div>
      </div>

      {currentQuestionIndex >= questions.length ? (
        <div className="submit-container">
          <button className="submit-button" onClick={handleSubmit}>
            Submit to doc
          </button>
          {reportId && (
            <a
              href={`http://127.0.0.1:8000/api/generate-report/${reportId}/`}
              target="_blank"
              rel="noopener noreferrer"
            >
              <button className="download-button">Download PDF Report</button>
            </a>
          )}
        </div>
      ) : (
        <div className="input-area">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Type your response..."
          />
          <button onClick={handleSendMessage}>Send</button>
        </div>
      )}
    </div>
  );
};

export default AIChat;
