import React from "react";
import "./BookingPage.css";

// Import images
import PlumbingImage from "../../assets/rec.jpg"; // تحديث المسار إلى صورة موجودة
import PaintingImage from "../../assets/oip3.jpeg";
import CarpentryImage from "../../assets/4.jpeg";
import ElectricalImage from "../../assets/OIP (3).jpeg";
import GardeningImage from "../../assets/OIP (4).jpeg";
import CleaningImage from "../../assets/OIP (5).jpeg";

const BookingPage = () => {
  const services = [
    {
      id: 1,
      name: "Plumbing Services",
      description: "Fix leaks, install pipes, and more by a professional artisan.",
      price: "$50 per hour",
      image: PlumbingImage
    },
    {
      id: 2,
      name: "Painting Services",
      description: "High-quality painting services for your home or office.",
      price: "$100 per room",
      image: PaintingImage
    },
    {
      id: 3,
      name: "Woodwork & Carpentry",
      description: "Custom furniture, repairs, and more by skilled artisans.",
      price: "$75 per hour",
      image: CarpentryImage
    },
    {
      id: 4,
      name: "Electrical Repairs",
      description: "Efficient and safe electrical repair services by professionals.",
      price: "$60 per hour",
      image: ElectricalImage
    },
    {
      id: 5,
      name: "Gardening Services",
      description: "Professional gardening and landscaping for your outdoor spaces.",
      price: "$80 per session",
      image: GardeningImage
    },
    {
      id: 6,
      name: "Cleaning Services",
      description: "Thorough cleaning for your home or office spaces.",
      price: "$40 per session",
      image: CleaningImage
    }
  ];

  return (
    <div className="booking-container">
      {/* Header */}
      <div className="header">
        <h1>Booking Page</h1>
      </div>

      {/* Services Section */}
      <div className="container">
        {services.map((service) => (
          <div key={service.id} className="service-card">
            <img src={service.image} alt={service.name} />
            <div className="service-details">
              <h3>{service.name}</h3>
              <p>{service.description}</p>
              <p className="price">{service.price}</p>
              <button>Book Now</button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default BookingPage;
