import React from 'react';
import './ForgotPassword.css'; // Import CSS for styling

const ForgotPassword = () => {
  return (
    <div className="forgot-password-container">
      <div className="left-side">
        <img
          src="https://via.placeholder.com/400x300"
          alt="Login Illustration"
          className="illustration"
        />
      </div>

      <div className="right-side">
        <h1>Forgot Your Password?</h1>
        <p className="subtitle">Enter your email address to receive a reset link.</p>
        <form className="reset-form">
          <input
            type="email"
            placeholder="Enter your email"
            required
            className="email-input"
          />
          <button type="submit" className="reset-button">
            SEND RESET LINK
          </button>
        </form>
        <a href="/login" className="back-link">
          Back to SIGN IN
        </a>
      </div>
    </div>
  );
};

export default ForgotPassword;
