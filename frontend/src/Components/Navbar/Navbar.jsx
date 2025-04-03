import { useState, useEffect } from "react";
import { Link, useNavigate } from "react-router-dom";
import { motion, AnimatePresence } from "framer-motion";
import "./Navbar.css";

const Navbar = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [user, setUser] = useState(null);
  const navigate = useNavigate();

  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.startsWith(name + "=")) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }

  useEffect(() => {
    const fetchUser = async () => {
      try {
        const response = await fetch("http://localhost:8000/get_user/", {
          method: "GET",
          credentials: "include",
          headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCookie("csrftoken"),
            "Authorization": `Bearer ${localStorage.getItem("token")}`
          },
        });

        if (response.status === 401) {
          setUser(null);
          localStorage.removeItem("user");
          return;
        }

        if (!response.ok) {
          throw new Error("Failed to fetch user data");
        }

        const userData = await response.json();
        setUser(userData);
        localStorage.setItem("user", JSON.stringify(userData));
      } catch (error) {
        console.error("Error fetching user:", error);
        setUser(null);
      }
    };

    fetchUser();
  }, []);

  const handleLogout = async () => {
    try {
      const response = await fetch("http://localhost:8000/logout/", {
        method: "POST",
        credentials: "include",
        headers: {
          "X-CSRFToken": getCookie("csrftoken"),
        },
      });

      if (response.ok) {
        setUser(null);
        localStorage.removeItem("user");
        localStorage.removeItem("token");
        navigate("/");
      } else {
        console.error("Logout failed");
      }
    } catch (error) {
      console.error("Error:", error);
    }
  };

  const toggleMenu = () => {
    setIsMenuOpen(!isMenuOpen);
  };

  return (
    <motion.header className="navbar" initial={{ y: -100, opacity: 0 }} animate={{ y: 0, opacity: 1 }} transition={{ duration: 0.6, ease: "easeOut" }}>
      <div className="container">
        <Link to="/" className="logo">
          <motion.span className="logo-icon" initial={{ opacity: 0, scale: 0.5 }} animate={{ opacity: 1, scale: 1 }} transition={{ duration: 0.5 }}>C</motion.span>
          <motion.span className="logo-text" initial={{ x: -50, opacity: 0 }} animate={{ x: 0, opacity: 1 }} transition={{ duration: 0.5 }}>CURA</motion.span>
        </Link>

        <nav className="nav-links">
          {["Home", "Providers", "AI Consultation", "Appointments"].map((item, index) => (
            <motion.div key={index} whileHover={{ scale: 1.1, color: "#50BFA5" }} transition={{ type: "spring", stiffness: 300 }}>
              <Link to={`/${item.toLowerCase().replace(/\s+/g, "-")}`} className="nav-item">{item}</Link>
            </motion.div>
          ))}
        </nav>

        <div className="auth-buttons">
          {user ? (
            <>
              <motion.div className="welcome-msg">Welcome, {user.username}</motion.div>
              <motion.button onClick={handleLogout} className="btn-logout" whileHover={{ scale: 1.1 }}>Logout</motion.button>
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

        <button className="menu-toggle" onClick={toggleMenu} aria-label="Toggle menu">
          {isMenuOpen ? "✖" : "☰"}
        </button>
      </div>
    </motion.header>
  );
};

export default Navbar;
