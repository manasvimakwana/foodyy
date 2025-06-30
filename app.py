from flask import Flask, render_template, request, redirect, url_for, flash
app = Flask(__name__)
app.secret_key = "your_secret_key"  # needed for flashing messages
@app.route('/')
def home():
    return render_template('index.html')
  
@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form.get('name')
        rating = request.form.get('rating')
        comments = request.form.get('comments')
        
        # You can store the feedback in DB or send it via email
        flash("Thank you for your feedback!")
        return redirect(url_for('feedback'))

    return render_template('feedback.html')

if __name__ == "__main__":
    app.run(debug=True)