#!/bin/bash

completed_dir="completed"
extracted_dir="extracted"

# Iterate over each .7z file in the completed directory
for file in "$completed_dir"/*.7z; do
    # Extract the file to the extracted directory
    7z e "$file" -o"$extracted_dir"

    # Parse the extracted XML file to JSON
    filename=$(basename "$file" .7z)
    xml_file="$extracted_dir/$filename"
    json_file="$extracted_dir/$filename.json"
    python chunk_parser.py "$xml_file" "$json_file"

    # Delete the extracted XML file
    rm "$xml_file"
done
