import React from 'react';
import {
  FaSearch,
  FaHome,
  FaMapMarkerAlt,
  FaHeart,
  FaUser,
  FaUserCircle,
  FaBell, // Import the bell icon for notifications
} from 'react-icons/fa';
import { useNavigate } from 'react-router-dom';
import './Home.css';

// Import Images
import cerpsImage from '../../assets/cerps.jpg';
import plumImage from '../../assets/plum.jpg';
import elecImage from '../../assets/elec.jpg';
import painterImage from '../../assets/painter.jpg';
import recImage from '../../assets/rec.jpg';
import rec2Image from '../../assets/rec2.jpg';
import rec3Image from '../../assets/rec3.jpg';

// Main Component
function Home() {
  const navigate = useNavigate();

  return (
    <div className="home-container">
      {/* Header Section */}
      <Header navigate={navigate} />

      {/* Search Button Section */}
      <div className="search-button-container">
        <button className="search-button" onClick={() => navigate('/search')}>بحث عن خدمة</button>
      </div>

      {/* Categories Section */}
      <Categories />

      {/* Top Rated Professionals Section */}
      <TopRated />

      {/* Footer Section */}
      <Footer navigate={navigate} />
    </div>
  );
}

// Header Component
const Header = ({ navigate }) => (
  <header className="header">
    <h2 className="title">فني ع الباب</h2>
    <div className="header-buttons">
      <button className="register-button" onClick={() => navigate('/registration')}>التسجيل</button>
      <button className="login-button" onClick={() => navigate('/login')}>تسجيل الدخول</button>
      <button className="favorites-button" onClick={() => navigate('/favorites')}>المفضلة</button>
      <button className="search-button" onClick={() => navigate('/search')}>بحث عن خدمة</button>
      <button className="order-history-button" onClick={() => navigate('/order-history')}>تاريخ الطلبات</button>
      <button className="notifications-button" onClick={() => navigate('/notifications')}>الإشعارات</button>
      <FaSearch size={20} color="#555" />
      <button className="profile-button" onClick={() => navigate('/profile')}>Profile</button>
      <FaUserCircle size={20} color="#555" />
      <FaBell size={20} color="#555" onClick={() => navigate('/notifications')} />
    </div>
  </header>
);

// Categories Component
const Categories = () => (
  <section>
    <h3 className="section-title">الفئه</h3>
    <div className="categories-container">
      {categoriesData.map((category, index) => (
        <Category key={index} image={category.image} name={category.name} />
      ))}
    </div>
  </section>
);

const Category = ({ image, name }) => (
  <div className="category">
    <img src={image} alt={name} className="category-image" />
    <p>{name}</p>
  </div>
);

// Top Rated Professionals Component
const TopRated = () => (
  <section>
    <h3 className="section-title">الأعلى تقييمًا في منطقتك</h3>
    <div className="top-rated-container">
      {[recImage, rec2Image, rec3Image].map((image, index) => (
        <img key={index} src={image} alt={`Professional ${index + 1}`} className="professional-image" />
      ))}
    </div>
  </section>
);

// Footer Component
const Footer = ({ navigate }) => (
  <footer className="footer">
    <FaHome size={20} />
    <FaMapMarkerAlt size={20} />
    <FaHeart size={20} onClick={() => navigate('/favorites')} className="favorites-button" />
    <FaUser size={20} />
  </footer>
);

// Categories Data
const categoriesData = [
  { image: plumImage, name: 'سباك' },
  { image: cerpsImage, name: 'نجار' },
  { image: elecImage, name: 'فني كهرباء' },
  { image: painterImage, name: 'فني دهان' },
];

export default Home;
