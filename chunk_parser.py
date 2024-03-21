import json
import sys
from collections import defaultdict
import xml.etree.ElementTree as ET

def parse_xml_file(input_xml_file, output_json_file):
    try:
        # Dictionary to store timestamps for each title
        title_timestamps = defaultdict(list)

        # Iterate over XML elements incrementally
        context = ET.iterparse(input_xml_file, events=("start", "end"))
        _, root = next(context)  # Get root element
        serial_number = 1
        for event, elem in context:
            if event == "end" and elem.tag == "{http://www.mediawiki.org/xml/export-0.10/}page":
                # Process page element
                title = elem.find('{http://www.mediawiki.org/xml/export-0.10/}title').text
                print(f"[{serial_number}] Processing title: {title}")  # Print title with serial number as progress
                revisions = elem.findall('{http://www.mediawiki.org/xml/export-0.10/}revision')
                for revision in revisions:
                    timestamp = revision.find('{http://www.mediawiki.org/xml/export-0.10/}timestamp').text
                    title_timestamps[title].append(timestamp)
                serial_number += 1
                # Clear the element to free memory
                elem.clear()
                root.clear()

        # Write title and timestamps to JSON file
        with open(output_json_file, "w") as json_file:
            json.dump(title_timestamps, json_file, indent=4)

    except FileNotFoundError:
        print(f"Error: File '{input_xml_file}' not found.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py input_xml_file output_json_file")
        sys.exit(1)
    
    input_xml_file = sys.argv[1]
    output_json_file = sys.argv[2]
    parse_xml_file(input_xml_file, output_json_file)
