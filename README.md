MITRE Technique Querier
Overview
The MITRE Technique Querier is a simple GUI application built in Python using tkinter and requests. It allows users to fetch and display descriptions of MITRE ATT&CK techniques from the MITRE ATT&CK framework repository.

Features
Input a MITRE technique identifier (e.g., T1003 or T1003.001).
Converts '_' to '.' for flexibility in input.
Fetches and displays the description of the technique.
Responsive GUI with real-time updates.
Installation
Clone the Repository:

bash
Copy code
git clone https://github.com/your-username/mitre-technique-querier.git
cd mitre-technique-querier
Install Dependencies:

Ensure Python 3 is installed on your system.
Install required packages:
bash
Copy code
pip install requests urllib3 tkinter
Usage
Launch the Application:

Run the main.py script:
bash
Copy code
python main.py
The application window will appear on your screen.
Using the Tool:

Enter a MITRE technique identifier in the input field. Use '_' or '.' as separators.
Click the 'Go!' button or press Enter to fetch the technique description.
The description will be displayed in the text area below.
Example Usage:

Enter T1003 or T1003.001 in the input field.
Click 'Go!' to see the description of the technique.
Notes
If an error occurs (e.g., network issues), an error message will be displayed.
Ensure a stable internet connection for fetching technique descriptions from the MITRE ATT&CK repository.
Feedback
Your feedback is valuable! If you encounter any issues or have suggestions for improvement, please create an issue or contact [your contact information].
