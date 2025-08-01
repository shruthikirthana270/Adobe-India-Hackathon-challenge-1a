#!/usr/bin/env python3
"""
Test script for title cleaning functionality
"""

import re
from pathlib import Path

def clean_title(filename_stem: str) -> str:
    """
    Clean the filename to create a proper title.
    Removes parentheses and content, replaces underscores with spaces.
    """
    # Remove parentheses and content inside them at the end
    title = re.sub(r"\s*$$[^)]*$$$", "", filename_stem)
    
    # Replace underscores with spaces
    title = title.replace('_', ' ')
    
    # Remove extra whitespace
    title = title.strip()
    
    # Capitalize first letter of each word for better presentation
    title = ' '.join(word.capitalize() for word in title.split())
    
    return title

def test_title_cleaning():
    """Test the title cleaning function with various examples."""
    test_cases = [
        ("document_name (1)", "Document Name"),
        ("my_file_name (copy)", "My File Name"),
        ("simple_document", "Simple Document"),
        ("UPPERCASE_FILE (backup)", "Uppercase File"),
        ("mixed_Case_File (final)", "Mixed Case File"),
        ("file with spaces (old)", "File With Spaces"),
        ("no_parentheses_here", "No Parentheses Here"),
        ("multiple_underscores_test (version 2)", "Multiple Underscores Test"),
    ]
    
    print("🧪 Testing Title Cleaning Function")
    print("=" * 50)
    
    for original, expected in test_cases:
        result = clean_title(original)
        status = "✅" if result == expected else "❌"
        print(f"{status} '{original}' -> '{result}'")
        if result != expected:
            print(f"   Expected: '{expected}'")
    
    print("\n🎯 Title cleaning test completed!")

if __name__ == "__main__":
    test_title_cleaning()
