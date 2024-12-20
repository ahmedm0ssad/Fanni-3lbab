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
import ForgotPassword from './components/auth/ForgotPassword'; // استيراد صفحة نسيت كلمة المرور
import LoginArtisan from './components/auth/LoginArtisan'; // استيراد صفحة تسجيل الدخول كفني
import RegisterArtisan from './components/auth/RegistrationArtisan'; // استيراد صفحة تسجيل الفني
import ArtisanHome from './components/artisan/ArtisanHome'; // استيراد صفحة الفني الرئيسية
import ArtisanNotificationPage from './components/artisan/ArtisanNotificationPage'; // استيراد صفحة إشعارات الفني
import AdminHome from './components/admin/AdminHome'; // استيراد صفحة الإدارة
import UserDetails from './components/admin/UserDetails'; // استيراد صفحة تفاصيل المستخدم
import ArtisanDetails from './components/admin/ArtisanDetails'; // استيراد صفحة تفاصيل الفني

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
        <Route path="/forgot-password" element={<ForgotPassword />} /> {/* إضافة مسار صفحة نسيت كلمة المرور */}
        <Route path="/loginartisan" element={<LoginArtisan />} /> {/* إضافة مسار صفحة تسجيل الدخول كفني */}
        <Route path="/registerartisan" element={<RegisterArtisan />} /> {/* إضافة مسار صفحة تسجيل الفني */}
        <Route path="/artisanhome" element={<ArtisanHome />} /> {/* إضافة مسار صفحة الفني الرئيسية */}
        <Route path="/artisannotifications" element={<ArtisanNotificationPage />} /> {/* إضافة مسار صفحة إشعارات الفني */}
        <Route path="/adminhome" element={<AdminHome />} /> {/* إضافة مسار صفحة الإدارة */}
        <Route path="/userdetails/:email" element={<UserDetails />} /> {/* إضافة مسار صفحة تفاصيل المستخدم */}
        <Route path="/artisandetails/:email" element={<ArtisanDetails />} /> {/* إضافة مسار صفحة تفاصيل الفني */}
      </Routes>
    </Router>
  );
}

export default App;