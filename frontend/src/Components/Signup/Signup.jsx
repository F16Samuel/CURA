import { useState } from "react";
import { motion } from "framer-motion";
import "./Signup.css";

const Signup = () => {
  const [role, setRole] = useState(null); // 'doctor' or 'patient'
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    password: "",
    hospital: "", // Only for doctors
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const endpoint = role === "doctor" ? "/api/register/doctor" : "/api/register/patient";

    try {
      const response = await fetch(endpoint, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData),
      });

      if (!response.ok) {
        throw new Error("Registration failed");
      }

      const result = await response.json();
      alert(`Success: ${result.message}`);
      setFormData({ name: "", email: "", password: "", hospital: "" });
      setRole(null); // Reset form
    } catch (error) {
      alert("Error: " + error.message);
    }
  };

  return (
    <div className="register-container">
      {!role ? (
        <div className="register-options">
          <motion.button
            className="btn-primary"
            whileHover={{ scale: 1.05 }}
            onClick={() => setRole("patient")}
          >
            Register as Patient
          </motion.button>
          <motion.button
            className="btn-outline"
            whileHover={{ scale: 1.05 }}
            onClick={() => setRole("doctor")}
          >
            Register as Doctor
          </motion.button>
        </div>
      ) : (
        <motion.form
          className="register-form"
          onSubmit={handleSubmit}
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.3 }}
        >
          <h2>Register as {role === "doctor" ? "Doctor" : "Patient"}</h2>
          <input
            type="text"
            name="name"
            placeholder="Full Name"
            value={formData.name}
            onChange={handleChange}
            required
          />
          <input
            type="email"
            name="email"
            placeholder="Email Address"
            value={formData.email}
            onChange={handleChange}
            required
          />
          <input
            type="password"
            name="password"
            placeholder="Password"
            value={formData.password}
            onChange={handleChange}
            required
          />
          {role === "doctor" && (
            <input
              type="text"
              name="hospital"
              placeholder="Currently working at"
              value={formData.hospital}
              onChange={handleChange}
              required
            />
          )}
          <motion.button
            type="submit"
            className="btn-primary"
            whileHover={{ scale: 1.05 }}
          >
            Register
          </motion.button>
          <motion.button
            className="btn-outline"
            whileHover={{ scale: 1.05 }}
            onClick={() => setRole(null)}
            type="button"
          >
            Back
          </motion.button>
        </motion.form>
      )}
    </div>
  );
};

export default Signup;
