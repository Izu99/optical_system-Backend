import React, { useState, useEffect } from 'react';

const ProductsPage = () => {
  const [products, setProducts] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Simulate API call
    const fetchProducts = async () => {
      setIsLoading(true);
      setError(null);
      try {
        // Replace with your actual API endpoint
        // For now, we'll use a mock API or a timeout to simulate fetching
        await new Promise(resolve => setTimeout(resolve, 1500)); // Simulate network delay

        // Example: Successful fetch
        const mockProducts = [
          { id: 1, name: 'Product A', price: '$10.00', stock: 100 },
          { id: 2, name: 'Product B', price: '$20.00', stock: 50 },
          { id: 3, name: 'Product C', price: '$15.75', stock: 75 },
        ];
        setProducts(mockProducts);

        // Example: Simulate an error
        // throw new Error("Failed to fetch products. Please try again later.");

      } catch (err) {
        setError(err.message);
        setProducts([]); // Clear products on error
      } finally {
        setIsLoading(false);
      }
    };

    fetchProducts();
  }, []); // Empty dependency array means this effect runs once on mount

  return (
    <div>
      <h2 className="text-2xl font-semibold mb-6">Manage Products</h2>
      
      {isLoading && (
        <div className="text-center p-4">
          <p className="text-lg text-blue-400">Loading products...</p>
          {/* You could add a spinner component here */}
        </div>
      )}

      {error && (
        <div className="text-center p-4 bg-red-700_bg-opacity-50_text-red-200 rounded-md">
          <p className="text-lg font-semibold">Error:</p>
          <p>{error}</p>
        </div>
      )}

      {!isLoading && !error && (
        <div className="bg-gray-800 shadow-xl rounded-lg p-6">
          {products.length > 0 ? (
            <ul className="divide-y divide-gray-700">
              {products.map(product => (
                <li key={product.id} className="py-4 flex justify-between items-center">
                  <div>
                    <h3 className="text-lg font-medium text-gray-100">{product.name}</h3>
                    <p className="text-sm text-gray-400">Price: {product.price} - Stock: {product.stock}</p>
                  </div>
                  <button className="bg-blue-600 hover:bg-blue-700 text-white font-semibold py-2 px-4 rounded-md transition duration-150 ease-in-out">
                    Edit
                  </button>
                </li>
              ))}
            </ul>
          ) : (
            <p className="text-center text-gray-400 py-4">No products found.</p>
          )}
        </div>
      )}
    </div>
  );
};

export default ProductsPage;
