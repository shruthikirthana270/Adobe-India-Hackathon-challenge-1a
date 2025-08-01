#!/bin/bash

# Build and test script for Adobe PDF Processor Challenge 1a

echo "🚀 Building Adobe PDF Processor for Challenge 1a..."

# Build the Docker image
docker build --platform linux/amd64 -t adobe-pdf-processor .

if [ $? -eq 0 ]; then
    echo "✅ Docker image built successfully"
else
    echo "❌ Docker build failed"
    exit 1
fi

# Create test directories if they don't exist
mkdir -p input output

echo "📁 Test directories created"

# Check if there are PDFs in the input directory
pdf_count=$(find input -name "*.pdf" 2>/dev/null | wc -l)

if [ $pdf_count -eq 0 ]; then
    echo "⚠️  No PDF files found in input directory"
    echo "   Please add PDF files to the 'input' directory before running the test"
    echo "   Example: cp your_pdfs/*.pdf input/"
else
    echo "📄 Found $pdf_count PDF file(s) in input directory"
fi

echo "🔄 Running PDF processor..."
start_time=$(date +%s)

docker run --rm \
    -v $(pwd)/input:/app/input:ro \
    -v $(pwd)/output:/app/output \
    --network none \
    adobe-pdf-processor

end_time=$(date +%s)
execution_time=$((end_time - start_time))

if [ $? -eq 0 ]; then
    echo "✅ PDF processing completed successfully in ${execution_time} seconds"
    
    # Count output files
    json_count=$(find output -name "*.json" 2>/dev/null | wc -l)
    echo "📊 Generated $json_count JSON output file(s)"
    
    if [ $json_count -gt 0 ]; then
        echo "📋 Output files:"
        ls -la output/*.json 2>/dev/null || echo "   No JSON files found"
    fi
else
    echo "❌ PDF processing failed"
    exit 1
fi

echo "🎉 Challenge 1a solution test completed!"
