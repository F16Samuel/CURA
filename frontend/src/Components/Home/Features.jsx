import React from "react";
import { HeartPulse, Stethoscope, Calendar, Brain } from "lucide-react";
import "./Features.css";

const features = [
  {
    title: "AI-Powered Diagnostics",
    description: "Get preliminary assessments using our advanced medical AI technology.",
    icon: Brain,
  },
  {
    title: "Connect with Specialists",
    description: "Easily find and connect with healthcare specialists in your area.",
    icon: Stethoscope,
  },
  {
    title: "Detailed Health Report",
    description: "Get a detailed PDF of your symptoms and possible diagnosis.",
    icon: HeartPulse,
  },
  {
    title: "Easy Scheduling",
    description: "Book appointments with healthcare providers in just a few clicks.",
    icon: Calendar,
  },
];

const Features = () => {
  return (
    <div className="features-section">
      <h2 className="features-title">Why Choose Cura</h2>
      <div className="features-grid">
        {features.map((feature, index) => (
          <div key={index} className="feature-card">
            <div className="feature-icon">
              <feature.icon size={30} />
            </div>
            <h3 className="feature-title">{feature.title}</h3>
            <p className="feature-description">{feature.description}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Features;
