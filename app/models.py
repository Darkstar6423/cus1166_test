
#from flask import url_for
from app import db




class Task(db.Model):

    task_id = db.Column(db.Integer, primary_key=True)
    task_title = db.Column(db.String(128))
    task_desc = db.Column(db.String(128), index=True)
    task_status = db.Column(db.String(128))
    task_date = db.Column(db.String(128))
    task_Cname = db.Column(db.String(128))
    task_address = db.Column(db.String(128))
    task_time = db.Column(db.String(128))
    task_duration = db.Column(db.String(128))