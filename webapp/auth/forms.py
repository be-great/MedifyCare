from flask_wtf import FlaskForm as Form
from flask_wtf import RecaptchaField
from wtforms import StringField, PasswordField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo, URL
from .models import User, Role


class LoginForm(Form):
    username = StringField('Username', [DataRequired(), Length(max=255)])
    password = PasswordField('Password', [DataRequired()])
    remember = BooleanField("Remember Me")

    def validate(self, extra_validators=None):
        check_validate = super(LoginForm, self).validate()

        # if our validators do not pass
        if not check_validate:
            return False

        # Does our user exist
        user = User.query.filter_by(username=self.username.data).first()
        if not user:
            self.username.errors.append('Invalid username or password')
            return False

        # Do the passwords match
        if not user.check_password(self.password.data):
            self.username.errors.append('Invalid password')
            return False

        return True


class RegisterForm(Form):
    username = StringField('Username', validators=[DataRequired(), Length(max=255)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    confirm = PasswordField('Confirm Password', validators=[
        DataRequired(),
        EqualTo('password', message="Passwords must match")
    ])
    role = SelectField('Role', choices=[], validators=[DataRequired()])
    speciality = StringField('Speciality')
    bio = StringField('Bio') 
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        # Fetch roles from the database and set choices
        self.role.choices = [(role.id, role.name.capitalize()) for role in Role.query.all()]

    def validate(self, extra_validators=None):
        # Perform standard validation
        if not super(RegisterForm, self).validate():
            return False
        print("---------------------------------------")
        print(self.speciality.data)
        print("---------------------------------------")
        if self.role.data == '1' and (self.speciality.data == "" or self.bio.data == ""):
            self.speciality.errors.append('Speciality and Bio is required for doctors')
            return False 
        # Custom validation: Check if the username already exists
        user = User.query.filter_by(username=self.username.data).first()
        if user:
            self.username.errors.append("User with that name already exists")
            return False

        return True
