import React from "react";
import { motion } from "framer-motion";
import "./AIConsultationHeader.css";

const AIConsultationHeader = () => {
  const handleStart = () => {
    const chatbotSection = document.getElementById("chatbot-section");
    if (chatbotSection) {
      chatbotSection.scrollIntoView({ behavior: "smooth" });
    }
  };

  return (
    <div className="ai-consultation-header">
      <motion.h1
        className="header-title"
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
      >
        AI Consultation
      </motion.h1>

      <motion.p
        className="header-description"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.3, duration: 0.5 }}
      >
        Get an AI-powered preliminary health assessment by answering a few simple questions.
      </motion.p>

      <motion.button
        className="start-btn"
        onClick={handleStart}
        whileHover={{ scale: 1.05 }}
      >
        Start Consultation
      </motion.button>
    </div>
  );
};

export default AIConsultationHeader;
