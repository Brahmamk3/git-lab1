import os

input_folder = 'data_input'
output_folder = 'data_output'

# Step 1: Ensure input folder exists
if not os.path.exists(input_folder):
    os.makedirs(input_folder)
    print(f"'{input_folder}' created. Please add .txt files and re-run the script.")
    exit()

# Step 2: Ensure output folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Step 3: Process each .txt file
summary_data = []

for filename in os.listdir(input_folder):
    if filename.endswith('.txt'):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        with open(input_path, 'r') as infile:
            lines = infile.readlines()

        modified_lines = []
        line_count = 0
        word_count = 0

        for line in lines:
            if line.strip().startswith('#'):
                modified_lines.append(line)  # Add unmodified comment line
                continue

            line_count += 1
            word_count += len(line.strip().split())

            # Replace "temp" (if any), or keep original line
            modified_line = line.replace("temp", "permanent")
            modified_lines.append(modified_line)

        # Step 4: Save to output folder with same filename
        with open(output_path, 'w') as outfile:
            outfile.writelines(modified_lines)

        # Collect summary info
        summary_data.append(f"{filename} | Lines: {line_count} | Words: {word_count}")

# Step 5: Write summary file
summary_path = os.path.join(output_folder, 'summary.txt')
with open(summary_path, 'w') as summary_file:
    summary_file.write("Summary of Processed Files\n")
    summary_file.write("===========================\n")
    for entry in summary_data:
        summary_file.write(entry + "\n")

print(f"Done. Modified files + summary saved in '{output_folder}' folder.")


"""
output:
brahm@Brahmanjaneyulu MINGW64 ~/OneDrive/Desktop/DevopsNotes/PythonScriptiing/git-lab1 (master)
$ python task2.py
Done. Modified files + summary saved in 'data_output' folder.

"""

