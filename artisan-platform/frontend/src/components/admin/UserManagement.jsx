import React from 'react';

const UserManagementPage = () => {
  const customers = [
    { id: 1, name: 'John Doe', email: 'john@gmail.com' },
    { id: 2, name: 'Andre Smith', email: 'andre@gmail.com' },
    { id: 3, name: 'Adam Taylor', email: 'adam56@gmail.com' },
  ];

  const artisans = [
    { id: 1, name: 'Michael Brown', email: 'michael@gmail.com' },
    { id: 2, name: 'Emily Davis', email: 'emily@gmail.com' },
    { id: 3, name: 'Ashley Daniels', email: 'ash658@gmail.com' },
  ];

  return (
    <div style={{ fontFamily: 'Arial, sans-serif', padding: '20px' }}>
      <h1 style={{ textAlign: 'center' }}>User Management</h1>

      <section style={{ marginBottom: '20px' }}>
        <h2>Customer Accounts</h2>
        <ul style={{ listStyleType: 'none', padding: 0 }}>
          {customers.map((customer) => (
            <li key={customer.id} style={listItemStyle}>
              <span style={{ flex: 1 }}>{customer.name} - {customer.email}</span>
              <div style={{ display: 'flex', gap: '5px' }}>
                <button style={editButtonStyle}>Edit</button>
                <button style={deleteButtonStyle}>Delete</button>
              </div>
            </li>
          ))}
        </ul>
      </section>

      <section>
        <h2>Artisan Accounts</h2>
        <ul style={{ listStyleType: 'none', padding: 0 }}>
          {artisans.map((artisan) => (
            <li key={artisan.id} style={listItemStyle}>
              <span style={{ flex: 1 }}>{artisan.name} - {artisan.email}</span>
              <div style={{ display: 'flex', gap: '5px' }}>
                <button style={editButtonStyle}>Edit</button>
                <button style={deleteButtonStyle}>Delete</button>
              </div>
            </li>
          ))}
        </ul>
      </section>
    </div>
  );
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

export default UserManagementPage;
