import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import './ArtisanDetails.css';

const ArtisanDetails = () => {
  const { email } = useParams();
  const [artisanData, setArtisanData] = useState(null);

  useEffect(() => {
    // جلب بيانات الفني من الخادم
    fetch(`/api/artisans/${email}`)
      .then(response => response.json())
      .then(data => setArtisanData(data));
  }, [email]);

  if (!artisanData) {
    return <div>Loading...</div>;
  }

  return (
    <div className="artisan-details-container">
      <h1>تفاصيل الفني</h1>
      <p>الاسم: {artisanData.name}</p>
      <p>البريد الإلكتروني: {artisanData.email}</p>
      <p>العنوان: {artisanData.address}</p>
      <p>رقم الهاتف: {artisanData.phone}</p>
      <p>عدد سنوات الخبرة: {artisanData.experienceYears}</p>
      <p>نوع الحرفة: {artisanData.craftType}</p>
      {/* أضف المزيد من التفاصيل حسب الحاجة */}
    </div>
  );
};

export default ArtisanDetails;