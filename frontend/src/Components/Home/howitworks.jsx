import React from "react";
import { Link } from "react-router-dom";
import "./howitworks.css";

const ConsultationBanner = () => {
  return (
    <div className="consultation-banner">
      <h1>AI Consultation</h1>
      <p>
        Get an AI-powered preliminary health assessment by answering a few simple questions.
      </p>
      <Link to="/ai-consultation" className="consultation-btn">
        Start Consultation
      </Link>
    </div>
  );
};

export default ConsultationBanner;
