import { Link } from "react-router-dom";
import { motion } from "framer-motion";
import "./Footer.css";

const Footer = () => {
  return (
    <motion.footer 
      className="footer-container"
      initial={{ opacity: 0, y: 50 }}
      whileInView={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.8, ease: "easeOut" }}
      viewport={{ once: true }}
    >
      <div className="footer-content">
        <div className="footer-brand">
          <span className="footer-brand-name">CURA</span>
          <p className="footer-description">
            Your gateway to telemedicine and AI-powered healthcare solutions.</p>
        </div>

        <div className="footer-services">
          <h3>Services</h3>
          <ul>
            <li><Link to="/providers">Find Providers</Link></li>
            <li><Link to="/ai-consult">AI Consultation</Link></li>
            <li><Link to="/appointments">Schedule Appointment</Link></li>
          </ul>
        </div>
      </div>

      <div className="footer-bottom">
        <p>&copy; {new Date().getFullYear()} CURA. All rights reserved.</p>
      </div>
    </motion.footer>
  );
};

export default Footer;
