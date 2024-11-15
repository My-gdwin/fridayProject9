import tkinter as tk
from tkinter import scrolledtext, messagebox
import openai

# OpenAI API setup
api_key = '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'
openai.api_key = api_key

# Function to interact with OpenAI API
def get_response():
    user_input = user_input_box.get("1.0", tk.END).strip()
    if not user_input:
        messagebox.showwarning("Input Error", "Please enter a message!")
        return
    
    try:
        # OpenAI API call
        completion = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        response = completion.choices[0].message['content']
        response_box.delete("1.0", tk.END)
        response_box.insert(tk.END, response)
    except Exception as e:
        messagebox.showerror("API Error", f"An error occurred: {e}")

# GUI setup
root = tk.Tk()
root.title("OpenAI Chat GUI")

# Input Label
input_label = tk.Label(root, text="Enter your message:")
input_label.pack(pady=5)

# User Input Box
user_input_box = tk.Text(root, height=5, width=50)
user_input_box.pack(pady=5)

# Submit Button
submit_button = tk.Button(root, text="Get Response", command=get_response)
submit_button.pack(pady=5)

# Response Label
response_label = tk.Label(root, text="Response:")
response_label.pack(pady=5)

# Response Display Box
response_box = scrolledtext.ScrolledText(root, height=10, width=50, wrap=tk.WORD)
response_box.pack(pady=5)

# Start the GUI event loop
root.mainloop()