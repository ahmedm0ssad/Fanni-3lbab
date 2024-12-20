import React, { useState, useEffect } from "react";
import "./ArtisanNotificationPage.css";

const ArtisanNotificationPage = () => {
  const [notifications, setNotifications] = useState([]);

  useEffect(() => {
    // جلب الإشعارات من الخادم
    fetch('/api/notifications')
      .then(response => response.json())
      .then(data => setNotifications(data));
  }, []);

  return (
    <div className="notification-container">
      <h1>الإشعارات</h1>
      <ul>
        {notifications.map((notification) => (
          <li key={notification.id}>{notification.message}</li>
        ))}
      </ul>
    </div>
  );
};

export default ArtisanNotificationPage;