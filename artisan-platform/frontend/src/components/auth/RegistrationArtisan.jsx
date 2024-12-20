import React from "react";
import './RegistrationArtisan.css';

function RegisterArtisan() {
  const handleGoogleLogin = () => {
    console.log("Logging in with Google...");
  };

  const handleFacebookLogin = () => {
    console.log("Logging in with Facebook...");
  };

  return (
    <div className="registration-container">
      <div className="header">
        <h1>سجل كفني</h1>
      </div>

      <div className="container">
        <h1>إنشاء حساب فني جديد</h1>
        <form>
          <input type="text" placeholder="الاسم بالكامل" required />
          <input type="email" placeholder="البريد الإلكتروني" required />
          <input type="password" placeholder="كلمة السر" required />
          <input type="password" placeholder="تأكيد كلمة السر" required />
          <input type="number" placeholder="السن" required />
          <input type="number" placeholder="عدد سنين الخبرة" required />
          <select required>
            <option value="">اختر نوع الحرفة</option>
            <option value="نجار">نجار</option>
            <option value="سباك">سباك</option>
            <option value="كهربائي">كهربائي</option>
            <option value="دهان">دهان</option>
          </select>
          <input type="file" placeholder="رفع صورة البطاقة" />
          <input type="file" placeholder="رفع شهادة الخبرة (إن وجدت)" />
          <input type="text" placeholder="المحافظة" required />
          <input type="text" placeholder="المدينة" required />
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

export default RegisterArtisan;