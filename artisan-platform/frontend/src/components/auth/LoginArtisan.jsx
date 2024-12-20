import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './LoginArtisan.css';

const LoginArtisan = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleLogin = (e) => {
    e.preventDefault();
    // محاكاة عملية تسجيل الدخول
    if ((email === 'artisan' && password === '0000') || (email === 'admin@gmail.com' && password === '0000')) {
      navigate('/artisanhome');
    } else {
      alert('Invalid credentials. Please try again.');
    }
  };

  return (
    <div className="login-container">
      <div className="header">
        <h1>تسجيل الدخول كفني</h1>
      </div>
      <div className="container">
        <h1>تسجيل الدخول كفني</h1>
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
        <a href="/registerartisan" className="register-link">التسجيل</a>
      </div>
    </div>
  );
};

export default LoginArtisan;