# main.py
import tkinter as tk
from tkinter import messagebox
from sentiment_analyzer import analyze_sentiment, save_result

def analyze():
    sentence = input_text.get("1.0", "end").strip()
    if not sentence:
        messagebox.showwarning("Input Missing", "Please enter a sentence.")
        return

    sentiment = analyze_sentiment(sentence)
    result_label.config(text=f"Sentiment: {sentiment}", fg="green")
    
    filename = save_result(sentence, sentiment)
    messagebox.showinfo("Saved", f"Sentiment saved to file:\n{filename}")

# GUI
root = tk.Tk()
root.title("AI Sentiment Analyzer")
root.geometry("400x350")
root.configure(bg="#f0f4f8")

tk.Label(root, text="Enter a sentence:", font=("Arial", 12), bg="#f0f4f8").pack(pady=(10, 5))

input_text = tk.Text(root, height=5, width=40, font=("Arial", 10))
input_text.pack(pady=5)

tk.Button(root, text="Analyze Sentiment", command=analyze, bg="#007acc", fg="white", font=("Arial", 11)).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"), bg="#f0f4f8")
result_label.pack(pady=5)

root.mainloop()
