from flask import Flask, render_template, redirect, url_for, flash
from form import RegistrationForm
import os
app = Flask(__name__)
app.secret_key = 'mysecretkey'  # CSRF protection key

@app.route("/", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Here you can add code to save the user info to a database
        flash(f"Successfully Registered! Name: {form.name.data}, Email: {form.email.data}", "success")
        return redirect(url_for('register'))
    return render_template("reg.html", form=form)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # ✅ this makes it work on Render
    app.run(debug=True, host="0.0.0.0", port=port)
