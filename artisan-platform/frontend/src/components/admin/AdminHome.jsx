import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { Line, Bar, Pie, Doughnut } from 'react-chartjs-2';
import 'chart.js/auto';
import './AdminHome.css';

const AdminHome = () => {
  const [searchEmail, setSearchEmail] = useState('');
  const navigate = useNavigate();

  const handleSearchUser = () => {
    navigate(`/userdetails/${searchEmail}`);
  };

  const handleSearchArtisan = () => {
    navigate(`/artisandetails/${searchEmail}`);
  };

  const [userData, setUserData] = useState([]);
  const [artisanData, setArtisanData] = useState([]);
  const [revenueData, setRevenueData] = useState([]);
  const [activeProvincesData, setActiveProvincesData] = useState([]);

  useEffect(() => {
    // Fetch data from the server
    fetch('/api/admin/user-stats')
      .then(response => response.json())
      .then(data => setUserData(data));

    fetch('/api/admin/artisan-stats')
      .then(response => response.json())
      .then(data => setArtisanData(data));

    fetch('/api/admin/revenue-stats')
      .then(response => response.json())
      .then(data => setRevenueData(data));

    fetch('/api/admin/active-provinces-stats')
      .then(response => response.json())
      .then(data => setActiveProvincesData(data));
  }, []);

  const artisanChartData = {
    labels: artisanData.map(data => data.month),
    datasets: [
      {
        label: 'نسبة الفنيين',
        data: artisanData.map(data => data.percentage),
        backgroundColor: [
          'rgba(255, 99, 132, 0.6)',
          'rgba(54, 162, 235, 0.6)',
          'rgba(255, 206, 86, 0.6)',
          'rgba(75, 192, 192, 0.6)',
          'rgba(153, 102, 255, 0.6)',
          'rgba(255, 159, 64, 0.6)',
        ],
        borderColor: [
          'rgba(255, 99, 132, 1)',
          'rgba(54, 162, 235, 1)',
          'rgba(255, 206, 86, 1)',
          'rgba(75, 192, 192, 1)',
          'rgba(153, 102, 255, 1)',
          'rgba(255, 159, 64, 1)',
        ],
        borderWidth: 1,
      },
    ],
  };

  const revenueChartData = {
    labels: revenueData.map(data => data.month),
    datasets: [
      {
        label: 'الإيرادات',
        data: revenueData.map(data => data.amount),
        backgroundColor: 'rgba(75, 192, 192, 0.6)',
        borderColor: 'rgba(75, 192, 192, 1)',
        borderWidth: 1,
      },
    ],
  };

  const activeProvincesChartData = {
    labels: activeProvincesData.map(data => data.province),
    datasets: [
      {
        label: 'أكثر المحافظات نشاطًا',
        data: activeProvincesData.map(data => data.count),
        backgroundColor: [
          'rgba(255, 99, 132, 0.6)',
          'rgba(54, 162, 235, 0.6)',
          'rgba(255, 206, 86, 0.6)',
          'rgba(75, 192, 192, 0.6)',
          'rgba(153, 102, 255, 0.6)',
          'rgba(255, 159, 64, 0.6)',
        ],
        borderColor: [
          'rgba(255, 99, 132, 1)',
          'rgba(54, 162, 235, 1)',
          'rgba(255, 206, 86, 1)',
          'rgba(75, 192, 192, 1)',
          'rgba(153, 102, 255, 1)',
          'rgba(255, 159, 64, 1)',
        ],
        borderWidth: 1,
      },
    ],
  };

  return (
    <div className="admin-home-container">
      <h1>صفحة الإدارة</h1>
      <div className="search-section">
        <input
          type="email"
          placeholder="البحث عن مستخدم أو فني بالبريد الإلكتروني"
          value={searchEmail}
          onChange={(e) => setSearchEmail(e.target.value)}
          required
        />
        <button onClick={handleSearchUser}>بحث عن مستخدم</button>
        <button onClick={handleSearchArtisan}>بحث عن فني</button>
      </div>
      <div className="charts-section">
        <div className="chart-container">
          <h2>نسبة الفنيين</h2>
          <Doughnut data={artisanChartData} />
        </div>
        <div className="chart-container">
          <h2>الإيرادات</h2>
          <Bar data={revenueChartData} />
        </div>
        <div className="chart-container">
          <h2>أكثر المحافظات نشاطًا</h2>
          <Pie data={activeProvincesChartData} />
        </div>
      </div>
    </div>
  );
};

export default AdminHome;