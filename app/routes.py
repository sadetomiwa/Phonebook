from app import app
from flask import render_template, redirect, url_for, flash
from app.forms import AddContactForm 




@app.route('/')
def index():
    return render_template('index.html')


@app.route('/contacts', methods=['GET', 'POST'])
def contacts():
    form = AddContactForm()
    if form.validate_on_submit():
        print('Sweet! The contact has been added')
        first_name = form.first_name.data
        last_name = form.last_name.data
        phone = form.phone.data
        address = form.address.data
        print(first_name, last_name, phone, address)
        flash(f"{first_name} {last_name} has been added to the rolodex")
        return redirect (url_for('index'))
    return render_template('contacts.html', form = form)





 
