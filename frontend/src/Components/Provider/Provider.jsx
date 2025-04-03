import React from "react";
import { motion } from "framer-motion";
import "./Provider.css";
import sandeep from "../../assets/sandeep.avif"
import ramesh from "../../assets/ramesh.webp"
import praveen from "../../assets/praveen.webp"
import anshuman from "../../assets/anshuman.jpg"
import rp from "../../assets/RP.jpg"
import neha from "../../assets/neha.jpeg"
import sunil from "../../assets/sunil.jpg"



const doctors = [
    {
        name: "Dr. Anshuman Kaushal",
        specialty: "General Surgeon",
        workplace: "Manipal Hospital, Jaipur",
        email: "anshuman.kaushal@example.com",
        phone: "+91 9012345678",
        photo: anshuman,
      },
      {
        name: "Dr. R.P. Yadav",
        specialty: "Orthopedic Surgeon",
        workplace: "Sawai Man Singh Hospital, Jaipur",
        email: "rp.yadav@example.com",
        phone: "+91 8123456789",
        photo: rp,
      },
      {
        name: "Dr. Sunil Tanwar",
        specialty: "Neurologist",
        workplace: "Neuro Care Clinic, Jaipur",
        email: "sunil.tanwar@example.com",
        phone: "+91 7234567891",
        photo: sunil,
      },
      {
        name: "Dr. Neha Gupta",
        specialty: "Gynecologist",
        workplace: "Apex Hospital, Jaipur",
        email: "neha.gupta@example.com",
        phone: "+91 9015674321",
        photo: neha,
      },
  {
    name: "Dr. Sandeep Jasuja",
    specialty: "Nephrologist",
    workplace: "EHCC Hospital, Jaipur",
    email: "sandeep.jasuja@example.com",
    phone: "+91 9876543210",
    photo: sandeep,
  },
  {
    name: "Dr. Praveen Goyal",
    specialty: "Cardiologist",
    workplace: "Fortis Escorts, Jaipur",
    email: "praveen.goyal@example.com",
    phone: "+91 9234567890",
    photo: praveen,
  },
  {
    name: "Dr. Ramesh Jain",
    specialty: "Oncologist",
    workplace: "Bhagwan Mahaveer Cancer Hospital, Jaipur",
    email: "ramesh.jain@example.com",
    phone: "+91 8765432109",
    photo: ramesh,
  },
];

const Providers = () => {
  return (
    <motion.div className="providers-container">
      {/* Title with fade-in effect */}
      <motion.h2 
        className="providers-title"
        initial={{ opacity: 0, y: -30 }} 
        whileInView={{ opacity: 1, y: 0 }} 
        transition={{ duration: 0.5, ease: "easeOut" }}
        viewport={{ once: true }} // Only triggers animation once
      >
        Our Healthcare Providers
      </motion.h2>

      {/* Doctors List */}
      <div className="providers-grid">
        {doctors.map((doctor, index) => (
          <motion.div 
            key={index} 
            className="doctor-card"
            initial={{ opacity: 0, x: -50 }}  // Slide from left
            whileInView={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.5, ease: "easeOut" }}
            viewport={{ once: true }} // Only animate once when in view
            whileHover={{ scale: 1.05 }}
          >
            <img src={doctor.photo} alt={doctor.name} className="doctor-photo" />
            <div className="doctor-info">
              <div className="doctor-name">{doctor.name}</div>
              <div className="doctor-specialty">{doctor.specialty}</div>
              <div className="doctor-workplace">{doctor.workplace}</div>
              <div className="doctor-contact">
                <a href={`mailto:${doctor.email}`}>{doctor.email}</a> | {doctor.phone}
              </div>
            </div>
          </motion.div>
        ))}
      </div>
    </motion.div>
  );
};

export default Providers;
