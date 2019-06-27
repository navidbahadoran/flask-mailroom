import os
from flask import Flask
from flask_login import LoginManager
from flask import render_template, request, redirect, url_for, session, flash
from form import RegistrationForm, LoginForm, CreateForm, SingleUserForm
from model import Donation, Donor

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY').encode()
login_manager = LoginManager(app)


@app.route('/')
@app.route('/home')
def home():
    return redirect(url_for('all_donation'))


@app.route('/donations')
def all_donation():
    message = request.args.get('user')
    if message:
        donor = Donor.select().where(Donor.name == message).get()
        donations = Donation.select().where(Donation.donor == donor)
        name = donor.name.title()
    else:
        donations = Donation.select()
        name = "All"
    return render_template('donations.jinja2', title='show all', name=name, donations=donations)


@app.route('/create', methods=['POST', 'GET'])
def create():
    if 'username' not in session:
        return redirect(url_for('login'))
    form = CreateForm()
    if form.validate_on_submit():
        flash(f'Thank you for your donation of {form.donation.data}.', 'success')
        user = Donor.select().where(Donor.username == session['username']).get()
        Donation(value=form.donation.data, donor=user).save()
        return redirect(url_for('all_donation'))
    return render_template('create_new.jinja2', title='create', form=form)


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_donor = Donor(username=form.username.data, name=form.name.data, password=form.password.data)
        new_donor.save()
        flash(f'Account created for {form.name.data}!, you can now log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.jinja2', title='register', form=form)


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = Donor.select().where(Donor.username == form.username.data)
        password = Donor.select().where(Donor.password == form.password.data)
        if username and password:
            flash(f'You have been logged in', 'success')
            session['username'] = form.username.data
            return redirect(url_for('create'))
        else:
            flash(f'Login Unsuccessful, Please check username and password', 'danger')
            return render_template('login.jinja2', title='login', form=form)
    return render_template('login.jinja2', title='login', form=form)


@app.route('/single_user', methods=['POST', 'GET'])
def single_user():
    form = SingleUserForm()
    if form.validate_on_submit():
        return redirect(url_for('all_donation', user=form.name.data))
    return render_template('single.jinja2', tittle='single_user', form=form)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
