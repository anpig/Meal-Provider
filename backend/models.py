from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Staff_Information(db.Model):
    __tablename__ = 'Staff_Information'

    StaffID = db.Column(db.Integer, primary_key=True)
    StaffName = db.Column(db.String(255))
    Position = db.Column(db.String(255))
    Gmail = db.Column(db.String(255))
    Password = db.Column(db.String(255))
    PhoneNumber = db.Column(db.Integer)

    def __repr__(self):
        return f"<Staff_Information {self.staff_id}>"