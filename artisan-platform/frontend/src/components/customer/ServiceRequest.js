import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./ServiceRequest.css";

const ServiceRequest = () => {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    service: "",
    description: "",
  });
  const navigate = useNavigate();

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({ ...prevData, [name]: value }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // هنا يمكنك إضافة منطق إرسال البيانات إلى الخادم
    alert("تم إرسال طلب الخدمة بنجاح!");

    // إرسال إشعار للفني
    fetch('/api/notifications', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        user_id: 1, // معرف الفني
        message: `طلب خدمة جديد: ${formData.service}`,
        is_read: false,
      }),
    });

    navigate('/search'); // توجيه المستخدم إلى صفحة البحث بعد تقديم الطلب بنجاح
  };

  return (
    <div className="service-request-container">
      <h1>طلب خدمة</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="name"
          placeholder="الاسم"
          value={formData.name}
          onChange={handleChange}
          required
        />
        <input
          type="email"
          name="email"
          placeholder="البريد الإلكتروني"
          value={formData.email}
          onChange={handleChange}
          required
        />
        <input
          type="text"
          name="service"
          placeholder="نوع الخدمة"
          value={formData.service}
          onChange={handleChange}
          required
        />
        <textarea
          name="description"
          placeholder="وصف الخدمة المطلوبة"
          value={formData.description}
          onChange={handleChange}
          required
        />
        <button type="submit">إرسال الطلب</button>
      </form>
    </div>
  );
};

export default ServiceRequest;