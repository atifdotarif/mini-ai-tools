# 🧠 mini-ai-tools

A collection of lightweight, OpenAI-powered desktop applications built using Python and Tkinter. This suite includes tools to assist with writing, sentiment analysis, and resume generation — ideal for students, professionals, and developers looking for quick AI utilities.

## 🚀 Features

### 1. ✍️ AI Writing Assistant
- Generate short, structured blog posts (~50–60 words)
- Engaging, high-quality content with headings and conclusion
- Automatically saves the output to a text file

### 2. 😊 Sentiment Analyzer
- Input any sentence or short paragraph
- Classifies sentiment as **Positive**, **Negative**, or **Neutral**
- Saves the analysis to a text file

### 3. 📄 Smart Resume Builder
- Enter a brief "Tell me about yourself"
- Automatically structures and enhances it into a clean resume
- Interactive UI with themes
- Export to **PDF** and **Text** formats

## 🛠️ Tech Stack

- **Python >=3.8**
- [OpenAI API](https://platform.openai.com/)
- `Tkinter` for GUI
- `fpdf` for PDF export
- `dotenv` for API key management

## 📦 Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/atifdotarif/mini-ai-tools.git
cd mini-ai-tools
```
2. **Install dependencies**
```bash
pip install -r requirements.txt
```
3. **Set up your .env file**
Create a .env file in the root directory and add your OpenAI API key:
OPEN_API_KEY=your_openai_api_key

4. **Run an application**
Each tool can be launched independently:
```bash
python AIBlogWritingAssistant/main.py
```
```bash
python sentiment_analyzer/main.py
```
```bash
python ResumeBuilder/main.py
```


**💡 Built during AI Internship @ Sharkstack**
**by Atif Arif😊**
