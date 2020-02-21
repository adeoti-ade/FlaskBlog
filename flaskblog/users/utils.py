import os
import secrets
from flask import url_for
from PIL import Image
from flask_mail import Message
from flaskblog import mail



def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message(subject='Password Reset Confirmation', 
                                recipients=[user.email], 
                                sender='noreply@demo.com')
    msg.body = f""" To reset your password, kindly use the link 
    {url_for('reset_token', token = token, _external=True)}

    if you did not request for the reset, kindly ignore this message
    """
    mail.send(msg)
