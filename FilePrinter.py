#!/usr/bin/python3
import os
import sys
import argparse

def list_files(directory, exclude, output_file):
    """
    List files and their contents in the specified directory,
    excluding those in the exclude list, and write the results
    to the specified file.

    Args:
    - directory (str): Directory path to start listing files from.
    - exclude (list): List of absolute paths to exclude from listing.
    - output_file (str): Output file path to write the listing results.

    """
    with open(output_file, 'w') as f:
        for root, dirs, files in os.walk(directory):
            dirs[:] = [d for d in dirs if os.path.join(root, d) not in exclude and not d.startswith('.')]
            
            for file_name in files:
                if file_name.startswith('.'):
                    continue
                
                file_path = os.path.join(root, file_name)
                
                if file_path not in exclude and file_name != script_name:
                    f.write("{}\n".format(file_path))
                    f.write("-------------------\n")
                    
                    try:
                        with open(file_path, 'r') as file:
                            f.write(file.read())
                            f.write("\n\n")
                    except Exception as e:
                        f.write("Error reading file: {}\n\n".format(e))

def main():
    parser = argparse.ArgumentParser(description="List files and their contents")
    parser.add_argument('-n', '--no-print', nargs='+', default=[], help="Files or directories to exclude")
    parser.add_argument('-o', '--output-file', required=True, help="Output file name")

    args, unknown = parser.parse_known_args()

    # Check if there are unrecognized arguments
    if unknown:
        print("Unrecognized arguments:", unknown)
        sys.exit(1)

    output_file = args.output_file
    exclude = [os.path.abspath(item) for item in args.no_print]
    global script_name
    script_name = os.path.basename(__file__)

    if os.path.exists(output_file):
        overwrite = input("File '{}' exists. Overwrite? (y/n): ".format(output_file)).strip().lower()
        if overwrite != 'y':
            print("Operation cancelled.")
            sys.exit(0)

    list_files(os.getcwd(), exclude, output_file)
    print("Output written to {}".format(output_file))

if __name__ == "__main__":
    main()
