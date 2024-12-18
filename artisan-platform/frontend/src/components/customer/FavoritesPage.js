import React, { useEffect, useState } from "react";
import "./FavoritesPage.css";

const FavoritesPage = () => {
  const [favoriteItems, setFavoriteItems] = useState([]);

  useEffect(() => {
    const userId = localStorage.getItem('userId');
    if (!userId) {
      console.error("User ID is not found in localStorage.");
      return;
    }

    const users = [
      { id: 1, email: 'user1@example.com', password: 'password1', favorites: [1, 2] },
      { id: 2, email: 'user2@example.com', password: 'password2', favorites: [] },
    ];
    const items = [
      { id: 1, name: 'Nintendo Switch Lite', image: 'path/to/image1.jpg' },
      { id: 2, name: 'Neuromancer', image: 'path/to/image2.jpg' },
      // ...other items
    ];

    const user = users.find(u => u.id === parseInt(userId));
    if (user) {
      const favoriteItems = items.filter(item => user.favorites.includes(item.id));
      setFavoriteItems(favoriteItems);
    } else {
      console.error("User not found.");
    }
  }, []);

  return (
    <div className="favorites-container">
      <div className="header">
        <h1>Favorites</h1>
        <div className="cart-icon">🛒</div>
      </div>

      <div className="search-bar">
        <input type="text" placeholder="Search" />
      </div>

      <div className="categories">
        <button>Books</button>
        <button>Electronics</button>
        <button>Clothes</button>
        <button>E-Books</button>
        <button>Furniture</button>
      </div>

      <div className="grid">
        {favoriteItems.map(item => (
          <div className="card" key={item.id}>
            <span className="heart">❤</span>
            <img src={item.image} alt={item.name} />
            <h3>{item.name}</h3>
          </div>
        ))}
      </div>

      <div className="pagination">
        <button>1</button>
        <button>2</button>
        <button>3</button>
      </div>
    </div>
  );
};

export default FavoritesPage;
