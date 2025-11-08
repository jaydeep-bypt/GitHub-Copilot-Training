import React from 'react';

const Display = ({ value }) => (
  <div className="calculator-display" aria-label="display">
    {value}
  </div>
);

export default Display;
