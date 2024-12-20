import React from 'react';

const AdminDashboard = () => {
  return (
    <div style={{ fontFamily: 'Arial, sans-serif', padding: '20px' }}>
      <h1 style={{ textAlign: 'center' }}>Admin Dashboard</h1>

      <section style={{ display: 'flex', justifyContent: 'space-around', marginBottom: '20px' }}>
        <div style={statBoxStyle}>
          <h3>Total Artisans</h3>
          <p>50</p>
        </div>
        <div style={statBoxStyle}>
          <h3>Total Customers</h3>
          <p>100</p>
        </div>
        <div style={statBoxStyle}>
          <h3>Total Services</h3>
          <p>30</p>
        </div>
        <div style={statBoxStyle}>
          <h3>Pending Bookings</h3>
          <p>20</p>
        </div>
      </section>

      <section style={{ marginBottom: '20px' }}>
        <h2>Platform Management</h2>
        <ul style={{ listStyleType: 'none', padding: 0 }}>
          <li style={listItemStyle}>
            User Management
            <button style={manageButtonStyle}>Go</button>
          </li>
          <li style={listItemStyle}>
            Service Management
            <button style={manageButtonStyle}>Go</button>
          </li>
          <li style={listItemStyle}>
            Reports and Analytics
            <button style={manageButtonStyle}>Go</button>
          </li>
        </ul>
      </section>

      <section>
        <h2>Recent Activities</h2>
        <ul style={{ listStyleType: 'none', padding: 0 }}>
          <li style={listItemStyle}>John Doe added a new service - Landscaping</li>
          <li style={listItemStyle}>Jane Smith updated her profile</li>
          <li style={listItemStyle}>Michael Brown completed a booking - Woodwork</li>
        </ul>
      </section>
    </div>
  );
};

const statBoxStyle = {
  border: '1px solid #ccc',
  borderRadius: '5px',
  padding: '20px',
  textAlign: 'center',
  width: '22%',
  backgroundColor: '#f9f9f9',
};

const listItemStyle = {
  display: 'flex',
  justifyContent: 'space-between',
  alignItems: 'center',
  padding: '10px',
  borderBottom: '1px solid #ddd',
};

const manageButtonStyle = {
  backgroundColor: 'blue',
  color: 'white',
  border: 'none',
  padding: '5px 10px',
  borderRadius: '5px',
  cursor: 'pointer',
};

export default AdminDashboard;
