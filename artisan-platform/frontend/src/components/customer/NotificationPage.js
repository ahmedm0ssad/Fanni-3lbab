import React from "react";
import "./NotificationPage.css";

const NotificationPage = () => {
  const notifications = [
    { id: 1, message: "تم تأكيد حجزك للخدمة." },
    { id: 2, message: "تذكير: يرجى تقديم ملاحظاتك حول الخدمة." },
    // يمكنك إضافة المزيد من الإشعارات هنا
  ];

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

export default NotificationPage;