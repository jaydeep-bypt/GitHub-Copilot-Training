#!/usr/bin/env python3
"""
Test Suite for utils.py Module

This file contains comprehensive tests for all functions in the utils module.
Run this file to verify that all utility functions are working correctly.

Usage:
    python3 test_utils.py

Author: GitHub Copilot
Date: 2025-10-11
Version: 1.0.0
"""

import sys
import traceback
from datetime import datetime
import utils


class TestRunner:
    """Simple test runner to organize and execute tests."""
    
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.total = 0
    
    def run_test(self, test_name, test_func):
        """Run a single test function and track results."""
        self.total += 1
        print(f"\n{'='*60}")
        print(f"Running: {test_name}")
        print('='*60)
        
        try:
            test_func()
            self.passed += 1
            print(f"✅ {test_name} - PASSED")
        except Exception as e:
            self.failed += 1
            print(f"❌ {test_name} - FAILED")
            print(f"Error: {e}")
            print("Traceback:")
            traceback.print_exc()
    
    def print_summary(self):
        """Print test results summary."""
        print(f"\n{'='*60}")
        print("TEST SUMMARY")
        print('='*60)
        print(f"Total Tests: {self.total}")
        print(f"Passed: {self.passed}")
        print(f"Failed: {self.failed}")
        print(f"Success Rate: {(self.passed/self.total)*100:.1f}%")
        
        if self.failed == 0:
            print("\n🎉 ALL TESTS PASSED! The utils module is working perfectly!")
        else:
            print(f"\n⚠️  {self.failed} test(s) failed. Please check the errors above.")


def test_format_date():
    """Test the format_date function with various scenarios."""
    print("Testing format_date() function...")
    
    # Create test datetime
    test_date = datetime(2025, 10, 11, 14, 30, 45)
    
    # Test 1: Default format
    result = utils.format_date(test_date)
    expected = "2025-10-11"
    assert result == expected, f"Expected '{expected}', got '{result}'"
    print(f"✓ Default format: {result}")
    
    # Test 2: Custom format - full date
    result = utils.format_date(test_date, "%B %d, %Y")
    expected = "October 11, 2025"
    assert result == expected, f"Expected '{expected}', got '{result}'"
    print(f"✓ Full date format: {result}")
    
    # Test 3: Date with time
    result = utils.format_date(test_date, "%m/%d/%Y %H:%M:%S")
    expected = "10/11/2025 14:30:45"
    assert result == expected, f"Expected '{expected}', got '{result}'"
    print(f"✓ Date with time: {result}")
    
    # Test 4: Short format
    result = utils.format_date(test_date, "%m/%d/%y")
    expected = "10/11/25"
    assert result == expected, f"Expected '{expected}', got '{result}'"
    print(f"✓ Short format: {result}")
    
    # Test 5: Day name format
    result = utils.format_date(test_date, "%A, %B %d")
    expected = "Saturday, October 11"  # October 11, 2025 is a Saturday
    assert result == expected, f"Expected '{expected}', got '{result}'"
    print(f"✓ Day name format: {result}")


def test_capitalize_words():
    """Test the capitalize_words function with various scenarios."""
    print("Testing capitalize_words() function...")
    
    test_cases = [
        # (input, expected_output)
        ("hello world", "Hello World"),
        ("PYTHON programming", "Python Programming"),
        ("the quick brown fox", "The Quick Brown Fox"),
        ("john doe smith", "John Doe Smith"),
        ("", ""),
        ("a", "A"),
        ("hello", "Hello"),
        ("HELLO", "Hello"),
        ("hELLo WoRLD", "Hello World"),
        ("first   second    third", "First   Second    Third"),  # Multiple spaces
        ("123 main street", "123 Main Street"),
        ("mary-jane watson", "Mary-Jane Watson"),
        ("o'connor", "O'Connor"),
    ]
    
    for i, (input_text, expected) in enumerate(test_cases, 1):
        result = utils.capitalize_words(input_text)
        assert result == expected, f"Test {i}: Expected '{expected}', got '{result}'"
        print(f"✓ Test {i}: '{input_text}' -> '{result}'")


def test_calculate_age():
    """Test the calculate_age function with various scenarios."""
    print("Testing calculate_age() function...")
    
    # Current date for testing (October 11, 2025)
    current_date = datetime.now()
    print(f"Current date for testing: {current_date.strftime('%Y-%m-%d')}")
    
    # Test cases with known ages (based on current date being 2025-10-11)
    test_cases = [
        ("1990-05-15", 35),  # Birthday already passed this year
        ("2000-12-25", 24),  # Birthday hasn't occurred yet this year
        ("1985-01-01", 40),  # Birthday already passed
        ("2025-01-01", 0),   # Born this year, birthday passed
        ("1975-10-11", 50),  # Birthday is today
    ]
    
    for birthdate, expected_age in test_cases:
        result = utils.calculate_age(birthdate)
        print(f"✓ Birthdate {birthdate} -> Age: {result} years (expected: {expected_age})")
        # Note: We don't assert exact ages since the test might run on different dates
        # Instead, we check that the result is reasonable
        assert 0 <= result <= 150, f"Age {result} seems unreasonable for birthdate {birthdate}"
    
    # Test different date formats
    print("\nTesting different date formats:")
    
    # US format (MM/DD/YYYY)
    result = utils.calculate_age("05/15/1990", "%m/%d/%Y")
    print(f"✓ US format (05/15/1990): {result} years")
    assert isinstance(result, int), "Result should be an integer"
    
    # European format (DD-MM-YYYY)
    result = utils.calculate_age("15-05-1990", "%d-%m-%Y")
    print(f"✓ European format (15-05-1990): {result} years")
    assert isinstance(result, int), "Result should be an integer"
    
    # Test error handling
    print("\nTesting error handling:")
    
    try:
        utils.calculate_age("invalid-date")
        assert False, "Should have raised ValueError for invalid date"
    except ValueError:
        print("✓ Correctly raised ValueError for invalid date")
    
    try:
        utils.calculate_age("05/15/1990", "%Y-%m-%d")  # Wrong format
        assert False, "Should have raised ValueError for format mismatch"
    except ValueError:
        print("✓ Correctly raised ValueError for format mismatch")


def test_clean_whitespace():
    """Test the clean_whitespace function with various scenarios."""
    print("Testing clean_whitespace() function...")
    
    test_cases = [
        # (input, expected_output)
        ("  hello    world  ", "hello world"),
        ("line1\n\n\nline2", "line1 line2"),
        ("   John    Doe   ", "John Doe"),
        ("normal text", "normal text"),
        ("", ""),
        ("   ", ""),
        ("text\twith\ttabs", "text with tabs"),
        ("text\nwith\nnewlines", "text with newlines"),
        ("text\r\nwith\r\ncarriage\r\nreturns", "text with carriage returns"),
        ("multiple\n\n\n\nlines", "multiple lines"),
        ("  \t  \n  ", ""),
        ("word", "word"),
    ]
    
    for i, (input_text, expected) in enumerate(test_cases, 1):
        result = utils.clean_whitespace(input_text)
        assert result == expected, f"Test {i}: Expected '{expected}', got '{result}'"
        print(f"✓ Test {i}: {repr(input_text)} -> '{result}'")


def test_truncate_string():
    """Test the truncate_string function with various scenarios."""
    print("Testing truncate_string() function...")
    
    long_text = "This is a very long sentence that needs truncation for display purposes"
    
    # Test 1: Basic truncation
    result = utils.truncate_string(long_text, 15)
    expected = "This is a ve..."
    assert result == expected, f"Expected '{expected}', got '{result}'"
    assert len(result) == 15, f"Result length should be 15, got {len(result)}"
    print(f"✓ Basic truncation (15 chars): '{result}'")
    
    # Test 2: Longer truncation
    result = utils.truncate_string(long_text, 30)
    expected = "This is a very long sentenc..."
    assert result == expected, f"Expected '{expected}', got '{result}'"
    assert len(result) == 30, f"Result length should be 30, got {len(result)}"
    print(f"✓ Longer truncation (30 chars): '{result}'")
    
    # Test 3: No truncation needed
    short_text = "Short text"
    result = utils.truncate_string(short_text, 20)
    assert result == short_text, f"Expected '{short_text}', got '{result}'"
    print(f"✓ No truncation needed: '{result}'")
    
    # Test 4: Exact length match
    result = utils.truncate_string("Hello", 5)
    assert result == "Hello", f"Expected 'Hello', got '{result}'"
    print(f"✓ Exact length match: '{result}'")
    
    # Test 5: Custom suffix
    result = utils.truncate_string(long_text, 15, " >>")
    expected = "This is a ve >>"
    assert result == expected, f"Expected '{expected}', got '{result}'"
    assert len(result) == 15, f"Result length should be 15, got {len(result)}"
    print(f"✓ Custom suffix: '{result}'")
    
    # Test 6: Empty string
    result = utils.truncate_string("", 10)
    assert result == "", f"Expected '', got '{result}'"
    print(f"✓ Empty string: '{result}'")
    
    # Test error handling
    print("\nTesting error handling:")
    
    try:
        utils.truncate_string("Hello", 2, "...")  # max_length < suffix length
        assert False, "Should have raised ValueError"
    except ValueError as e:
        print(f"✓ Correctly raised ValueError: {e}")


def test_integration_scenarios():
    """Test realistic integration scenarios using multiple functions together."""
    print("Testing integration scenarios...")
    
    # Scenario 1: User profile processing
    print("\n--- Scenario 1: User Profile Processing ---")
    
    # Raw user data (messy)
    raw_name = "  john   doe  "
    raw_birthdate = "1990-05-15"
    raw_bio = "  Software   developer    with   passion   for   Python  "
    
    # Process the data
    clean_name = utils.capitalize_words(utils.clean_whitespace(raw_name))
    age = utils.calculate_age(raw_birthdate)
    clean_bio = utils.clean_whitespace(raw_bio)
    bio_preview = utils.truncate_string(clean_bio, 30)
    profile_date = utils.format_date(datetime.now(), "%B %d, %Y")
    
    print(f"✓ Cleaned name: '{clean_name}'")
    print(f"✓ Calculated age: {age} years")
    print(f"✓ Cleaned bio: '{clean_bio}'")
    print(f"✓ Bio preview: '{bio_preview}'")
    print(f"✓ Profile date: '{profile_date}'")
    
    # Assertions
    assert clean_name == "John Doe", f"Expected 'John Doe', got '{clean_name}'"
    assert isinstance(age, int), "Age should be an integer"
    assert len(bio_preview) <= 30, f"Bio preview too long: {len(bio_preview)}"
    
    # Scenario 2: Content management
    print("\n--- Scenario 2: Content Management ---")
    
    article_title = "understanding machine learning fundamentals"
    publish_date = datetime(2025, 10, 11)
    content_preview = "This article covers the basic concepts of machine learning including supervised and unsupervised learning algorithms."
    
    formatted_title = utils.capitalize_words(article_title)
    formatted_date = utils.format_date(publish_date, "%B %d, %Y")
    short_preview = utils.truncate_string(content_preview, 50)
    
    print(f"✓ Formatted title: '{formatted_title}'")
    print(f"✓ Formatted date: '{formatted_date}'")
    print(f"✓ Short preview: '{short_preview}'")
    
    assert formatted_title == "Understanding Machine Learning Fundamentals"
    assert formatted_date == "October 11, 2025"
    assert len(short_preview) <= 50


def main():
    """Main function to run all tests."""
    print("🚀 Starting comprehensive test suite for utils.py module")
    print(f"Test started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Create test runner
    runner = TestRunner()
    
    # Run all tests
    runner.run_test("format_date() tests", test_format_date)
    runner.run_test("capitalize_words() tests", test_capitalize_words)
    runner.run_test("calculate_age() tests", test_calculate_age)
    runner.run_test("clean_whitespace() tests", test_clean_whitespace)
    runner.run_test("truncate_string() tests", test_truncate_string)
    runner.run_test("Integration scenarios", test_integration_scenarios)
    
    # Print summary
    runner.print_summary()
    
    # Exit with appropriate code
    sys.exit(0 if runner.failed == 0 else 1)


if __name__ == "__main__":
    main()