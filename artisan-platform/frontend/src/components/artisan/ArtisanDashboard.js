import React from 'react';

const Dashboard = () => {
  const services = [
    { id: 1, name: 'Woodwork Services' },
    { id: 2, name: 'Interior Painting' },
    { id: 3, name: 'Landscaping' },
    { id: 4, name: 'Plumbing' },
  ];

  const bookings = [
    { id: 1, customer: 'John Doe', service: 'Woodwork' },
    { id: 2, customer: 'Jane Smith', service: 'Interior Painting' },
    { id: 3, customer: 'Aisla Anderson', service: 'Electric Work' },
  ];

  return (
    <div style={{ fontFamily: 'Arial, sans-serif', padding: '20px' }}>
      <h1 style={{ textAlign: 'center' }}>Artisan Dashboard</h1>

      <section style={{ display: 'flex', justifyContent: 'space-around', marginBottom: '20px' }}>
        <div style={statBoxStyle}>
          <h3>Total Services</h3>
          <p>10</p>
        </div>
        <div style={statBoxStyle}>
          <h3>Pending Bookings</h3>
          <p>3</p>
        </div>
        <div style={statBoxStyle}>
          <h3>Completed Jobs</h3>
          <p>20</p>
        </div>
      </section>

      <section style={{ marginBottom: '20px' }}>
        <h2>Manage Your Services</h2>
        <ul style={{ listStyleType: 'none', padding: 0 }}>
          {services.map((service) => (
            <li key={service.id} style={listItemStyle}>
              <span style={{ flex: 1 }}>{service.name}</span>
              <div style={{ display: 'flex', gap: '10px' }}>
                <button style={editButtonStyle}>Edit</button>
                <button style={deleteButtonStyle}>Delete</button>
              </div>
            </li>
          ))}
        </ul>
      </section>

      <section>
        <h2>Recent Bookings</h2>
        <ul style={{ listStyleType: 'none', padding: 0 }}>
          {bookings.map((booking) => (
            <li key={booking.id} style={listItemStyle}>
              <span style={{ flex: 1 }}>{booking.customer} - Service: {booking.service}</span>
              <button style={detailsButtonStyle}>View Details</button>
            </li>
          ))}
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
  width: '30%',
  backgroundColor: '#f9f9f9',
};

const listItemStyle = {
  display: 'flex',
  justifyContent: 'space-between',
  alignItems: 'center',
  padding: '10px',
  borderBottom: '1px solid #ddd',
};

const editButtonStyle = {
  backgroundColor: 'purple',
  color: 'white',
  border: 'none',
  padding: '5px 10px',
  borderRadius: '5px',
  cursor: 'pointer',
};

const deleteButtonStyle = {
  backgroundColor: 'red',
  color: 'white',
  border: 'none',
  padding: '5px 10px',
  borderRadius: '5px',
  cursor: 'pointer',
};

const detailsButtonStyle = {
  backgroundColor: 'blue',
  color: 'white',
  border: 'none',
  padding: '5px 10px',
  borderRadius: '5px',
  cursor: 'pointer',
};

export default Dashboard;
