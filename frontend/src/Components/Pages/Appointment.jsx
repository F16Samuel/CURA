import React from "react";
import DoctorView from "../DoctorAppointment/DoctorAppointment";
import PatientView from "../PatientAppointment/PatientAppointment";
import "./Appointment.css"; // Import CSS file
import Navbar from "../Navbar/Navbar"
import Footer from "../Footer/Footer";

const AppointmentPage = ({ userType }) => {
  return (
    <div>
        <Navbar/>
        <div className="appointment-container">
        <h2 className="appointment-heading">
            {userType === "doctor" ? "Doctor's Dashboard" : "Patient's Dashboard"}
        </h2>

        {/* Render different views based on userType */}
        {userType === "doctor" ? <DoctorView /> : <PatientView />}
        </div>
        <Footer/>
    </div>
  );
};

export default AppointmentPage;
