import React, { useState } from "react";
import { useNavigate } from "react-router-dom"; // Import useNavigate

const HandymanServices = () => {
  const [selectedService, setSelectedService] = useState(null);
  const [selectedTimeOption, setSelectedTimeOption] = useState("");
  const [selectedDate, setSelectedDate] = useState("");
  const navigate = useNavigate(); // Initialize useNavigate

  const services = [
    { name: "Electrician", icon: "🔌" },
    { name: "Plumber", icon: "🚿" },
    { name: "Carpenter", icon: "🪚" },
    { name: "Painter", icon: "🎨" },
    { name: "Mechanic", icon: "🔧" },
    { name: "General Repair", icon: "🛠️" },
  ];

  const handymen = [
    {
      name: "John Doe",
      rating: 4.5,
      rate: "$20 / Hour",
      image: "https://via.placeholder.com/50",
    },
    {
      name: "Jane Smith",
      rating: 5.0,
      rate: "$25 / Hour",
      image: "https://via.placeholder.com/50",
    },
    {
      name: "Mike Johnson",
      rating: 4.2,
      rate: "$18 / Hour",
      image: "https://via.placeholder.com/50",
    },
    {
      name: "Emily Davis",
      rating: 4.8,
      rate: "$22 / Hour",
      image: "https://via.placeholder.com/50",
    },
  ];

  const handleServiceClick = (service) => {
    setSelectedService(service);
  };

  const handleTimeOptionClick = (option) => {
    setSelectedTimeOption(option);
  };

  const handleDateChange = (event) => {
    setSelectedDate(event.target.value);
  };

  const handleHandymanClick = (handyman) => {
    navigate('/portfolio'); // Navigate to the portfolio page
  };

  return (
    <div style={{ fontFamily: "Arial, sans-serif", padding: "20px" }}>
      {/* Service Selection */}
      <div style={{ marginBottom: "20px" }}>
        <h2>Choose your Service</h2>
        <div
          style={{
            display: "grid",
            gridTemplateColumns: "repeat(3, 1fr)",
            gap: "10px",
          }}
        >
          {services.map((service) => (
            <button
              key={service.name}
              onClick={() => handleServiceClick(service)}
              style={{
                border: "1px solid #ddd",
                borderRadius: "10px",
                padding: "10px",
                textAlign: "center",
                backgroundColor: "#f9f9f9",
                cursor: "pointer",
              }}
            >
              <div style={{ fontSize: "24px" }}>{service.icon}</div>
              <div>{service.name}</div>
            </button>
          ))}
        </div>
      </div>

      {/* Service Details */}
      {selectedService && (
        <div>
          <h2>{selectedService.name} Service</h2>
          <div style={{ marginBottom: "10px" }}>
            <label>
              Where?
              <input
                type="text"
                placeholder="Enter your location"
                style={{
                  display: "block",
                  width: "100%",
                  padding: "10px",
                  marginTop: "5px",
                  border: "1px solid #ddd",
                  borderRadius: "5px",
                }}
              />
            </label>
          </div>

          {/* Date Selection */}
          <div style={{ marginBottom: "10px" }}>
            <label>
              Choose the Date:
              <input
                type="date"
                value={selectedDate}
                onChange={handleDateChange}
                style={{
                  display: "block",
                  width: "100%",
                  padding: "10px",
                  marginTop: "5px",
                  border: "1px solid #ddd",
                  borderRadius: "5px",
                }}
              />
            </label>
          </div>

          {/* Time Options */}
          <div style={{ marginBottom: "10px" }}>
            <label>
              Time Required:
              <div
                style={{
                  display: "flex",
                  gap: "10px",
                  marginTop: "5px",
                  flexWrap: "wrap",
                }}
              >
                {["1 Hour", "2 Hours", "One Day", "Entire Project"].map(
                  (option) => (
                    <button
                      key={option}
                      onClick={() => handleTimeOptionClick(option)}
                      style={{
                        padding: "10px",
                        borderRadius: "5px",
                        backgroundColor:
                          selectedTimeOption === option ? "#007bff" : "#f9f9f9",
                        color: selectedTimeOption === option ? "#fff" : "#000",
                        border: "1px solid #ddd",
                        cursor: "pointer",
                      }}
                    >
                      {option}
                    </button>
                  )
                )}
              </div>
            </label>
          </div>

          {/* Available Handymen */}
          <div>
            <h3>Available Handymen</h3>
            <div>
              {handymen.map((handyman) => (
                <div
                  key={handyman.name}
                  onClick={() => handleHandymanClick(handyman)}
                  style={{
                    display: "flex",
                    alignItems: "center",
                    border: "1px solid #ddd",
                    padding: "10px",
                    borderRadius: "5px",
                    marginBottom: "10px",
                    gap: "10px",
                    cursor: "pointer", // Add cursor pointer for clickable effect
                  }}
                >
                  <img
                    src={handyman.image}
                    alt={handyman.name}
                    style={{ borderRadius: "50%", width: "50px" }}
                  />
                  <div>
                    <h4>{handyman.name}</h4>
                    <p>{handyman.rate}</p>
                    <p>
                      <span
                        style={{
                          color: "#FFD700",
                          fontSize: "16px",
                          marginRight: "5px",
                        }}
                      >
                        {"★".repeat(Math.floor(handyman.rating))}
                      </span>
                      <span style={{ color: "#ccc", fontSize: "16px" }}>
                        {"★".repeat(5 - Math.floor(handyman.rating))}
                      </span>
                      ({handyman.rating})
                    </p>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default HandymanServices;