import { useState } from "react";
import { Link } from "react-router-dom";
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
        <Link to="/" className="logo">
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
        </Link>

        {/* Navigation Links (Desktop) */}
        <nav className="nav-links">
          {["Home", "Providers", "AI Consultation", "Appointments"].map((item, index) => (
            <motion.div key={index} whileHover={{ scale: 1.1, color: "#50BFA5" }} transition={{ type: "spring", stiffness: 300 }}>
              <Link to={`/${item.toLowerCase().replace(/\s+/g, "-")}`} className="nav-item">
                {item}
              </Link>
            </motion.div>
          ))}
        </nav>

        {/* Authentication Buttons */}
        <div className="auth-buttons">
          <motion.div whileHover={{ scale: 1.05 }}>
            <Link to="/Login" className="btn-outline">Log in</Link>
          </motion.div>
          <motion.div whileHover={{ scale: 1.05 }}>
            <Link to="/signup" className="btn-primary">Sign up</Link>
          </motion.div>
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
                <motion.div key={index} whileHover={{ scale: 1.1, color: "#50BFA5" }} transition={{ type: "spring", stiffness: 300 }}>
                  <Link to={`/${item.toLowerCase().replace(/\s+/g, "-")}`} className="mobile-nav-item" onClick={toggleMenu}>
                    {item}
                  </Link>
                </motion.div>
              ))}
              <Link to="/signin" className="btn-outline mobile-btn" onClick={toggleMenu}>Sign in</Link>
              <Link to="/signup" className="btn-primary mobile-btn" onClick={toggleMenu}>Sign up</Link>
            </nav>
          </motion.div>
        )}
      </AnimatePresence>
    </motion.header>
  );
};

export default Navbar;
