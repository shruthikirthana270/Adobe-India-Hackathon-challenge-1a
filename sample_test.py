#!/usr/bin/env python3
"""
Simple test script that mimics your original functionality
"""

import json
import re
from pathlib import Path

def process_pdfs_simple(input_dir, output_dir):
    """
    Simple version that matches your original code exactly.
    """
    input_dir = Path(input_dir)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    pdf_files = list(input_dir.glob("*.pdf"))
    if not pdf_files:
        print(f"No PDFs found in {input_dir}")
        return
    
    for pdf_file in pdf_files:
        original_stem = pdf_file.stem
        # Remove parentheses and content inside them at the end of the filename
        title = re.sub(r"\s*$$[^)]*$$$", "", original_stem)
        title = title.replace('_', ' ').strip()
        
        print(f"Original filename stem: '{original_stem}' -> Processed title: '{title}'")
        
        output_data = {
            "title": title,
            "outline": []
        }
        
        output_file = output_dir / f"{original_stem}.json"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(output_data, f, indent=2)
        
        print(f"Generated output for {pdf_file.name} -> {output_file.name}")

if __name__ == "__main__":
    # Create test directories
    input_folder = Path("sample_data/input")
    output_folder = Path("outputs")
    
    input_folder.mkdir(parents=True, exist_ok=True)
    
    # Create some dummy PDF files for testing
    test_files = [
        "document_sample (1).pdf",
        "my_test_file (copy).pdf", 
        "simple_document.pdf",
        "report_final (backup).pdf"
    ]
    
    print("📝 Creating test PDF files...")
    for filename in test_files:
        test_file = input_folder / filename
        test_file.write_text("dummy pdf content")
        print(f"   Created: {filename}")
    
    print("\n🔄 Processing PDFs...")
    process_pdfs_simple(input_folder, output_folder)
    
    print("\n📊 Results:")
    for json_file in output_folder.glob("*.json"):
        with open(json_file, 'r') as f:
            data = json.load(f)
        print(f"   {json_file.name}: title = '{data['title']}'")
