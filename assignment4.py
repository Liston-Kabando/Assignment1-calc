def process_file(input_path='input.txt', output_path='output.txt'):
    try:
        # Step 1: Read the content of input.txt
        with open(input_path, 'r') as infile:
            content = infile.read()

        # Step 2: Count words
        words = content.split()
        word_count = len(words)

        # Step 3: Convert to uppercase
        upper_text = content.upper()

        # Step 4: Write processed text and word count to output.txt
        with open(output_path, 'w') as outfile:
            outfile.write("WORD COUNT: " + str(word_count) + "\n\n")
            outfile.write(upper_text)

        # Step 5: Success message
        print(f"Success! '{output_path}' has been created.")
        print(f"Word count: {word_count}")

    except FileNotFoundError:
        print(f"Error: '{input_path}' not found. Please ensure it exists with at least five lines of text.")
    except Exception as e:
        print("An unexpected error occurred:", e)

def create_sample_input(input_path='input.txt'):
    """Optional helper to create a sample input.txt with five lines."""
    sample_lines = [
        "This is the first line.",
        "Here is the second line of text.",
        "Line number three is right here.",
        "Almost done—this is line four.",
        "Finally, this is line five."
    ]
    with open(input_path, 'w') as f:
        for line in sample_lines:
            f.write(line + "\n")
    print(f"Sample '{input_path}' created with {len(sample_lines)} lines.")

if __name__ == "__main__":
    # Uncomment the next line if you need a sample input file.
    # create_sample_input()

    process_file()