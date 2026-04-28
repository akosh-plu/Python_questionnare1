from flask import Flask, render_template, request, redirect, url_for, session
import test_questions

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Required for sessions

@app.route('/')
def index():
    # Reset the test state
    session['score'] = 0
    session['current_q'] = 1
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    q_id = session.get('current_q', 1)
    
    if request.method == 'POST':
        user_answer = request.form.get('answer')
        
        # Grade the answer using your existing function
        if test_questions.check_answer(q_id, user_answer):
            session['score'] += 1
        
        # Move to next question or finish
        session['current_q'] += 1
        if session['current_q'] > 25:
            return redirect(url_for('results'))
        
        return redirect(url_for('quiz'))

    # Get question data from your test_questions.py
    question_data = test_questions.get_question_for_display(q_id)
    return render_template('quiz.html', q=question_data, q_num=q_id)

@app.route('/results')
def results():
    score = session.get('score', 0)
    return render_template('results.html', score=score)

if __name__ == '__main__':
    app.run(debug=True)