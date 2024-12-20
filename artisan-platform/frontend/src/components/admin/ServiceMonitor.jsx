import React from "react";

const ServiceMonitoringPage = () => {
  const serviceRequests = [
    { id: 1, name: "Woodwork Service", status: "Pending", date: "15-12-2024" },
    { id: 2, name: "Interior Painting", status: "In Progress", date: "18-12-2024" },
    { id: 3, name: "Landscaping", status: "Completed", date: "10-12-2024" },
    {id: 4, name:"plumbing", status:"cancelled", date:"13-12-2024"},
  ];

  const bookings = [
    { id: 1, customer: "John Doe", service: "Woodwork", date: "2024-12-20", status: "Confirmed" },
    { id: 2, customer: "Jane Smith", service: "Interior Painting", date: "2024-12-22", status: "Pending" },
    {id: 3, customer: "Aisla Anderson", service:"electric work", date: "28-11-2024", status:"Finished"} 
  ];

  return (
    <div style={{ fontFamily: "Arial, sans-serif", padding: "20px" }}>
      <h1 style={{ textAlign: "center" }}>Service Monitoring Page</h1>

      {/* Service Requests Section */}
      <section style={{ marginBottom: "20px" }}>
        <h2>Service Requests</h2>
        <div style={{ display: "flex", flexDirection: "column", gap: "10px" }}>
          {serviceRequests.map((request) => (
            <div
              key={request.id}
              style={{
                display: "flex",
                justifyContent: "space-between",
                alignItems: "center",
                padding: "10px",
                border: "1px solid #ddd",
                borderRadius: "5px",
                backgroundColor: "#f9f9f9",
              }}
            >
              <span>{request.name}</span>
              <span>{request.status}</span>
              <span>{request.date}</span>
            </div>
          ))}
        </div>
      </section>

      {/* Bookings Section */}
      <section>
        <h2>Bookings</h2>
        <table style={{ width: "100%", borderCollapse: "collapse" }}>
          <thead>
            <tr style={{ backgroundColor: "#f3f3f3" }}>
              <th style={tableHeaderStyle}>Customer</th>
              <th style={tableHeaderStyle}>Service</th>
              <th style={tableHeaderStyle}>Date</th>
              <th style={tableHeaderStyle}>Status</th>
            </tr>
          </thead>
          <tbody>
            {bookings.map((booking) => (
              <tr key={booking.id}>
                <td style={tableCellStyle}>{booking.customer}</td>
                <td style={tableCellStyle}>{booking.service}</td>
                <td style={tableCellStyle}>{booking.date}</td>
                <td style={tableCellStyle}>{booking.status}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </section>
    </div>
  );
};

const tableHeaderStyle = {
  textAlign: "left",
  padding: "10px",
  borderBottom: "2px solid #ddd",
};

const tableCellStyle = {
  padding: "10px",
  borderBottom: "1px solid #ddd",
};

export default ServiceMonitoringPage;
