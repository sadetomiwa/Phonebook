from app import app, db
from flask import render_template, redirect, url_for, flash
from app.forms import AddContactForm, SignUpForm, LoginForm, SearchForm
from app.models import Address, Users
from flask_login import login_user, logout_user, login_required, current_user




@app.route('/')
def index():
    addresses = Address.query.all()
    form = SearchForm()
    if form.validate_on_submit():
        search_term = form.search_term.data
        addresses = db.session.execute(db.select(Address).where((Address.first_name.ilike(f"%{search_term}%")) | (Address.last_name.ilike(f"%{search_term}%")))).scalars().all()
    return render_template('index.html', addresses=addresses, form=form)




@app.route('/view')
def view():
    addresses = Address.query.all()
    return render_template('view.html', addresses = addresses)

    

@app.route('/contacts', methods=['GET', 'POST'])
@login_required
def contacts():
    form = AddContactForm()
    if form.validate_on_submit():
        print('Sweet! The contact has been added')
        first_name = form.first_name.data
        last_name = form.last_name.data
        phone = form.phone.data
        address = form.address.data
        new_contact = Address(first_name=first_name, last_name=last_name, phone=phone, address=address, user_id=current_user.id)
        flash(f"{new_contact.first_name} {new_contact.last_name} has been added to the rolodex")
        return redirect (url_for('index'))
    return render_template('contacts.html', form = form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        print('Sweet! Youve successfully signed up')
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        username = form.username.data
        password = form.password.data
        print(first_name, last_name, email, username, password)
        check_user = db.session.execute(db.select(Users).filter((Users.username == username) | (Users.email == email))).scalars().all()
        if check_user:
            flash(f"A user with that username/email already exists", "danger")
            return redirect(url_for('signup'))
        new_user = Users(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
        flash(f" Thank you {new_user.username} for signing up!", "success")
    return render_template('signup.html', form = form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    login_user 
    if form.validate_on_submit():
        print('Sweet! Youve successfully logged in')
        username = form.username.data
        password = form.password.data
        print(username, password)
        user = Users.query.filter( username == username).first()
        if user is not None and user.check_password:
            login_user(user)
            flash(f" You have successfully logged in as {username}", "success")
            return redirect(url_for('index'))
        else:
            flash(f"Invalid username or password", "danger")
            return redirect(url_for('login'))
    return render_template('login.html', form = form)
    


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    flash("You have successfully logged out", "success")
    return redirect(url_for('index'))

    

@app.route('/edit/<address_id>', methods=['GET', 'POST'])
@login_required
def edit_contact(address_id):
    form = AddContactForm()
    address_edit = Address.query.get_or_404(address_id)
    if address_edit.user != current_user:
        flash("You are not authorized to edit this contact", "danger")
        return redirect(url_for('view'))
    if form.validate_on_submit():
        address_edit.first_name = form.first_name.data
        address_edit.last_name = form.last_name.data
        address_edit.phone = form.phone.data
        address_edit.address = form.address.data
        db.session.commit()
        flash(f"{address_edit.first_name} {address_edit.last_name} has benn edited", "success")
        return redirect(url_for('view'))
    
    form.first_name.data = address_edit.first_name
    form.last_name.data = address_edit.last_name
    form.phone.data = address_edit.phone
    form.address.data = address_edit.address
    return render_template('edit.html', form= form, addresses = address_edit)
    

@app.route('/delete/<address_id>', methods=['GET', 'POST'])
@login_required
def delete_contact(address_id):
    address_delete = Address.query.get_or_404(address_id)
    if address_delete.user_id!= current_user:
        flash("You are not authorized to delete this contact", "danger")
        return redirect(url_for('view'))
    db.session.delete(address_delete)
    db.session.commit()
    flash(f"{address_delete.first_name} {address_delete.last_name} has been deleted", "success")
    return redirect(url_for('view'))















 
