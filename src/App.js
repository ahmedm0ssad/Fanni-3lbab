import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./components/home/Home";
import Registration from "./components/auth/Registration";
import Login from './components/auth/Login';
import FavoritesPage from './components/customer/FavoritesPage'; // Import the FavoritesPage component
import SearchPage from './components/search/SearchPage'; // Import the SearchPage component
import PortfolioManager from './components/artisan/PortfolioManager'; // Import the PortfolioManager component
import ProfileManagement from './components/profile/ProfileManagement'; // Import the ProfileManagement component

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/registration" element={<Registration />} />
        <Route path="/login" element={<Login />} />
        <Route path="/favorites" element={<FavoritesPage />} /> {/* Add the FavoritesPage route */}
        <Route path="/search" element={<SearchPage />} /> {/* Add the SearchPage route */}
        <Route path="/portfolio" element={<PortfolioManager />} /> {/* Add the PortfolioManager route */}
        <Route path="/profile" element={<ProfileManagement />} /> {/* Add the ProfileManagement route */}
      </Routes>
    </Router>
  );
}

export default App;
