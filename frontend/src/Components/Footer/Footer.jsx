import React from "react";
import { Link } from "react-router-dom";
import { motion } from "framer-motion"; // <-- import framer motion
import "./Footer.css";

const Footer = () => {
  return (
    <motion.footer
      className="footer"
      initial={{ opacity: 0, y: 50 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.6 }}
    >
      <div className="footer-container">
        {/* Logo */}
        <motion.div
          className="footer-logo"
          whileHover={{ scale: 1.05 }}
          transition={{ type: "spring", stiffness: 300 }}
        >
          <div className="logo-icon">C</div>
          <Link to={"/home"}><span className="footer-logo-text">CURA</span></Link>
        </motion.div>

        {/* Navigation Links */}
        <div className="footer-links">
          {[
            { to: "/", label: "Home" },
            { to: "/providers", label: "Provider" },
            { to: "/ai-consultation", label: "AI Consultation" },
            { to: "/appointments", label: "Appointment" },
          ].map((link, index) => (
            <motion.div
              key={index}
              whileHover={{ scale: 1.1, color: "teal" }}
              transition={{ type: "spring", stiffness: 300 }}
            >
              <Link to={link.to}>{link.label}</Link>
            </motion.div>
          ))}
        </div>

        {/* Footer bottom text */}
        <motion.div
          className="footer-bottom"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.5, duration: 0.5 }}
        >
          &copy; {new Date().getFullYear()} CURA. All rights reserved.
        </motion.div>
      </div>
    </motion.footer>
  );
};

export default Footer;
