import tkinter as tk
from tkinter import scrolledtext
import threading
import requests
import urllib3
import pyperclip  # Import pyperclip for clipboard functionality

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def fetch_mitre_technique_description(technique_id):
    url = "https://raw.githubusercontent.com/mitre/cti/master/enterprise-attack/enterprise-attack.json"

    try:
        response = requests.get(url, verify=False)
        response.raise_for_status()

        data = response.json()
        techniques = [item for item in data['objects'] if item['type'] == 'attack-pattern']

        for technique in techniques:
            for external_ref in technique.get('external_references', []):
                if technique_id == external_ref.get('external_id', ''):
                    return technique.get('description', "No description available")

        return "Technique not found."
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

def process_text(description):
    characters_to_remove = "-|><!&;"
    description = description.replace("\\", "/")
    for char in characters_to_remove:
        description = description.replace(char, "")
    return description

def on_go_button_click():
    technique_id = input_text.get().strip().upper().replace('_', '.')

    def fetch_description():
        description = fetch_mitre_technique_description(technique_id)
        processed_description = process_text(description)
        return processed_description

    # Run the fetch_description function in a separate thread
    thread = threading.Thread(target=lambda: update_output(fetch_description()))
    thread.start()

def update_output(description):
    # Update the output text area in the main GUI thread
    root.after(0, output_text.delete, '1.0', tk.END)  # Clear previous content
    root.after(0, output_text.insert, '1.0', description)  # Insert new content

def copy_to_clipboard():
    description = output_text.get('1.0', tk.END)  # Get text from output text area
    pyperclip.copy(description)  # Copy description to clipboard

def on_enter_key(event):
    on_go_button_click()

# Create the main window
root = tk.Tk()
root.title("MITRE Technique Querier")

# Calculate the screen width and height for centering the window
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = 600
window_height = 400

x_position = (screen_width // 2) - (window_width // 2)
y_position = (screen_height // 2) - (window_height // 2)

# Set the window size and position
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Create and place the instructions label
instructions = tk.Label(root,
                        text="Please enter a MITRE technique identifier (e.g., T1048 or T1048_001 or T1048.001) and click 'Go!':")
instructions.pack(pady=10)

# Create and place the input label and text entry
input_label = tk.Label(root, text="MITRE Technique Identifier:")
input_label.pack(pady=5)
input_text = tk.Entry(root, width=50)
input_text.pack(pady=5)

# Create and place the output text area
output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=15)
output_text.pack(pady=10)

# Create a frame for buttons to align them horizontally
button_frame = tk.Frame(root)
button_frame.pack(pady=5)

# Create and place the Go! button
go_button = tk.Button(button_frame, text="Go!", command=on_go_button_click)
go_button.pack(side=tk.LEFT, padx=5)

# Create and place the Copy to Clipboard button
copy_button = tk.Button(button_frame, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(side=tk.LEFT, padx=5)

# Bind the Enter key to the Go! button
root.bind('<Return>', on_enter_key)

# Start the main loop
root.mainloop()
