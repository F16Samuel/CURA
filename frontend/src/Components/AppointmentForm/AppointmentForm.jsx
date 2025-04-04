import React, { useState } from "react";
import "../Pages/Appointment.css";

const AppointmentForm = ({ onClose }) => {
  const [formData, setFormData] = useState({
    doctor: "",
    date: "",
    time: "",
    reason: "",
    virtual: false
  });

  const [charCount, setCharCount] = useState(0);
  const maxChar = 200; // Character limit for reason field

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;

    if (name === "reason" && value.length > maxChar) return;

    setFormData({
      ...formData,
      [name]: type === "checkbox" ? checked : value
    });

    if (name === "reason") setCharCount(value.length);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!formData.doctor || !formData.date || !formData.time || !formData.reason) {
      alert("Please fill in all required fields.");
      return;
    }
    console.log("Appointment Request:", formData);
    onClose();
  };

  return (
    <div className="appointment-form-container">
      <h2 className="form-title">Request a New Appointment</h2>
      <form onSubmit={handleSubmit}>
        {/* Doctor Selection */}
        <div className="form-group">
          <label className="label">Select Doctor</label>
          <select
            name="doctor"
            className="select-field"
            value={formData.doctor}
            onChange={handleChange}
            required
          >
            <option value="" disabled>Select a doctor</option>
            <option value="dr-naresh-trehan">Dr. Naresh Trehan - Cardiologist</option>
            <option value="dr-devi-shetty">Dr. Devi Shetty - Cardiac Surgeon</option>
            <option value="dr-ramakant-panda">Dr. Ramakant Panda - Cardiac Surgeon</option>
            <option value="dr-mukesh-goel">Dr. Mukesh Goel - Orthopedic Surgeon</option>
            <option value="dr-randeep-guleria">Dr. Randeep Guleria - Pulmonologist</option>
            <option value="dr-ajay-aggarwal">Dr. Ajay Aggarwal - Endocrinologist</option>
            <option value="dr-sanjay-kumar">Dr. Sanjay Kumar - Neurologist</option>
            <option value="dr-sneha-mehta">Dr. Sneha Mehta - Dermatologist</option>
            <option value="dr-rajat-gupta">Dr. Rajat Gupta - Plastic Surgeon</option>
            <option value="dr-neha-sharma">Dr. Neha Sharma - Gynecologist</option>
          </select>
        </div>

        {/* Preferred Date */}
        <div className="form-group">
          <label className="label">Preferred Date</label>
          <input
            type="date"
            name="date"
            className="input-field"
            value={formData.date}
            onChange={handleChange}
            required
          />
        </div>

        {/* Preferred Time */}
        <div className="form-group">
          <label className="label">Preferred Time</label>
          <select
            name="time"
            className="select-field"
            value={formData.time}
            onChange={handleChange}
            required
          >
            <option value="" disabled>Select a time</option>
            <option value="morning">Morning (9 AM - 12 PM)</option>
            <option value="afternoon">Afternoon (1 PM - 5 PM)</option>
            <option value="evening">Evening (6 PM - 9 PM)</option>
          </select>
        </div>

        {/* Reason for Visit */}
        <div className="form-group">
          <label className="label">Reason for Visit</label>
          <textarea
            name="reason"
            className="textarea-field"
            value={formData.reason}
            onChange={handleChange}
            required
            placeholder="Briefly describe your symptoms..."
          ></textarea>
          <p className="char-count">{charCount}/{maxChar} characters</p>
        </div>

        {/* Virtual Consultation Checkbox */}
        <div className="checkbox-group">
          <input
            type="checkbox"
            name="virtual"
            checked={formData.virtual}
            onChange={handleChange}
          />
          <span>I prefer a virtual consultation if available</span>
        </div>

        {/* Buttons */}
        <div className="button-group">
          <button type="button" className="button cancel-button" onClick={onClose}>
            Cancel
          </button>
          <button type="submit" className="button submit-button">
            Submit Request
          </button>
        </div>
      </form>
    </div>
  );
};

export default AppointmentForm;
