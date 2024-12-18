import React from "react";
import './Registration.css';

function Register() {
  const handleGoogleLogin = () => {
    console.log("Logging in with Google...");
  };

  const handleFacebookLogin = () => {
    console.log("Logging in with Facebook...");
  };

  return (
    <div className="registration-container">
      <div className="header">
        <h1>سجل هنا</h1>
      </div>

      <div className="container">
        <h1>إنشاء حساب جديد</h1>
        <form>
          <input type="text" placeholder="الاسم بالكامل" required />
          <input type="email" placeholder="البريد الإلكتروني" required />
          <input type="password" placeholder="كلمة السر" required />
          <input type="password" placeholder="تأكيد كلمة السر" required />
          <button type="submit">تسجيل</button>
        </form>
        <div className="divider">
          <span>أو</span>
        </div>
        <div className="third-party-btns">
          <button onClick={handleGoogleLogin} className="google-btn">
            التسجيل باستخدام Google
          </button>
          <button onClick={handleFacebookLogin} className="facebook-btn">
            التسجيل باستخدام Facebook
          </button>
        </div>
      </div>
    </div>
  );
}

export default Register;
