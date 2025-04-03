import React from "react";
import "../Pages/Appointment.css"; // Import CSS file

const DoctorView = () => {
  return (
    <div className="doctor-container">
      <h3 className="section-heading">Upcoming Appointments</h3>
      {/* TODO: Fetch appointments from Django API */}
      <div className="box">
        <p>No upcoming appointments.</p>
      </div>

      <h3 className="section-heading">Patient Reports</h3>
      {/* TODO: Fetch patient reports from Django API */}
      <div className="box">
        <p>No reports available.</p>
      </div>
    </div>
  );
};

export default DoctorView;
