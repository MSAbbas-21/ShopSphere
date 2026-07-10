import { useEffect, useState } from "react";
import Navbar from "../components/Navbar";
import ProductCard from "../components/ProductCard";
import api from "../services/api";

function Home() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    fetchProducts();
  }, []);

  const fetchProducts = async () => {
    try {
      const response = await api.get("products/");
      setProducts(response.data);
    } catch (error) {
      console.log(error);
    }
  };

  return (
  <>
    <Navbar />

    <div className="p-8">
      <h1 className="text-4xl font-bold mb-8">
        Featured Products
      </h1>

      <div className="flex gap-8 flex-wrap">
        {products.map((product) => (
          <ProductCard
            key={product.id}
            product={product}
          />
        ))}
      </div>
    </div>
  </>
  );
}

export default Home;