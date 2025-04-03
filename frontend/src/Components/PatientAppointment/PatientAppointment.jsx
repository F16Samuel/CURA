import React, { useState } from "react";
import { motion, AnimatePresence } from "framer-motion"; // Import Framer Motion
import "../Pages/Appointment.css"; // Import CSS file
import AppointmentForm from "../AppointmentForm/AppointmentForm";

const PatientView = () => {
  const [showForm, setShowForm] = useState(false);
  const [activeTab, setActiveTab] = useState("scheduled");

  // Mock upcoming appointments (Replace with API data later)
  const upcomingAppointments = [
    { id: 1, doctor: "Dr. Rajesh Sharma", specialty: "Cardiologist", date: "May 10, 2025", time: "9:00 AM" },
    { id: 2, doctor: "Dr. Priya Mehta", specialty: "Dermatologist", date: "May 11, 2025", time: "11:30 AM" },
    { id: 3, doctor: "Dr. Anil Verma", specialty: "Neurologist", date: "May 13, 2025", time: "2:15 PM" }
  ];

  return (
    <div className="patient-container">
      <motion.h2 className="appointment-heading" initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ duration: 0.5 }}>
        Appointments
      </motion.h2>

      {/* Tab navigation */}
      <div className="tab-container">
        {["scheduled", "requests", "past"].map((tab) => (
          <motion.button
            key={tab}
            className={activeTab === tab ? "tab active" : "tab"}
            onClick={() => setActiveTab(tab)}
            whileHover={{ scale: 1.1 }}
            whileTap={{ scale: 0.9 }}
          >
            {tab.charAt(0).toUpperCase() + tab.slice(1)}
          </motion.button>
        ))}
      </div>

      {/* Tab Content Animation */}
      <AnimatePresence mode="wait">
        {activeTab === "scheduled" && (
          <motion.div 
            key="scheduled" 
            initial={{ opacity: 0, y: 20 }} 
            animate={{ opacity: 1, y: 0 }} 
            exit={{ opacity: 0, y: -20 }} 
            transition={{ duration: 0.3 }}
          >
            <h3 className="section-heading">Your Upcoming Appointments</h3>
            {upcomingAppointments.length > 0 ? (
              <table className="appointment-table">
                <thead>
                  <tr>
                    <th>Doctor</th>
                    <th>Specialty</th>
                    <th>Date</th>
                    <th>Time</th>
                  </tr>
                </thead>
                <tbody>
                  {upcomingAppointments.map((appointment) => (
                    <motion.tr key={appointment.id} whileHover={{ scale: 1.02 }} transition={{ duration: 0.2 }}>
                      <td>{appointment.doctor}</td>
                      <td>{appointment.specialty}</td>
                      <td>{appointment.date}</td>
                      <td>{appointment.time}</td>
                    </motion.tr>
                  ))}
                </tbody>
              </table>
            ) : (
              <div className="box">
                <p>No upcoming appointments.</p>
              </div>
            )}
          </motion.div>
        )}
      </AnimatePresence>

      {/* Request Appointment Button */}
      <motion.button
        className="request-btn"
        onClick={() => setShowForm(true)}
        whileHover={{ scale: 1.1 }}
        whileTap={{ scale: 0.9 }}
      >
        Request an Appointment
      </motion.button>

      {/* Appointment Request Form Animation */}
      <AnimatePresence>
        {showForm && (
          <motion.div
            key="appointment-form"
            initial={{ scale: 0.8, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            exit={{ scale: 0.8, opacity: 0 }}
            transition={{ duration: 0.3 }}
          >
            <AppointmentForm onClose={() => setShowForm(false)} />
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
};

export default PatientView;
