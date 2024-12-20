import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './Login.css';

const Login = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleLogin = (e) => {
    e.preventDefault();
    // محاكاة عملية تسجيل الدخول
    if (email === 'admin@gmail.com' && password === '0000') {
      navigate('/adminhome');
    } else if (email === 'user1@example.com' && password === 'password1') {
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
        <a href="/forgot-password" className="forgot-password-link">نسيت كلمة المرور؟</a>
        <a href="/loginartisan" className="artisan-login-link">تسجيل الدخول كفني</a>
        <a href="/registration" className="register-link">التسجيل</a>
      </div>
    </div>
  );
};

export default Login;
