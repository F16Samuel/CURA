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
  "Do you smoke? (Yes/No)",
  "Do you consume alcohol or tobacco? If yes, mention duration.",
  "Have you had similar problems in the past?",
  "Have you undergone any surgery?",
  "Does your family have a history of cancer, kidney stones, or headaches?",
  "What are your current symptoms?",
  "How long have you been experiencing these symptoms?",
  "Do you have any allergies?",
  "Are you currently on any medication?",
];

const femaleSpecificQuestions = [
  "Is your menstrual cycle regular or irregular?",
];

const AIChat = () => {
  const [messages, setMessages] = useState([]);
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [userResponses, setUserResponses] = useState({});
  const [questions, setQuestions] = useState(initialQuestions);
  const [input, setInput] = useState("");
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

    setMessages([...messages, userMessage]);
    setUserResponses(updatedResponses);
    setInput("");

    let nextIndex = currentQuestionIndex + 1;

    if (currentQuestionIndex === 2) {
      // Check gender response and add female-specific questions
      if (input.toLowerCase() === "female") {
        setQuestions((prev) => [...prev, ...femaleSpecificQuestions]);
      }
    }

    if (nextIndex < questions.length) {
      setTimeout(() => {
        setMessages((prev) => [...prev, { sender: "AI", text: questions[nextIndex] }]);
        setCurrentQuestionIndex(nextIndex);
      }, 1000);
    }
  };

  const handleSubmit = async () => {
    const responseFromML = "Predicted Condition: Fever"; // Replace with actual ML model response

    const finalData = {
      responses: userResponses,
      mlResult: responseFromML,
    };

    try {
      const res = await fetch("http://your-backend-url.com/api/submit-consultation", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(finalData),
      });

      if (res.ok) {
        alert("Form submitted successfully to the doctor!");
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

      {currentQuestionIndex < questions.length ? (
        <div className="input-area">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Type your response..."
          />
          <button onClick={handleSendMessage}>Send</button>
        </div>
      ) : (
        <div className="submit-container">
          <button className="submit-button" onClick={handleSubmit}>
            Submit to Doctor
          </button>
        </div>
      )}
    </div>
  );
};

export default AIChat;
