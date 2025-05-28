import React from 'react';

const HomePage = () => {
  return (
    <div className="text-center">
      <h2 className="text-2xl font-semibold mb-4">Welcome to the POS Dashboard</h2>
      <p>This is the main dashboard area. More content will be added here.</p>
      {/* Example of a styled element */}
      <div className="mt-6 p-6 bg-gray-700 rounded-lg shadow-md">
        <h3 className="text-xl mb-2">Quick Stats (Placeholder)</h3>
        <p>Total Sales: $0.00</p>
        <p>New Orders: 0</p>
      </div>
    </div>
  );
};

export default HomePage;
