from openai import OpenAI
from tkinter import *
import tkinter as tk
from tkinter import Label, Tk

client = OpenAI(
    api_key="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"
)


if __name__ == "__main__":
    
    root=Tk()
    root.title('Chatbot app')
    root.geometry('500x400')
    root.configure(bg='light blue')
    root.resizable(False, False)


    chat_history = Text(root, fg='black', border=2, bg='white', height=17, width=57, font=("cambria", 11))
    chat_history.place(x=10, y=90)
    chat_history.config(state=tk.DISABLED)

    input_label = Label(root, text="Ask chat gpt something").grid(row=0)
    user_input = tk.Entry(root)
    user_input.grid(row=0,column=1)

    # function to request a reply from chat gpt and display it on the UI
    def generate_chatgpt_response():
        if user_input.get() == '':
            return # Can not ask chat gpt stuff using empty input
        response = client.responses.create(
            model='gpt-4o', # Model can be chosen here
            input=user_input.get()
        )
        chat_history.config(state=tk.NORMAL)
        chat_history.insert(tk.END, f"You: {user_input.get()}\n\n")
        chat_history.insert(tk.END, f"Chat gpt: {response.output_text}\n\n")
        chat_history.config(state=tk.DISABLED)
        user_input.delete(0, tk.END)

    ask = Button(root, width=25, pady=5, text="Click to ask", fg='black', command=generate_chatgpt_response).grid(row=0,column=2)


    root.mainloop()

