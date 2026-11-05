# PyBot - Simple Rule-Based Chatbot

**Internship:** Pynexia Technology  
**Domain:** Artificial Intelligence  
**Project:** Simple Rule-Based Chatbot  
**Interface:** Python terminal application

## 1. Project objective

Build a text-based chatbot that accepts user messages, cleans the text, identifies keywords/patterns, and returns predefined responses using if-then rules and intent mappings.

## 2. Requirements covered

1. **Input and text cleaning:** accepts terminal input, converts it to lowercase, removes punctuation, and normalizes spaces.
2. **Pattern matching:** uses Python's `re` module and regular expressions to identify intents.
3. **If-then rules and intent mappings:** maps recognized intents to predefined responses.
4. **Conversational flow:** keeps running until the user types a farewell such as `bye`, and stores the conversation turns during the session.

## 3. Project structure

```text
Pynexia_Rule_Based_Chatbot/
│
├── chatbot.py
├── README.md
├── requirements.txt
└── tests/
    └── test_chatbot.py
```

## 4. Software required

- Python 3.8 or newer
- VS Code, IDLE, or another Python editor
- Terminal / Command Prompt

No third-party packages are required.

## 5. How to run

1. Extract the ZIP file.
2. Open the project folder in VS Code or a terminal.
3. Run:

```bash
python chatbot.py
```

If your computer uses the `py` command on Windows, run:

```bash
py chatbot.py
```

## 6. Example questions

- `Hello`
- `What is your name?`
- `What can you do?`
- `Tell me about Python`
- `What is Artificial Intelligence?`
- `Explain Machine Learning`
- `Tell me about internships`
- `What is the time?`
- `What is today's date?`
- `Thank you`
- `Bye`

## 7. How the chatbot works

1. The user enters a message.
2. `clean_text()` normalizes the message.
3. `detect_intent()` checks the cleaned message against regular-expression patterns.
4. `generate_response()` selects a predefined response for the detected intent.
5. The chatbot prints the response and saves the turn in the session's conversation history.
6. The loop continues until a goodbye intent is detected.

## 8. Testing

Run the automated tests from the project folder:

```bash
python -m unittest discover -s tests -v
```

The tests check text cleaning, greeting detection, Python-topic detection, unknown input handling, and response generation.

## 9. Limitations

- This is a rule-based chatbot, not a machine-learning or generative-AI model.
- It can only answer topics covered by its predefined patterns and responses.
- Conversation history is kept in memory only and is cleared when the program closes.

## 10. Conclusion

PyBot demonstrates basic chatbot development using Python, regular expressions, keyword matching, intent mapping, conditional response generation, and a continuous text-based conversation loop.
