# fridayProject9
# OpenAI Chat GUI

This project is a simple GUI application that allows users to interact with OpenAI's API. Users can input messages, and the application retrieves responses using the OpenAI GPT model. The interface is built using Python's `tkinter` library.

---

## Setup Instructions

### 1. Create a `.env` File
To securely store your OpenAI API key, create a `.env` file in the same directory as the Python script. Follow these steps:
1. Open a text editor.
2. Add the following line to the file, replacing `'YOUR_API_KEY'` with your actual OpenAI API key:
   ```plaintext
   key='YOUR_API_KEY'
   ```
3. Save the file as `.env` (no file extension).

### 2. Install Dependencies
Ensure you have Python installed. Then, install the required Python libraries:
```bash
pip install openai python-dotenv
```

---

## Running the Application

1. Run the Python script:
   ```bash
   python <script_name>.py
   ```
   Replace `<script_name>` with the name of the Python file, e.g., `app.py`.

2. The GUI window will open. Follow these steps:
   - **Input Message:** Enter a message in the text box labeled "Enter your message."
   - **Submit Message:** Click the "Get Response" button.
   - **View Response:** The response from OpenAI will appear in the "Response" box. This box is read-only.

---

## Code Functionality

### Key Features:
1. **User Input Box:** Allows the user to type a message.
2. **Submit Button:** Sends the user input to the OpenAI API.
3. **Response Display Box:** Displays the API response. It is non-editable to ensure integrity.
4. **Error Handling:** Alerts the user in case of issues such as missing input or API errors.

### API Interaction:
- The application uses OpenAI's `ChatCompletion` API with the `gpt-4o-mini` model.
- A system message configures the assistant's behavior as "You are a helpful assistant."

---

## File Structure
- `app.py`: The main Python script containing the GUI code.
- `.env`: File storing the OpenAI API key.

---

## Troubleshooting

### Common Issues:
1. **API Key Missing or Invalid:**
   - Ensure the `.env` file exists and contains the `key='YOUR_API_KEY'`.
   - Verify that the API key is correct and active in your OpenAI account.

2. **Missing Dependencies:**
   - Run `pip install openai python-dotenv` to install missing libraries.

3. **Error Message:**
   - If an error occurs during API interaction, ensure your internet connection is active and the API key has sufficient credits.

---

## License
This project is open-source and available under the MIT License. 

---

## Acknowledgments
- [OpenAI API Documentation](https://platform.openai.com/docs/)
- Python's `tkinter` library for GUI development.