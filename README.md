
# 🧠 Simple GPT Chat UI with Streamlit

I made a super simple GPT-style chat app using **UI4AI**, and **Wrapper4AI**.  
You can run it easily and it looks and feels like ChatGPT — but much lighter!

There are **four versions** you can try based on what you need.

---

## 🚀 What's Inside

| Folder | What it does |
|:-------|:-------------|
| `basic_chat_ui/` | Just a basic chat — no saved conversations |
| `chat_ui_with_titles/` | Chat with stored conversations + auto titles |
| `full_chat_ui_with_token_count/` | Chat with titles + history + token counting |
| `full_chat_ui_with_memsize/` | Chat with everything + bigger memory for long chats |

---

## 🛠 How to Set It Up

1. **Clone the repo**  
   ```bash
   git clone https://github.com/DKethan/simple-ai-ui
   cd simple-gpt-ui
   ```

2. **Install the needed libraries**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Pick a version and run it**  
   Example:
   ```bash
   cd basic_chat_ui
   streamlit run app.py
   ```

That's it! 🎯

## 📚 Quick Look at the Code

Here's basically what’s happening inside:

```python
from UI4AI import run_chat
from Wrapper4AI.wrap import connect

client = connect("openai", "gpt-40", "your-api-key")

run_chat(
    generate_response=client.chat_with_history,
    generate_title=client.generate_title,
    count_tokens=client.count_tokens,
    max_history_tokens=3000
)
```

Small, clean, powerful! ⚡

---

## 💬 Why I Made This

I just wanted a quick way to make a GPT-like chat app without writing too much frontend code.  
Now, with a few lines, you can have a working chat UI with saved conversations, titles, and even token counts!

---

## 🤝 Feel Free to Use It!

If you find this useful, feel free to fork it, use it, improve it, or just play around with it! 🚀

Thanks for reading! 🙌

---

# Tags:
#streamlit #openai #chatgpt #huggingface #python #chatbot

---
