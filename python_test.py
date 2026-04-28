# python_test.py
# This file can be shared with students

import test_questions  # This imports the hidden questions file

class PythonTest:
    """A test system for Python topics"""
    
    def __init__(self):
        self.score = 0
        self.total_questions = 25
    
        self.answers = {}
    
    def display_question(self, question_num):
        """Display a question to the student"""
        question = test_questions.get_question_for_display(question_num)
        
        if not question:
            print(f"Question {question_num} not found!")
            return
        
        print(f"\n{'='*60}")
        print(f"Question {question['id']} - Topic: {question['topic'].upper()}")
        print(f"{'='*60}")
        print(question['question'])
        
        if question['type'] == 'multiple_choice' and 'options' in question:
            print()
            for option in question['options']:
                print(f"  {option}")
        
        print()
    
    def submit_answer(self, question_num, answer):
        """Submit an answer for a question"""
        self.answers[question_num] = answer
        print(f"Answer recorded for question {question_num}")
    
    def take_test(self):
        """Interactive test-taking mode"""
        print("\n" + "="*60)
        print("PYTHON KNOWLEDGE TEST")
        print("="*60)
        print(f"Total Questions: {self.total_questions}")
        print("For multiple choice, enter the letter (A, B, C, or D)")
        print("For short answer, type your answer")
        print("="*60)
        
        for i in range(1, self.total_questions + 1):
            self.display_question(i)
            answer = input("Your answer: ").strip()
            self.submit_answer(i, answer)
        
        self.grade_test()
    
    def grade_test(self):
        """Grade the test and show results"""
        print("\n" + "="*60)
        print("GRADING YOUR TEST...")
        print("="*60)
        
        correct = 0
        for question_num, user_answer in self.answers.items():
            is_correct = test_questions.check_answer(question_num, user_answer)
            if is_correct:
                correct += 1
        
        self.score = correct
        percentage = (correct / self.total_questions) * 100
        
        print(f"\nYou got {correct} out of {self.total_questions} correct!")
        print(f"Score: {percentage:.1f}%")
        
        if percentage >= 90:
            print("Grade: A - Excellent work! 🎉")
        elif percentage >= 80:
            print("Grade: B - Good job! 👍")
        elif percentage >= 70:
            print("Grade: C - Not bad, keep practicing! 📚")
        elif percentage >= 60:
            print("Grade: D - You need more practice 📖")
        else:
            print("Grade: F - Please review the material 📝")
        
        print("="*60)


# Example usage - Students will run this
if __name__ == "__main__":
    test = PythonTest()
    test.take_test()
