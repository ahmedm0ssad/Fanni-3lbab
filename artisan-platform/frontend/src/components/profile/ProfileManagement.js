import React, { useState } from "react";

const ProfileManagement = () => {
  // State to manage form input values
  const [formData, setFormData] = useState({
    fullName: "",
    email: "",
    phoneNumber: "",
    password: "",
    confirmPassword: "",
  });

  // Function to handle input changes
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({ ...prevData, [name]: value }));
  };

  // Function to save changes (placeholder for actual save logic)
  const handleSave = () => {
    alert("تم حفظ التغييرات بنجاح!");
  };

  // Function to reset the form
  const handleCancel = () => {
    setFormData({
      fullName: "",
      email: "",
      phoneNumber: "",
      password: "",
      confirmPassword: "",
    });
    alert("تم إلغاء التغييرات!");
  };

  return (
    <div className="profile-management">
      {/* Page Header */}
      <h1>إدارة الملف الشخصي</h1>

      {/* Profile Picture Section */}
      <div className="profile-picture-section">
        <img
          src="https://via.placeholder.com/100"
          alt="Profile"
          className="profile-picture"
        />
        <button className="btn btn-primary">تغيير صورة الملف الشخصي</button>
      </div>

      {/* Form Title */}
      <h2>تحديث التفاصيل الشخصية</h2>

      {/* Form Section */}
      <form>
        <div className="form-group">
          <label>الاسم ا��كامل</label>
          <input
            type="text"
            name="fullName"
            value={formData.fullName}
            onChange={handleChange}
            className="form-control"
            placeholder="أدخل اسمك الكامل"
          />
        </div>

        <div className="form-group">
          <label>البريد الإلكتروني</label>
          <input
            type="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            className="form-control"
            placeholder="أدخل بريدك الإلكتروني"
          />
        </div>

        <div className="form-group">
          <label>رقم الهاتف</label>
          <input
            type="text"
            name="phoneNumber"
            value={formData.phoneNumber}
            onChange={handleChange}
            className="form-control"
            placeholder="أدخل رقم هاتفك"
          />
        </div>

        <div className="form-group">
          <label>كلمة المرور</label>
          <input
            type="password"
            name="password"
            value={formData.password}
            onChange={handleChange}
            className="form-control"
            placeholder="أدخل كلمة المرور الجديدة"
          />
        </div>

        <div className="form-group">
          <label>تأكيد كلمة المرور</label>
          <input
            type="password"
            name="confirmPassword"
            value={formData.confirmPassword}
            onChange={handleChange}
            className="form-control"
            placeholder="تأكيد كلمة المرور الجديدة"
          />
        </div>

        {/* Buttons */}
        <div className="button-group">
          <button
            type="button"
            className="btn btn-success"
            onClick={handleSave}
          >
            حفظ التغييرات
          </button>
          <button
            type="button"
            className="btn btn-secondary"
            onClick={handleCancel}
          >
            إلغاء
          </button>
        </div>
      </form>
    </div>
  );
};

export default ProfileManagement;