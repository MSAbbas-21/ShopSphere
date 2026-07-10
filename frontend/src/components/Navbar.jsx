import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav className="bg-blue-600 text-white px-8 py-4 flex justify-between items-center">

      <h1 className="text-2xl font-bold">
        ShopSphere
      </h1>

      <ul className="flex gap-6">

        <li>
          <Link to="/">Home</Link>
        </li>

        <li>
          <Link to="/">Products</Link>
        </li>

        <li>
          <Link to="/">Wishlist</Link>
        </li>

        <li>
          <Link to="/cart">Cart</Link>
        </li>

        <li>
          <Link to="/login">Login</Link>
        </li>

      </ul>

    </nav>
  );
}

export default Navbar;