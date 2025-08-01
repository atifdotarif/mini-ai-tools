# main.py
import tkinter as tk
from tkinter import messagebox, scrolledtext
from blog_generator import generate_blog, save_blog_to_file

def on_generate():
    topic = topic_entry.get().strip()
    if not topic:
        messagebox.showwarning("Input Needed", "Please enter a blog topic.")
        return

    blog = generate_blog(topic)
    output_box.delete(1.0, tk.END)
    output_box.insert(tk.END, blog)

    filename = save_blog_to_file(topic, blog)
    messagebox.showinfo("Saved", f"Blog saved as {filename}")

# Build UI
root = tk.Tk()
root.title("AI Writing Assistant")
root.geometry("700x600")
root.configure(bg="#f4f8fb")

tk.Label(root, text="Enter Blog Topic:", font=("Helvetica", 14), bg="#f4f8fb").pack(pady=10)
topic_entry = tk.Entry(root, font=("Helvetica", 12), width=60)
topic_entry.pack(pady=5)

generate_btn = tk.Button(root, text="Generate Blog", font=("Helvetica", 12), command=on_generate, bg="#007acc", fg="white")
generate_btn.pack(pady=10)

output_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Helvetica", 12), width=80, height=25)
output_box.pack(padx=10, pady=10)

root.mainloop()
