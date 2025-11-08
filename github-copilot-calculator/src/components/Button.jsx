import React from 'react';

const Button = ({ label, onClick, icon, className = '', ariaLabel }) => (
  <button
    className={`calculator-btn ${className}`}
    onClick={onClick}
    aria-label={ariaLabel || label}
  >
    {icon ? <span className="btn-icon">{icon}</span> : label}
  </button>
);

export default Button;
