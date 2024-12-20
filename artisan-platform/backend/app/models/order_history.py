from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from app.config.database import Base

class OrderHistory(Base):
    """
    OrderHistory class represents the history of orders made by customers.

    Attributes:
        order_id (int): The primary key for the order history.
        booking_id (int): The foreign key referencing the booking associated with the order.
        customer_id (int): The foreign key referencing the customer who made the order.
        artisan_id (int): The foreign key referencing the artisan providing the service.
        amount_paid (decimal): The amount paid for the order.
        payment_status (str): The status of the payment (e.g., paid, pending, failed).
        transaction_date (datetime): The date and time when the transaction occurred.
    """

    __tablename__ = "order_histories"

    # Define columns
    order_id = Column(Integer, primary_key=True, index=True)
    booking_id = Column(Integer, ForeignKey("bookings.booking_id"))
    customer_id = Column(Integer, ForeignKey("users.user_id"))
    artisan_id = Column(Integer, ForeignKey("users.user_id"))
    amount_paid = Column(DECIMAL)
    payment_status = Column(String(255))
    transaction_date = Column(DateTime)

    # Define relationships
    booking = relationship("Booking", back_populates="order_histories")
    customer = relationship("User", foreign_keys=[customer_id])
    artisan = relationship("User", foreign_keys=[artisan_id])
    def to_dict(self):
        return {
            "order_id": self.order_id,
            "booking_id": self.booking_id,
            "customer_id": self.customer_id,
            "artisan_id":self.artisan_id,
            "amount_paid": self.amount_paid,
            "payment_status": self.payment_status,
            "transaction_date": self.transaction_date,
            
        }