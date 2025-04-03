import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import "./Navbar.css";

const Navbar = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const toggleMenu = () => {
    setIsMenuOpen(!isMenuOpen);
  };

  return (
    <motion.header
      className="navbar"
      initial={{ y: -100, opacity: 0 }}
      animate={{ y: 0, opacity: 1 }}
      transition={{ duration: 0.6, ease: "easeOut" }}
    >
      <div className="container">
        {/* Logo */}
        <a href="#" className="logo">
          <motion.span 
            className="logo-icon"
            initial={{ opacity: 0, scale: 0.5 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 0.5 }}
          >
            C
          </motion.span>
          <motion.span 
            className="logo-text"
            initial={{ x: -50, opacity: 0 }}
            animate={{ x: 0, opacity: 1 }}
            transition={{ duration: 0.5 }}
          >
            CURA
          </motion.span>
        </a>

        {/* Navigation Links (Desktop) */}
        <nav className="nav-links">
          {["Home", "Providers", "AI Consultation", "Appointments"].map((item, index) => (
            <motion.a
              key={index}
              href="#"
              className="nav-item"
              whileHover={{ scale: 1.1, color: "#50BFA5" }}
              transition={{ type: "spring", stiffness: 300 }}
            >
              {item}
            </motion.a>
          ))}
        </nav>

        {/* Authentication Buttons */}
        <div className="auth-buttons">
          <motion.a href="#" className="btn-outline" whileHover={{ scale: 1.05 }}>Sign in</motion.a>
          <motion.a href="#" className="btn-primary" whileHover={{ scale: 1.05 }}>Sign up</motion.a>
        </div>

        {/* Mobile Menu Button */}
        <button className="menu-toggle" onClick={toggleMenu} aria-label="Toggle menu">
          {isMenuOpen ? "✖" : "☰"}
        </button>
      </div>

      {/* Mobile Menu */}
      <AnimatePresence>
        {isMenuOpen && (
          <motion.div 
            className="mobile-menu"
            initial={{ opacity: 0, y: -20 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -20 }}
            transition={{ duration: 0.3 }}
          >
            <nav className="mobile-nav">
              {["Home", "Providers", "AI Consultation", "Appointments"].map((item, index) => (
                <motion.a
                  key={index}
                  href="#"
                  className="mobile-nav-item"
                  onClick={toggleMenu}
                  whileHover={{ scale: 1.1, color: "#50BFA5" }}
                  transition={{ type: "spring", stiffness: 300 }}
                >
                  {item}
                </motion.a>
              ))}
              <a href="#" className="btn-outline mobile-btn" onClick={toggleMenu}>Sign in</a>
              <a href="#" className="btn-primary mobile-btn" onClick={toggleMenu}>Sign up</a>
            </nav>
          </motion.div>
        )}
      </AnimatePresence>
    </motion.header>
  );
};

export default Navbar;
