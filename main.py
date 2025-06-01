from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    q1 = None
    q2 = []
    q3 = None
    q4 = None
    q5 = None
    if request.method == 'POST':
        q1 = request.form.get('q1')
        q2 = request.form.getlist('q2')  # getlist для чекбоксов
        q3 = request.form.get('q3')
        q4 = request.form.get('q4')
        q5 = request.form.get('q5')
    return render_template('fixed_index.html', q1=q1, q2=q2, q3=q3, q4=q4, q5=q5)
if __name__ == "__main__":
    app.run(debug=True)
