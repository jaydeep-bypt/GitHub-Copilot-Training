import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import Calculator from '../src/components/Calculator';

describe('Calculator', () => {
  test('renders display and buttons', () => {
    render(<Calculator />);
    expect(screen.getByLabelText('display')).toBeInTheDocument();
    expect(screen.getAllByRole('button').length).toBeGreaterThan(0);
  });

  test('performs addition', () => {
    render(<Calculator />);
    fireEvent.click(screen.getByText('1'));
    fireEvent.click(screen.getByText('+'));
    fireEvent.click(screen.getByText('2'));
    fireEvent.click(screen.getByText('='));
    expect(screen.getByLabelText('display').textContent).toMatch(/3/);
  });

  test('performs subtraction', () => {
    render(<Calculator />);
    fireEvent.click(screen.getByText('9'));
    fireEvent.click(screen.getByText('−'));
    fireEvent.click(screen.getByText('4'));
    fireEvent.click(screen.getByText('='));
    expect(screen.getByLabelText('display').textContent).toMatch(/5/);
  });

  test('performs multiplication', () => {
    render(<Calculator />);
    fireEvent.click(screen.getByText('7'));
    fireEvent.click(screen.getByText('×'));
    fireEvent.click(screen.getByText('6'));
    fireEvent.click(screen.getByText('='));
    expect(screen.getByLabelText('display').textContent).toMatch(/42/);
  });

  test('performs division', () => {
    render(<Calculator />);
    fireEvent.click(screen.getByText('8'));
    fireEvent.click(screen.getByText('÷'));
    fireEvent.click(screen.getByText('2'));
    fireEvent.click(screen.getByText('='));
    expect(screen.getByLabelText('display').textContent).toMatch(/4/);
  });

  test('handles divide by zero', () => {
    render(<Calculator />);
    fireEvent.click(screen.getByText('8'));
    fireEvent.click(screen.getByText('÷'));
    fireEvent.click(screen.getByText('0'));
    fireEvent.click(screen.getByText('='));
    expect(screen.getByLabelText('display').textContent).toMatch(/Error/);
  });

  test('history updates after calculation', () => {
    render(<Calculator />);
    fireEvent.click(screen.getByText('2'));
    fireEvent.click(screen.getByText('×'));
    fireEvent.click(screen.getByText('3'));
    fireEvent.click(screen.getByText('='));
    // Open history panel
    fireEvent.click(screen.getByLabelText('History'));
    // Find all elements with '6' and check one is in history-result class
    const results = screen.getAllByText('6');
    const found = results.some(el => el.className && el.className.includes('history-result'));
    expect(found).toBe(true);
    expect(screen.getByText('2×3')).toBeInTheDocument();
  });

  test('clear and reset buttons work', () => {
    render(<Calculator />);
    fireEvent.click(screen.getByText('5'));
    fireEvent.click(screen.getByText('C'));
    expect(screen.getByLabelText('display').textContent).toBe('0');
    fireEvent.click(screen.getByText('7'));
    fireEvent.click(screen.getByText('AC'));
    expect(screen.getByLabelText('display').textContent).toBe('0');
  });

  test('performs decimal addition', () => {
    render(<Calculator />);
    fireEvent.click(screen.getByText('2'));
    fireEvent.click(screen.getByText('.'));
    fireEvent.click(screen.getByText('5'));
    fireEvent.click(screen.getByText('+'));
    fireEvent.click(screen.getByText('3'));
    fireEvent.click(screen.getByText('.'));
    fireEvent.click(screen.getByText('1'));
    fireEvent.click(screen.getByText('='));
    expect(screen.getByLabelText('display').textContent).toMatch(/5.6/);
  });
});
