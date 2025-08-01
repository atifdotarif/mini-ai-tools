import tkinter as tk
from tkinter import messagebox, scrolledtext, filedialog
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import textwrap
from resume_builder import generate_resume

# UI Theme
BG_COLOR = "#f4f4f4"
HEADER_COLOR = "#1a73e8"
TEXT_COLOR = "#333"
BTN_COLOR = "#1a73e8"
BTN_TEXT = "#fff"

root = tk.Tk()
root.title("AI Resume Builder")
root.geometry("800x700")
root.configure(bg=BG_COLOR)

generated_resume = None

def wrap_text(text, width):
    return textwrap.wrap(text, width)

def display_resume(data):
    output_box.delete("1.0", tk.END)
    for key, value in data.items():
        output_box.insert(tk.END, f"{key.capitalize()}\n", "title")
        if isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    for k, v in item.items():
                        output_box.insert(tk.END, f"  • {k.capitalize()}: {v}\n", "text")
                else:
                    output_box.insert(tk.END, f"  • {item}\n", "text")
        elif isinstance(value, dict):
            for k, v in value.items():
                output_box.insert(tk.END, f"  • {k.capitalize()}: {v}\n", "text")
        else:
            output_box.insert(tk.END, f"  {value}\n", "text")
        output_box.insert(tk.END, "\n")

def handle_generate():
    global generated_resume
    name = name_entry.get().strip()
    about = about_text.get("1.0", tk.END).strip()
    if not name or not about:
        messagebox.showwarning("Input Required", "Please enter your name and about yourself.")
        return
    try:
        generated_resume = generate_resume(name, about)
        display_resume(generated_resume)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate resume:\n{str(e)}")

def export_to_pdf():
    if not generated_resume:
        messagebox.showwarning("No Resume", "Please generate a resume first.")
        return
    filename = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if not filename:
        return
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    y = height - 50
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, "AI-Generated Resume")
    y -= 30
    c.setFont("Helvetica", 12)
    for key, value in generated_resume.items():
        c.setFont("Helvetica-Bold", 13)
        c.drawString(50, y, key.capitalize() + ":")
        y -= 20
        c.setFont("Helvetica", 11)
        if isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    for subkey, subval in item.items():
                        lines = wrap_text(f"{subkey.capitalize()}: {subval}", 90)
                        for line in lines:
                            c.drawString(60, y, line)
                            y -= 15
                else:
                    for line in wrap_text(str(item), 90):
                        c.drawString(60, y, f"• {line}")
                        y -= 15
        elif isinstance(value, dict):
            for subkey, subval in value.items():
                for line in wrap_text(f"{subkey.capitalize()}: {subval}", 90):
                    c.drawString(60, y, line)
                    y -= 15
        else:
            for line in wrap_text(str(value), 90):
                c.drawString(60, y, line)
                y -= 15
        y -= 10
        if y < 100:
            c.showPage()
            y = height - 50
    c.save()
    messagebox.showinfo("Success", f"PDF saved as {filename}")

def export_to_txt():
    if not generated_resume:
        messagebox.showwarning("No Resume", "Please generate a resume first.")
        return
    filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if not filename:
        return
    with open(filename, "w", encoding="utf-8") as f:
        for key, value in generated_resume.items():
            f.write(f"{key.capitalize()}:\n")
            if isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        for subkey, subval in item.items():
                            f.write(f"  - {subkey.capitalize()}: {subval}\n")
                    else:
                        f.write(f"  - {item}\n")
            elif isinstance(value, dict):
                for subkey, subval in value.items():
                    f.write(f"  - {subkey.capitalize()}: {subval}\n")
            else:
                f.write(f"  {value}\n")
            f.write("\n")
    messagebox.showinfo("Success", f"Text file saved as {filename}")

# === UI Layout ===

tk.Label(root, text="AI Resume Builder", font=("Helvetica", 20, "bold"), bg=BG_COLOR, fg=HEADER_COLOR).pack(pady=10)

frame = tk.Frame(root, bg=BG_COLOR)
frame.pack(pady=10)

tk.Label(frame, text="Full Name:", font=("Helvetica", 12), bg=BG_COLOR, fg=TEXT_COLOR).grid(row=0, column=0, sticky="w")
name_entry = tk.Entry(frame, font=("Helvetica", 12), width=40)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame, text="Tell me about yourself:", font=("Helvetica", 12), bg=BG_COLOR, fg=TEXT_COLOR).grid(row=1, column=0, sticky="nw", pady=5)
about_text = scrolledtext.ScrolledText(frame, width=60, height=5, font=("Helvetica", 11))
about_text.grid(row=1, column=1, pady=5)

btn_frame = tk.Frame(root, bg=BG_COLOR)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Generate Resume", font=("Helvetica", 12, "bold"), bg=BTN_COLOR, fg=BTN_TEXT, command=handle_generate).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Export to PDF", font=("Helvetica", 12, "bold"), bg="#34a853", fg=BTN_TEXT, command=export_to_pdf).grid(row=0, column=1, padx=10)
tk.Button(btn_frame, text="Export to Text", font=("Helvetica", 12, "bold"), bg="#fbbc05", fg=BTN_TEXT, command=export_to_txt).grid(row=0, column=2, padx=10)

output_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Helvetica", 11), width=90, height=25)
output_box.pack(pady=10)
output_box.tag_configure("title", font=("Helvetica", 13, "bold"), foreground=HEADER_COLOR)
output_box.tag_configure("text", font=("Helvetica", 11), foreground=TEXT_COLOR)

root.mainloop()