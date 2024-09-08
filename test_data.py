import logging
import random
from webapp import create_app
from webapp import db
from webapp.auth.models import User, Role
from webapp.auth import bcrypt
from config import DevConfig


logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
logging.getLogger().setLevel(logging.DEBUG)

log = logging.getLogger(__name__)
app = create_app(DevConfig)
app.app_context().push()



fake_users = [
    {'username': 'Esra', 'role': 'patient'},
    {'username': 'Dr.James Smith', 'role': 'doctor', 'specialty': 'cardiology', 'bio': 'Dr. James Smith is a board-certified cardiologist with over 15 years of experience in diagnosing and treating heart conditions. He specializes in interventional cardiology and is passionate about improving patient outcomes through advanced cardiac procedures.'},
    {'username': 'Dr.Susan Martin', 'role': 'doctor', 'specialty': 'neurology', 'bio': 'Dr. Susan Martin is a neurologist with a focus on neurodegenerative diseases and stroke management. With a keen interest in research and patient care, she works to advance treatment options for neurological disorders and enhance patients\' quality of life.'},
    {'username': 'Dr.Michael Johnson', 'role': 'doctor', 'specialty': 'orthopedics', 'bio': 'Dr. Michael Johnson is an orthopedic surgeon specializing in sports injuries and joint replacement. He is dedicated to helping patients recover from musculoskeletal injuries and improve their mobility through both surgical and non-surgical methods.'},
    {'username': 'Dr.Emily Clark', 'role': 'doctor', 'specialty': 'pediatrics', 'bio': 'Dr. Emily Clark is a pediatrician with expertise in child development and preventive care. She is committed to providing compassionate care to children and their families, focusing on early diagnosis and management of common pediatric conditions.'}
]
fake_roles = ['doctor', 'patient']


def generate_roles():
    roles = list()
    for rolename in fake_roles:
        role = Role.query.filter_by(name=rolename).first()
        if role:
            roles.append(role)
            continue
        role = Role(rolename)
        roles.append(role)
        db.session.add(role)
        try:
            db.session.commit()
        except Exception as e:
            log.error("Erro inserting role: %s, %s" % (str(role),e))
            db.session.rollback()
    return roles

def generate_users():
    users = list()
    for item in fake_users:
        user = User.query.filter_by(username=item['username']).first()
        if user:
            users.append(user)
            continue
        user = User()
        poster = Role.query.filter_by(name=item['role']).one()
        user.roles.append(poster)
        user.username = item['username']
        if item['role'] == 'doctor':
            user.specialty = item['specialty']
            user.bio = item['bio']
        user.password = bcrypt.generate_password_hash("password")
        users.append(user)
        try:
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            log.error("Eror inserting user: %s, %s" % (str(user), e))
            db.session.rollback()
    return users



generate_roles()
generate_users()
