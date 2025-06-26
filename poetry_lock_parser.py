
import argparse

# Default file names
INPUT_FILE = "poetry.lock"
OUTPUT_FILE = "parsed_requirements.txt"


def poetry_parser(input_path, output_path):
    """
    Parse poetry.lock file and output all python dependencies as text file.
    """
    requirements_arr = []

    # Read poetry.lock 
    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Process content lines
    lines = content.splitlines()
    for i, line in enumerate(lines):
        if "[[package]]" in line:
            pkg_tuple = lines[i+1].split('=', 1)
            ver_tuple = lines[i+2].split('=', 1)

            pkg_name = pkg_tuple[1].strip()[1:-1]
            ver_no = ver_tuple[1].strip()[1:-1]

            requirements_arr.append(f"{pkg_name}=={ver_no}")

    # Write to output file
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(sorted(requirements_arr)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract python package dependencies from poetry.lock")
    parser.add_argument("--input", default=INPUT_FILE, required=False, help="Path to poetry.lock file")
    parser.add_argument("--output", default=OUTPUT_FILE, required=False, help=f"Optional path to save output (default: {OUTPUT_FILE})")

    args = parser.parse_args()
    try:
        poetry_parser(args.input, args.output)
    except FileNotFoundError as ex:
        print(f"File Not Found!!! Please give correct path for {args.input}")
    except Exception as ex:
        print(f"Some error occurred: {ex}")
