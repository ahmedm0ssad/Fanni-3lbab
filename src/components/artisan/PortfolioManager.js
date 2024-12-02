import React, { useState, useEffect } from 'react';
import './PortfolioManager.css';

const Portfolio = () => {
  const [projects, setProjects] = useState([]);

  useEffect(() => {
    // بيانات افتراضية للمشاريع
    const fetchedProjects = [
      {
        title: 'Home Renovation',
        description: 'A complete home renovation project focusing on modern design and functionality.',
        images: ['https://via.placeholder.com/100', 'https://via.placeholder.com/100'],
        rating: 4.5,
      },
      {
        title: 'Bathroom Remodeling',
        description: 'Upgraded a bathroom with high-end fixtures and a new layout.',
        images: ['https://via.placeholder.com/100', 'https://via.placeholder.com/100'],
        rating: 4.0,
      },
      {
        title: 'Kitchen Makeover',
        description: 'Transformed a traditional kitchen into a sleek, modern space.',
        images: ['https://via.placeholder.com/100', 'https://via.placeholder.com/100'],
        rating: 5.0,
      },
    ];
    setProjects(fetchedProjects);
  }, []);

  return (
    <div className="portfolio">
      <h2>Portfolio</h2>
      <p>Explore some of the amazing projects completed by our skilled professionals.</p>
      <div className="portfolio-list">
        {projects.map((project, index) => (
          <div key={index} className="portfolio-item">
            <h3>{project.title}</h3>
            <p>{project.description}</p>
            <div className="portfolio-images">
              {project.images.map((image, i) => (
                <img key={i} src={image} alt={`Project ${index + 1} Image ${i + 1}`} />
              ))}
            </div>
            <p>Rating: 
              <span style={{ color: '#FFD700', marginLeft: '5px' }}>
                {'★'.repeat(Math.floor(project.rating))}
              </span>
              <span style={{ color: '#ddd' }}>
                {'★'.repeat(5 - Math.floor(project.rating))}
              </span>
            </p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Portfolio;
