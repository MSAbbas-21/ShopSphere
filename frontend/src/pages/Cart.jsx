import { useEffect, useState } from "react";
import api from "../services/api";

function Cart() {
  const [cartItems, setCartItems] = useState([]);

  useEffect(() => {
    fetchCart();
  }, []);

  const fetchCart = async () => {
    try {
      const response = await api.get("cart/");
      setCartItems(response.data);
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div className="p-8">
      <h1 className="text-4xl font-bold mb-8">
        My Cart
      </h1>

      {cartItems.length === 0 ? (
        <h2>Your cart is empty.</h2>
      ) : (
        cartItems.map((item) => (
          <div
            key={item.id}
            className="border rounded-lg p-4 mb-4"
          >
            <h2 className="text-2xl font-semibold">
              {item.product.name}
            </h2>

            <p>Price: ₹ {item.product.price}</p>

            <p>Quantity: {item.quantity}</p>
          </div>
        ))
      )}
    </div>
  );
}

export default Cart;