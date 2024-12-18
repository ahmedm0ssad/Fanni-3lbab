import React from 'react';
import './OrderHistory.css'; // تأكد من أن ملف CSS في نفس المسار أو قم بتعديل المسار بما يتناسب مع مشروعك.

const OrderHistory = () => {
  const orders = [
    {
      id: '12345',
      date: 'November 27, 2024',
      items: [
        {
          imgSrc: 'OIP (2).jpeg',
          name: 'Nintendo Switch Lite',
          price: '$199.99'
        },
        {
          imgSrc: 'oip3.jpeg',
          name: 'Neuromancer',
          price: '$9.99'
        }
      ]
    },
    {
      id: '12344',
      date: 'November 20, 2024',
      items: [
        {
          imgSrc: '4.jpeg',
          name: '1984',
          price: '$14.99'
        },
        {
          imgSrc: 'OIP (3).jpeg',
          name: 'The Hobbit',
          price: '$19.99'
        }
      ]
    },
    {
      id: '12343',
      date: 'November 15, 2024',
      items: [
        {
          imgSrc: 'OIP (4).jpeg',
          name: 'Notebook Dell',
          price: '$999.99'
        },
        {
          imgSrc: 'OIP (5).jpeg',
          name: 'Pro Tork Helmet',
          price: '$79.99'
        }
      ]
    }
  ];

  return (
    <div>
      <div className="header">
        <h1>Order History</h1>
        <div className="cart-icon">🛒</div>
      </div>

      <div className="order-container">
        {orders.map(order => (
          <div className="order" key={order.id}>
            <div className="order-header">
              <h3>Order #{order.id}</h3>
              <span className="order-date">{order.date}</span>
            </div>
            <div className="order-items">
              {order.items.map((item, index) => (
                <div className="item" key={index}>
                  <img src={item.imgSrc} alt={item.name} />
                  <div className="item-info">
                    <h4>{item.name}</h4>
                    <p className="item-price">{item.price}</p>
                  </div>
                </div>
              ))}
            </div>
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

export default OrderHistory;
