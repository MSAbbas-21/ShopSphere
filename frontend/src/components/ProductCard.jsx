import { Link } from "react-router-dom";

function ProductCard({ product }) {
  return (
    <Link to={`/products/${product.id}`} className="block">
      <div className="border rounded-lg shadow-lg p-4 w-64 hover:shadow-xl transition">

        <h2 className="text-xl font-bold">
          {product.name}
        </h2>

        <p className="text-gray-500 mt-2">
          ₹ {product.price}
        </p>

        <p className="mt-2">
          Stock: {product.stock}
        </p>

        <button className="bg-blue-600 text-white px-4 py-2 rounded mt-4 w-full">
          Add to Cart
        </button>

      </div>
    </Link>
  );
}

export default ProductCard;