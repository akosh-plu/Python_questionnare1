# secure_test_questions.py
# More secure version - answers are encoded

import base64
import json

# Questions with encoded answers
ENCODED_QUESTIONS = """
W3siaWQiOiAxLCAidG9waWMiOiAic3RyaW5ncyIsICJxdWVzdGlvbiI6ICJXaGF0IGlzIHRoZSBv
dXRwdXQgb2Y6ICdoZWxsbycudXBwZXIoKT8iLCAidHlwZSI6ICJtdWx0aXBsZV9jaG9pY2UiLCAi
b3B0aW9ucyI6IFsiQSkgSEVMTE8iLCAiQikgaGVsbG8iLCAiQykgSGVsbG8iLCAiRCkgSGVMTG8i
XSwgImNvcnJlY3QiOiAiQSJ9LCB7ImlkIjogMiwgInRvcGljIjogInN0cmluZ3MiLCAicXVlc3Rp
b24iOiAiV2hhdCBkb2VzICdweXRob24nWzE6NF0gcmV0dXJuPyIsICJ0eXBlIjogIm11bHRpcGxl
X2Nob2ljZSIsICJvcHRpb25zIjogWyJBKSBweXQiLCAiQikgeXRoIiwgIkMpIHl0aG8iLCAiRCkg
dGhvIl0sICJjb3JyZWN0IjogIkIifSwgeyJpZCI6IDMsICJ0b3BpYyI6ICJsaXN0cyIsICJxdWVz
dGlvbiI6ICJXaGF0IGlzIHRoZSBvdXRwdXQgb2Y6IFsxLCAyLCAzXSArIFs0LCA1XT8iLCAidHlw
ZSI6ICJtdWx0aXBsZV9jaG9pY2UiLCAib3B0aW9ucyI6IFsiQSkgWzEsIDIsIDMsIDQsIDVdIiwg
IkIpIFs1LCA3LCA4XSIsICJDKSBFcnJvciIsICJEKSBbWzEsMiwzXSxbNCw1XV0iXSwgImNvcnJl
Y3QiOiAiQSJ9XQ==
"""

def load_questions():
    """Decode and load questions"""
    decoded = base64.b64decode(ENCODED_QUESTIONS).decode('utf-8')
    return json.loads(decoded)

def check_answer(question_id, user_answer):
    """Check if the user's answer is correct"""
    questions = load_questions()
    question = next((q for q in questions if q["id"] == question_id), None)
    if not question:
        return False
    
    if question["type"] == "short_answer":
        return user_answer.strip().lower() == question["correct"].lower()
    else:
        return user_answer.strip().upper() == question["correct"].upper()

def get_question_for_display(question_id):
    """Get question without the answer"""
    questions = load_questions()
    question = next((q for q in questions if q["id"] == question_id), None)
    if not question:
        return None
    
    display_q = {
        "id": question["id"],
        "topic": question["topic"],
        "question": question["question"],
        "type": question["type"]
    }
    
    if "options" in question:
        display_q["options"] = question["options"]
    
    return display_q
