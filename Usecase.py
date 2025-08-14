import re

def read_server_log(file_path, output_path=None):
    # Compile regex to match any of the tags
    pattern = re.compile(r"\[(ERROR|WARNING|FAILURE)\]")
    
    results = []
    
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            for line_number, line in enumerate(f, start=1):
                if pattern.search(line):
                    results.append(f"Line {line_number}: {line.strip()}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # Output results
    if output_path:
        try:
            with open(output_path, "w", encoding="utf-8") as out_file:
                out_file.write("\n".join(results))
            print(f"Results saved to {output_path}")
        except Exception as e:
            print(f"Error writing output: {e}")
    else:
        # Just print to console
        for entry in results:
            print(entry)


# Example usage
if __name__ == "__main__":
    log_file = "server.log"         # Path to your log file
    output_file = "issues_found.txt"  # Path to save results (optional)
    
    read_server_log(log_file, output_file)
