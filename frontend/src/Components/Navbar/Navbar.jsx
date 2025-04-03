import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { motion, AnimatePresence } from "framer-motion";
import "./Navbar.css";

const Navbar = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [user, setUser] = useState(null);

  // Fetch user data from backend on mount
  useEffect(() => {
    const fetchUser = async () => {
      const token = localStorage.getItem("access_token");  // Retrieve token from localStorage
      if (!token) {
        console.warn("No access token found");
        return;
      }

      try {
        const response = await fetch("http://localhost:8000/current-user/", {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${token}`,  // Attach token for authentication
          },
          credentials: "include",
        });

        if (!response.ok) throw new Error(`Failed to fetch user data, Status: ${response.status}`);

        const userData = await response.json();
        setUser(userData);
        localStorage.setItem("user", JSON.stringify(userData)); // Store user in localStorage
      } catch (error) {
        console.error("Error fetching user:", error);
        setUser(null);
      }
    };

    fetchUser();
  }, []);

  // Toggle mobile menu
  const toggleMenu = () => {
    setIsMenuOpen(!isMenuOpen);
  };

  // Logout function
  const handleLogout = async () => {
    try {
      const token = localStorage.getItem("access_token");
      await fetch("http://localhost:8000/api/logout/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        credentials: "include",
      });

      localStorage.removeItem("user");
      localStorage.removeItem("access_token");
      setUser(null);
    } catch (error) {
      console.error("Error logging out:", error);
    }
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
          <motion.span className="logo-icon" initial={{ opacity: 0, scale: 0.5 }} animate={{ opacity: 1, scale: 1 }} transition={{ duration: 0.5 }}>
            C
          </motion.span>
          <motion.span className="logo-text" initial={{ x: -50, opacity: 0 }} animate={{ x: 0, opacity: 1 }} transition={{ duration: 0.5 }}>
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

        {/* Authentication Section */}
        <div className="auth-buttons">
          {user ? (
            <>
              <motion.div className="welcome-msg">Welcome, {user.username}</motion.div>
              <motion.button className="btn-outline" onClick={handleLogout} whileHover={{ scale: 1.05 }}>
                Logout
              </motion.button>
            </>
          ) : (
            <>
              <motion.div whileHover={{ scale: 1.05 }}>
                <Link to="/login" className="btn-outline">Log in</Link>
              </motion.div>
              <motion.div whileHover={{ scale: 1.05 }}>
                <Link to="/signup" className="btn-primary">Sign up</Link>
              </motion.div>
            </>
          )}
        </div>

        {/* Mobile Menu Button */}
        <button className="menu-toggle" onClick={toggleMenu} aria-label="Toggle menu">
          {isMenuOpen ? "✖" : "☰"}
        </button>
      </div>

      {/* Mobile Menu */}
      <AnimatePresence>
        {isMenuOpen && (
          <motion.div className="mobile-menu" initial={{ opacity: 0, y: -20 }} animate={{ opacity: 1, y: 0 }} exit={{ opacity: 0, y: -20 }} transition={{ duration: 0.3 }}>
            <nav className="mobile-nav">
              {["Home", "Providers", "AI Consultation", "Appointments"].map((item, index) => (
                <motion.div key={index} whileHover={{ scale: 1.1, color: "#50BFA5" }} transition={{ type: "spring", stiffness: 300 }}>
                  <Link to={`/${item.toLowerCase().replace(/\s+/g, "-")}`} className="mobile-nav-item" onClick={toggleMenu}>
                    {item}
                  </Link>
                </motion.div>
              ))}

              {user ? (
                <>
                  <motion.div className="welcome-msg">Welcome, {user.username}</motion.div>
                  <button className="btn-outline mobile-btn" onClick={() => { handleLogout(); toggleMenu(); }}>
                    Logout
                  </button>
                </>
              ) : (
                <>
                  <Link to="/login" className="btn-outline mobile-btn" onClick={toggleMenu}>Log in</Link>
                  <Link to="/signup" className="btn-primary mobile-btn" onClick={toggleMenu}>Sign up</Link>
                </>
              )}
            </nav>
          </motion.div>
        )}
      </AnimatePresence>
    </motion.header>
  );
};

export default Navbar;
