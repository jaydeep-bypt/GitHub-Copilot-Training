import React, { useState, useEffect } from 'react';
import Display from './Display';
import Button from './Button';
import HistoryPanel from './HistoryPanel';
import { FaHistory } from 'react-icons/fa';

// Calculator icons (simple Unicode for demo, replace with SVGs or icon lib for production)
const icons = {
  add: '+',
  subtract: '−',
  multiply: '×',
  divide: '÷',
  clear: '🧹',
  reset: '🔄',
  delete: '⌫',
  equals: '=',
  dot: '.',
  history: <FaHistory />,
};

// Helper to persist history in sessionStorage
const getSessionHistory = () => {
  const data = sessionStorage.getItem('calc_history');
  return data ? JSON.parse(data) : [];
};

const Calculator = () => {
  // State for input, result, history, and history panel visibility
  const [input, setInput] = useState('');
  const [result, setResult] = useState('');
  const [history, setHistory] = useState(getSessionHistory());
  const [showHistory, setShowHistory] = useState(false); // new state

  // Persist history in sessionStorage
  useEffect(() => {
    sessionStorage.setItem('calc_history', JSON.stringify(history));
  }, [history]);

  // Handle button click
  const handleButtonClick = (value) => {
    if (value === 'C') {
      setInput('');
      setResult('');
    } else if (value === 'AC') {
      setInput('');
      setResult('');
      setHistory([]);
      sessionStorage.removeItem('calc_history');
    } else if (value === 'DEL') {
      if (result !== '') {
        setResult('');
        setInput((prev) => prev.slice(0, -1));
      } else {
        setInput((prev) => prev.slice(0, -1));
      }
    } else if (value === '=') {
      try {
        // If input is empty or only zeros, show '0' and do not add to history
        if (/^0*$/.test(input)) {
          setResult('0');
          setInput('0');
          return;
        }
        // Replace all sequences of zeros with a single zero
        let expr = input.replace(/×/g, '*').replace(/÷/g, '/').replace(/−/g, '-');
        // expr = expr.replace(/\b0+\b/g, '0');
        expr = expr.replace(/\b0+(\d)/g, '$1');
        // Remove trailing operator(s) before evaluation
        expr = expr.replace(/[+\-*/.]+$/g, '');
        // If expression is only operators or empty, show '0' and do not add to history
        if (/^[+\-*/.]*$/.test(expr) || expr === '') {
          setResult('0');
          setInput('0');
          return;
        }
        if (/\d*\.\d*\./.test(expr)) throw new Error('Invalid decimal');
        if (/\/0(?!\d)/.test(expr)) throw new Error('Divide by zero');
        // eslint-disable-next-line no-eval
        const res = eval(expr);
        setResult(res);
        // Only add to history if input is not just zeros or operators
        setHistory([...history, { expression: input, result: res }]);
        setInput('' + res); // allow chaining calculations
      } catch (err) {
        setResult('Error');
        setInput('');
      }
    } else {
      if (value === '.' && /\d*\.\d*$/.test(input.split(/[^\d.]/).pop())) return;
      setResult(''); // clear result when starting new input
      setInput((prev) => prev + value);
    }
  };

  // Keyboard support
  useEffect(() => {
    const handleKeyDown = (e) => {
      const keyMap = {
        '+': '+', '-': '−', '*': '×', '/': '÷', '.': '.',
        'Enter': '=', '=': '=', 'Backspace': 'DEL', 'Delete': 'AC', 'c': 'C',
      };
      if (e.key >= '0' && e.key <= '9') {
        handleButtonClick(e.key);
      } else if (keyMap[e.key]) {
        handleButtonClick(keyMap[e.key]);
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [input, result, history]);

  // Calculator buttons
  const buttons = [
    { label: '7' }, { label: '8' }, { label: '9' }, { label: icons.divide, value: '÷' },
    { label: '4' }, { label: '5' }, { label: '6' }, { label: icons.multiply, value: '×' },
    { label: '1' }, { label: '2' }, { label: '3' }, { label: icons.subtract, value: '−' },
    { label: icons.dot, value: '.' }, { label: '0' }, { label: icons.equals, value: '=' }, { label: icons.add, value: '+' },
    { label: 'C', value: 'C', className: 'btn-clear' },
    { label: 'AC', value: 'AC', className: 'btn-reset' },
    { label: icons.delete, value: 'DEL', className: 'btn-delete' },
  ];

  return (
    <div className="calculator-container">
      {showHistory && (
        <HistoryPanel history={history} show={showHistory} onClose={() => setShowHistory(false)} />
      )}
      <div className="calculator-main">
        <Display value={result !== '' ? result : input || '0'} />
        <div className="calculator-buttons">
          {buttons.map((btn, idx) => (
            <Button
              key={idx}
              label={btn.label}
              icon={btn.value && icons[btn.value.toLowerCase()]}
              className={btn.className}
              onClick={() => handleButtonClick(btn.value || btn.label)}
              ariaLabel={btn.value || btn.label}
            />
          ))}
          {/* History icon button */}
          <Button
            label=""
            icon={icons.history}
            className={`btn-history${showHistory ? ' active' : ''}`}
            onClick={() => setShowHistory((prev) => !prev)}
            ariaLabel="History"
          />
        </div>
      </div>
    </div>
  );
};

export default Calculator;
