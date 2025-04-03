import React from "react";
import { Link } from "react-router-dom";
import "./hero.css";
import hero from "../../assets/hero.jpeg"

const HeroSection = () => {
  return (
    <div className="hero-container">
      <div className="hero-content">
        <div className="hero-text">
          <h1>
            Your Health, <span className="highlight">AI</span>-Enhanced
          </h1>
          <p>
            Experience the future of healthcare with Cura's AI-powered medical consultations and seamless provider appointments.
          </p>
          <div className="hero-buttons">
            <Link to="/ai-consultation" className="primary-btn">
              Try AI Consultation
            </Link>
            <Link to="/providers" className="secondary-btn">
              Find Providers
            </Link>
          </div>
        </div>
        <div className="hero-image">
          <img src={hero} alt="Cura AI Healthcare" />
        </div>
      </div>
    </div>
  );
};

export default HeroSection;
