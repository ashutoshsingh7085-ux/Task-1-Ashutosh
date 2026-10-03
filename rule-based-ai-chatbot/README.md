# 🤖 Rule-Based AI Chatbot

> **DecodeLabs · AI Industrial Training Kit · Project 1 (Batch 2026)**
> Foundation phase: control flow, decision-making logic, and basic AI concepts.

A simple, deterministic chatbot that replies to predefined user inputs. No machine learning, just clean logic you can trace from input to output (a "white box").

## ✨ Features

- **Continuous loop**: `while True` keeps the bot alive until the exit command
- **Input sanitization**: handles case, extra whitespace, and trailing punctuation
- **Knowledge base**: dictionary with 10+ intents (greetings, small talk, AI facts)
- **Fallback response**: graceful default for unknown inputs via `dict.get()`
- **Clean exit**: `exit`, `quit`, `bye`, or `goodbye` ends the session (Ctrl+C / Ctrl+D also handled)
- **Unit tests** included

## 🧠 Architecture (IPO Model)

| Phase | Responsibility | Code |
|-------|----------------|------|
| **Input** | Sanitization & normalization | `sanitize()` |
| **Process** | Intent matching via hash map, O(1) | `RESPONSES.get(...)` |
| **Output** | Response generation & feedback loop | `main()` loop |

### Why a dictionary instead of an `if-elif` ladder?

An `if-elif` chain scans rules one by one (**O(n)**) and becomes hard to maintain as rules grow. A dictionary gives **O(1)** lookup, and `.get(key, default)` handles lookup and fallback in a single atomic operation.

## 🚀 Getting Started

Requires **Python 3.8+** (no external dependencies).

```bash
git clone https://github.com/<your-username>/rule-based-ai-chatbot.git
cd rule-based-ai-chatbot
python chatbot.py
```

### Example session

```
DecoBot: Hello! I'm DecoBot. Type 'help' for ideas or 'exit' to quit.
You:   HELLO!
DecoBot: Hi there! How can I help you today?
You: what is AI?
DecoBot: Artificial Intelligence is the simulation of human intelligence by machines.
You: pizza
DecoBot: I do not understand. Type 'help' to see what I can answer.
You: exit
DecoBot: Goodbye! Have a great day.
```

## 🧪 Run Tests

```bash
python -m unittest -v
```

## ➕ Add Your Own Rules

Edit the `RESPONSES` dictionary in `chatbot.py`. Keys must be **lowercase with no trailing punctuation**:

```python
RESPONSES["what is python"] = "Python is a beginner-friendly programming language."
```

## ✅ Project Checklist

- [x] **Input loop**: continuous `while` cycle
- [x] **Sanitization**: handle case & whitespace
- [x] **Knowledge base**: dictionary with 5+ intents
- [x] **Fallback**: default response for unknowns
- [x] **Exit strategy**: clean `break` command

## 🔭 Ideas to Extend

- Add nested conditions or simple multi-turn state (e.g., remember the user's name)
- Give the bot a unique personality
- Keyword matching (e.g., "hello there" → `hello`)
- **Project 2**: move from exact-match keys to semantic vectors
- **Hybrid architecture**: rules first for instant answers, then pass unmatched queries to an LLM

## 📁 Structure

```
rule-based-ai-chatbot/
├── chatbot.py        # Bot logic
├── test_chatbot.py   # Unit tests
├── README.md
├── LICENSE
└── .gitignore
```

## 📄 License

MIT. See [LICENSE](LICENSE).

---
*Powered by DecodeLabs*
