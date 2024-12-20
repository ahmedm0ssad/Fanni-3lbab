import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import './UserDetails.css';

const UserDetails = () => {
  const { email } = useParams();
  const [userData, setUserData] = useState(null);

  useEffect(() => {
    // جلب بيانات المستخدم من الخادم
    fetch(`/api/users/${email}`)
      .then(response => response.json())
      .then(data => setUserData(data));
  }, [email]);

  if (!userData) {
    return <div>Loading...</div>;
  }

  return (
    <div className="user-details-container">
      <h1>تفاصيل المستخدم</h1>
      <p>الاسم: {userData.name}</p>
      <p>البريد الإلكتروني: {userData.email}</p>
      <p>العنوان: {userData.address}</p>
      <p>رقم الهاتف: {userData.phone}</p>
      {/* أضف المزيد من التفاصيل حسب الحاجة */}
    </div>
  );
};

export default UserDetails;