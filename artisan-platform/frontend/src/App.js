import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./components/home/Home";
import Registration from "./components/auth/Registration";
import Login from './components/auth/Login';
import FavoritesPage from './components/customer/FavoritesPage';
import SearchPage from './components/search/SearchPage';
import PortfolioManager from './components/artisan/PortfolioManager';
import ProfileManagement from './components/profile/ProfileManagement';
import ServiceRequest from './components/customer/ServiceRequest'; // استيراد صفحة طلب الخدمة
import BookingPage from './components/customer/BookingPage'; // استيراد صفحة الحجز
import OrderHistory from './components/customer/OrderHistory'; // استيراد صفحة تاريخ الطلبات
import NotificationPage from './components/customer/NotificationPage'; // استيراد صفحة الإشعارات

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/registration" element={<Registration />} />
        <Route path="/login" element={<Login />} />
        <Route path="/favorites" element={<FavoritesPage />} />
        <Route path="/search" element={<SearchPage />} />
        <Route path="/portfolio" element={<PortfolioManager />} />
        <Route path="/profile" element={<ProfileManagement />} />
        <Route path="/service-request" element={<ServiceRequest />} /> {/* إضافة مسار صفحة طلب الخدمة */}
        <Route path="/booking" element={<BookingPage />} /> {/* إضافة مسار صفحة الحجز */}
        <Route path="/order-history" element={<OrderHistory />} /> {/* إضافة مسار صفحة تاريخ الطلبات */}
        <Route path="/notifications" element={<NotificationPage />} /> {/* إضافة مسار صفحة الإشعارات */}
      </Routes>
    </Router>
  );
}

export default App;
