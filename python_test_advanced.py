# python_test_advanced.py
# Advanced version with randomized questions
# This file can be shared with students

import test_questions
import random

class AdvancedPythonTest:
    """Advanced test system with randomization"""
    
    def __init__(self, num_questions=25, randomize=True):
        self.total_questions = num_questions
        self.randomize = randomize
        self.score = 0
        self.answers = {}
        self.question_order = list(range(1, num_questions + 1))
        
        if randomize:
            random.shuffle(self.question_order)
    
    def display_question(self, question_num, display_num):
        """Display a question to the student"""
        question = test_questions.get_question_for_display(question_num)
        
        if not question:
            print(f"Question {question_num} not found!")
            return
        
        print(f"\n{'='*60}")
        print(f"Question {display_num} of {self.total_questions} - Topic: {question['topic'].upper()}")
        print(f"{'='*60}")
        print(question['question'])
        
        if question['type'] == 'multiple_choice' and 'options' in question:
            print()
            options = question['options'].copy()
            if self.randomize:
                random.shuffle(options)
            for option in options:
                print(f"  {option}")
        
        print()
    
    def submit_answer(self, question_num, answer):
        """Submit an answer for a question"""
        self.answers[question_num] = answer
    
    def take_test(self):
        """Interactive test-taking mode"""
        print("\n" + "="*60)
        print("PYTHON KNOWLEDGE TEST - ADVANCED")
        print("="*60)
        print(f"Total Questions: {self.total_questions}")
        if self.randomize:
            print("Questions are randomized for each student")
        print("\nFor multiple choice, enter the letter (A, B, C, or D)")
        print("For short answer, type your answer")
        print("="*60)
        
        for i, question_num in enumerate(self.question_order, 1):
            self.display_question(question_num, i)
            answer = input("Your answer: ").strip()
            self.submit_answer(question_num, answer)
        
        self.grade_test()
    
    def grade_test(self):
        """Grade the test and show results"""
        print("\n" + "="*60)
        print("GRADING YOUR TEST...")
        print("="*60)
        
        correct = 0
        topic_scores = {}
        
        for question_num, user_answer in self.answers.items():
            is_correct = test_questions.check_answer(question_num, user_answer)
            
            # Track by topic
            q = test_questions.get_question_for_display(question_num)
            topic = q['topic']
            if topic not in topic_scores:
                topic_scores[topic] = {'correct': 0, 'total': 0}
            
            topic_scores[topic]['total'] += 1
            
            if is_correct:
                correct += 1
                topic_scores[topic]['correct'] += 1
        
        self.score = correct
        percentage = (correct / self.total_questions) * 100
        
        print(f"\n📊 OVERALL RESULTS:")
        print(f"You got {correct} out of {self.total_questions} correct!")
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
        
        # Show performance by topic
        print(f"\n📚 PERFORMANCE BY TOPIC:")
        for topic, scores in sorted(topic_scores.items()):
            topic_pct = (scores['correct'] / scores['total']) * 100
            print(f"  {topic.upper()}: {scores['correct']}/{scores['total']} ({topic_pct:.0f}%)")
        
        # Suggestions
        print(f"\n💡 SUGGESTIONS:")
        weak_topics = [topic for topic, scores in topic_scores.items() 
                      if (scores['correct'] / scores['total']) < 0.7]
        
        if weak_topics:
            print(f"  Review these topics: {', '.join(weak_topics)}")
        else:
            print("  Great job! Keep up the good work!")
        
        print("="*60)


# Example usage
if __name__ == "__main__":
    # You can customize these parameters:
    # num_questions: How many questions to ask (max 10 in current question bank)
    # randomize: Whether to randomize question order
    
    test = AdvancedPythonTest(num_questions=25, randomize=True)
    test.take_test()
