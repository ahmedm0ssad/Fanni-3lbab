import React, { useState } from 'react';
import './Login.css';

const Login = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = (e) => {
    e.preventDefault();
    // محاكاة عملية تسجيل الدخول
    if (email === 'user1@example.com' && password === 'password1') {
      alert('Login successful! Welcome, user1!');
    } else if (email === 'user2@example.com' && password === 'password2') {
      alert('Login successful! Welcome, user2!');
    } else {
      alert('Invalid credentials. Please try again.');
    }
  };

  return (
    <div className="login-container">
      <div className="header">
        <h1>تسجيل الدخول</h1>
      </div>
      <div className="container">
        <h1>تسجيل الدخول</h1>
        <form onSubmit={handleLogin}>
          <input
            type="email"
            placeholder="البريد الإلكتروني"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
          <input
            type="password"
            placeholder="كلمة السر"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
          <button type="submit">تسجيل الدخول</button>
        </form>
      </div>
    </div>
  );
};

export default Login;
