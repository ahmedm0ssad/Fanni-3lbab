import React, { useState, useEffect } from 'react';
import { Line } from 'react-chartjs-2';
import { useNavigate } from 'react-router-dom';
import './ArtisanHome.css';

const TechnicianDashboard = () => {
  const navigate = useNavigate();
  const user = {
    name: "Ahmed Mohamed",
    email: "ahmed@example.com",
    profileImage: "https://via.placeholder.com/100",
    overallRating: 4.5,
  };

  const [ongoingTasks, setOngoingTasks] = useState([
    { service: "Plumbing", location: "Giza", date: "2024-12-19", price: "$50" },
    { service: "Cleaning", location: "Cairo", date: "2024-12-18", price: "$30" },
  ]);

  const [completedTasks, setCompletedTasks] = useState([
    { service: "Repairing", price: "$100", rating: 4.9 },
    { service: "Shifting", price: "$150", rating: 5.0 },
  ]);

  const [currentRequests, setCurrentRequests] = useState([
    {
      service: "Electrical Repair",
      location: "Alexandria",
      date: "2024-12-20",
      price: "$40",
      description: "Fixing electrical wiring issues in the living room.",
      address: "123 Main St, Alexandria",
    },
  ]);

  const [viewMode, setViewMode] = useState("rating"); // Toggle between rating and earnings

  const earningsData = {
    labels: ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5"],
    datasets: [
      {
        label: "Earnings",
        data: [50, 75, 100, 150, 200],
        fill: false,
        backgroundColor: "#007bff",
        borderColor: "#007bff",
      },
    ],
  };

  useEffect(() => {
    // جلب الطلبات الحالية من الخادم
    fetch('/api/current_requests')
      .then(response => response.json())
      .then(data => setCurrentRequests(data));
  }, []);

  const handleAcceptRequest = (request) => {
    setOngoingTasks([...ongoingTasks, request]);
    setCurrentRequests(currentRequests.filter(r => r !== request));
  };

  const handleRejectRequest = (request) => {
    setCurrentRequests(currentRequests.filter(r => r !== request));
  };

  const handleCompleteTask = (task) => {
    const confirmPayment = window.confirm("هل استلمت الأموال من العميل؟");
    if (confirmPayment) {
      setCompletedTasks([...completedTasks, task]);
      setOngoingTasks(ongoingTasks.filter(t => t !== task));
    }
  };

  return (
    <div className="artisan-dashboard">
      <header className="dashboard-header">
        <div className="user-info">
          <img src={user.profileImage} alt="Profile" className="profile-image" />
          <div>
            <h2>{user.name}</h2>
            <p>{user.email}</p>
          </div>
        </div>
        <button className="notification-button" onClick={() => navigate('/artisannotifications')}>
          إشعارات
        </button>
      </header>
      <main className="dashboard-main">
        <section className="tasks-section">
          <h3>الطلبات الحالية</h3>
          <ul>
            {currentRequests.map((request, index) => (
              <li key={index}>
                <p>الخدمة: {request.service}</p>
                <p>الموقع: {request.location}</p>
                <p>التاريخ: {request.date}</p>
                <p>السعر: {request.price}</p>
                <p>الوصف: {request.description}</p>
                <p>العنوان: {request.address}</p>
                <button onClick={() => handleAcceptRequest(request)}>قبول</button>
                <button onClick={() => handleRejectRequest(request)}>رفض</button>
              </li>
            ))}
          </ul>
        </section>
        <section className="tasks-section">
          <h3>المهام الجارية</h3>
          <ul>
            {ongoingTasks.map((task, index) => (
              <li key={index}>
                <p>الخدمة: {task.service}</p>
                <p>الموقع: {task.location}</p>
                <p>التاريخ: {task.date}</p>
                <p>السعر: {task.price}</p>
                <button onClick={() => handleCompleteTask(task)}>إكمال</button>
              </li>
            ))}
          </ul>
        </section>
        <section className="tasks-section">
          <h3>المهام المكتملة</h3>
          <ul>
            {completedTasks.map((task, index) => (
              <li key={index}>
                <p>الخدمة: {task.service}</p>
                <p>السعر: {task.price}</p>
                <p>التقييم: {task.rating}</p>
              </li>
            ))}
          </ul>
        </section>
        <section className="chart-section">
          <button onClick={() => setViewMode(viewMode === "rating" ? "earnings" : "rating")}>
            {viewMode === "rating" ? "عرض الأرباح" : "عرض التقييم"}
          </button>
          {viewMode === "rating" ? (
            <div className="rating-display" style={{ color: "#007bff", fontWeight: "bold" }}>
              {user.overallRating}/5
            </div>
          ) : (
            <Line data={earningsData} />
          )}
        </section>
      </main>
    </div>
  );
};

export default TechnicianDashboard;
