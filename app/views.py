from flask import render_template, flash  ,url_for, redirect, request
from app import app,db
from app.models import User, Post
from .forms import SignupForm, SigninForm, ForgotPasswordForm, PostForm
from flask_login import login_user, logout_user, current_user, login_required
import os
from datetime import datetime



ROWS_PER_PAGE = 6

@app.route("/")
@app.route("/index")
@login_required
def index():
    page_number=int(request.args.get('page', 1))
    all_posts=Post.query.order_by(Post.date.desc()).paginate(page=page_number, per_page=ROWS_PER_PAGE )
    
    return render_template('index.html', title='index_page' , all_posts=all_posts)



@app.route("/signup", methods=['GET', 'POST'])
def signup():
    registerform = SignupForm()
    if request.method == 'POST':
        if registerform.validate_on_submit():
            username=registerform.username.data
            email=registerform.email.data
            password=registerform.password.data
            joined=datetime.utcnow()
            status='Active'
            Usertype='Author'
            last_time_seen=datetime.utcnow()
            if User.query.filter_by(username=username).first() != None:
                flash("That username is already taken...please choose another.", "danger")
            elif User.query.filter_by(email=email).first() != None:
                flash("That email is already taken...please choose another.", "danger")
            else:
                user=User(username=username, email=email, password=password, joined=joined, 
                status=status, Usertype=Usertype, last_time_seen=last_time_seen)
                db.session.add(user)
                db.session.commit()
                flash(f'Congratulation!!! Account has been created for {username}.', 'success')
                return redirect(url_for('signin'))

    return render_template('signup.html', title='Register_page', registerform=registerform)




@app.route("/signin", methods=['GET', 'POST'])
def signin():
    loginform = SigninForm()
    if request.method == 'POST':
        if loginform.validate_on_submit():
            password=loginform.password.data
            email=loginform.email.data
            legit_user=User.query.filter_by(email=email, password=password).first()
            if legit_user is None: 
                flash('Sign in failed , check your username and password.', 'danger')
                return redirect(url_for('signin'))
            else:
                login_user(legit_user, remember=loginform.remember_me.data)
                flash(f'Hello, {legit_user.username}','success')
                return redirect(url_for('index'))

    return render_template('signin.html', title='Login_page', loginform=loginform)

@app.route("/admin", methods=['GET', 'POST'])
@login_required
def admin():
    users=User.query.order_by(User.last_time_seen.desc()).all()
    return render_template('admin.html', title='admin_page', users=users)


@app.route("/cancel_users<int:user_id>", methods=['GET', 'POST'])
@login_required
def cancel_users(user_id):
    user=User.query.filter_by(id=user_id).first()
    db.session.delete(user)
    db.session.commit()
    flash(f'{user.username}, has been successfully deleted','success')
    return redirect(url_for('admin'))

@app.route("/upload", methods=['GET', 'POST'])
@login_required
def upload():
    if request.method == "POST":
        if request.files:
            profile_picture=request.files['profile_picture']
            pic_address=os.path.join(app.root_path, 'static/img', profile_picture.filename)
            profile_picture.save(pic_address)    
            current_user.profile_img=profile_picture.filename 
            db.session.commit() 
            flash("Your profile picture is uploaded successfully", 'success')
            return redirect(request.url)
    return render_template('upload.html', title='upload_your_picture')


@app.route("/account")
@login_required
def user_account():
    return render_template('account.html', title='User_Account')

@app.route("/post_content",methods=['GET', 'POST'])
@login_required
def post_content():
    post_form=PostForm()
    if request.method == "POST":
        if post_form.validate_on_submit():
            post_title=post_form.title_of_post.data
            posted_body=post_form.body.data
            posted_content=Post(post_title=post_title, posted_content=posted_body, author=current_user)
            db.session.add(posted_content)
            db.session.commit()
            flash('Your post has been created successfully', 'success')
            return redirect(url_for('index'))
    return render_template('post.html', title='create_post', post_form=post_form)


@app.route("/signout")
@login_required
def signout():
    logout_user()
    return redirect(url_for('signin'))


@app.route("/viewPost/<int:id>", methods=['GET', 'POST'])
@login_required
def viewPost(id):
    viewed_post=Post.query.get_or_404(id)
    return render_template('viewPost.html', title="viewPost", viewed_post=viewed_post)

@app.route("/viewPost/<int:post_id>/updatePost", methods=['GET', 'POST'])
@login_required
def updatePost(post_id):
    
    update_post=Post.query.get_or_404(post_id)
    if request.method == "POST":
        post_title=request.form['title']
        post_contents=request.form['content']
        update_post.post_title=post_title
        update_post.posted_content=post_contents
        db.session.commit()
        flash("Your post is updated successfuly", 'success')
        return redirect(url_for('viewPost', id=update_post.id))
   
    return render_template('updatepost.html', title="UpdatePost", update_post=update_post)

@app.route("/viewPost/<int:post_id>/deletePost", methods=['GET','POST'])
@login_required
def deletePost(post_id):
    to_be_deleted_post=Post.query.get_or_404(post_id)
    db.session.delete(to_be_deleted_post)
    db.session.commit()
    flash("Your post has been deleted successfully", "success")
    return redirect(url_for('index'))

@app.route("/viewPost/<int:post_id>/confirm_deltion", methods=['GET','POST'])
@login_required
def confirm_deltion(post_id):
    if request.method == "POST":
        return redirect(url_for('deletePost', post_id=post_id))
    return render_template('confirm.html', post_id=post_id)


@app.route("/forgot_password", methods=['GET','POST'])

def forgot_password():
    forgot_form=ForgotPasswordForm()
    if forgot_form.validate_on_submit():
        pass
    return render_template('forgot_password.html', title="forgot_form", forgot_form=forgot_form)