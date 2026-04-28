# Python Test System - Teacher Guide

## Overview
This system allows you to create Python knowledge tests where students can see the test-taking code but NOT the questions and answers.

## Files Structure

### FOR TEACHER ONLY (Don't share):
- `test_questions.py` - Contains all questions and answers (simple version)
- `secure_test_questions.py` - Contains encoded questions (more secure)
- `encode_questions.py` - Helper to encode your own questions

### FOR STUDENTS (Share this):
- `python_test.py` - The test runner code students will execute

## How It Works

### Method 1: Simple Separation (test_questions.py)
1. Questions are in a separate file
2. Test runner imports the questions module
3. Students only receive `python_test.py`
4. They can't see answers without the `test_questions.py` file

**Pros**: Simple, easy to modify
**Cons**: If students get the questions file, they can see answers

### Method 2: Encoded Questions (secure_test_questions.py)
1. Questions are base64 encoded
2. Harder for students to decode
3. More secure but still not foolproof

**Pros**: More secure, harder to decode
**Cons**: More complex to manage

## Setup Instructions

### For Teachers:

1. **Edit your questions** in `test_questions.py`:
   ```python
   QUESTIONS = [
       {
           "id": 1,
           "topic": "strings",
           "question": "Your question here?",
           "type": "multiple_choice",
           "options": ["A) Answer 1", "B) Answer 2", ...],
           "correct": "A"
       },
       # Add more questions...
   ]
   ```

2. **Update the total_questions** in `python_test.py`:
   ```python
   self.total_questions = 10  # Change to your number of questions
   ```

3. **Share only** `python_test.py` with students

4. **Keep on your machine**:
   - `test_questions.py`
   - Students must run the test where both files exist

### For Students:

1. Run the test:
   ```bash
   python python_test.py
   ```

2. Answer each question as prompted

3. Get your grade at the end

## Question Types

### Multiple Choice
```python
{
    "id": 1,
    "topic": "strings",
    "question": "What is the output of: 'hello'.upper()?",
    "type": "multiple_choice",
    "options": ["A) HELLO", "B) hello", "C) Hello", "D) HeLLo"],
    "correct": "A"
}
```

### Short Answer
```python
{
    "id": 4,
    "topic": "lists",
    "question": "How do you add an item to the end of a list?",
    "type": "short_answer",
    "correct": "append"
}
```

## Distribution Methods

### Method 1: Email python_test.py only
Students run it on a computer where you've already placed test_questions.py

### Method 2: Online testing environment
Upload both files to a server, students access via web terminal

### Method 3: In-class testing
Install both files on classroom computers beforehand

### Method 4: Use .pyc compiled files
Compile test_questions.py to bytecode:
```bash
python -m py_compile test_questions.py
```
Share the .pyc file instead (harder to read)

## Grading Scale

- A (90-100%): Excellent
- B (80-89%): Good
- C (70-79%): Satisfactory
- D (60-69%): Needs improvement
- F (<60%): Review required

## Customization

You can modify:
- Number of questions
- Topics covered
- Grading thresholds
- Display messages
- Question formats

## Security Notes

**This is NOT foolproof!** Determined students can:
- Read the test_questions.py file if they get access
- Decode base64 strings
- Decompile .pyc files

For high-stakes testing:
- Use an online testing platform
- Randomize question order
- Use question pools
- Time limits
- Proctoring

For classroom learning, this system is perfectly adequate!
