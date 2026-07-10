import { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import api from "../services/api";

function ProductDetails() {
  const { id } = useParams();
  const navigate = useNavigate();

  const [product, setProduct] = useState(null);

  useEffect(() => {
    fetchProduct();
  }, []);

  const fetchProduct = async () => {
    try {
      const response = await api.get(`products/${id}/`);
      setProduct(response.data);
    } catch (error) {
      console.log(error);
    }
  };

  const addToCart = async () => {
    try {
      await api.post("cart/add/", {
        product: product.id,
        quantity: 1,
      });

      alert("Product added to cart!");

      navigate("/cart");
    } catch (error) {
      console.log(error.response?.data || error);
      alert("Failed to add product.");
    }
  };

  if (!product) {
    return <h1 className="text-3xl p-8">Loading...</h1>;
  }

  return (
    <div className="max-w-4xl mx-auto p-8">

      <h1 className="text-4xl font-bold">
        {product.name}
      </h1>

      <p className="text-2xl text-green-600 mt-4">
        ₹ {product.price}
      </p>

      <p className="mt-4">
        <strong>Stock:</strong> {product.stock}
      </p>

      <p className="mt-4">
        {product.description}
      </p>

      <button
        onClick={addToCart}
        className="bg-blue-600 text-white px-6 py-3 rounded mt-6 hover:bg-blue-700"
      >
        Add to Cart
      </button>

    </div>
  );
}

export default ProductDetails;