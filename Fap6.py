from sqlalchemy import create_engine,Column , String , Integer , ForeignKey
from sqlalchemy.orm import declarative_base , sessionmaker , relationship


"""This code is about SQLAlchemy which is a powerful Object-Relational Mapping (ORM) library for Python. It allows developers to interact with databases using Python objects and classes, rather than writing raw SQL queries."""
"""mportant for dealing with database and backend"""
engine=create_engine("sqlite:///autism.db")
Base=declarative_base()

class Patient(Base):
    __tablename__="patients"

    id=Column(Integer , primary_key=True)
    name=Column(String)
    report=relationship("Report")
    


class Doctor(Base):
    __tablename__="doctors"
    d_id=Column(Integer , primary_key=True)
    d_name=Column(String)
    report=relationship("Report")


class Report(Base):
    __tablename__="reports"
    r_id=Column(Integer , primary_key=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    doctor_id = Column(Integer, ForeignKey("doctors.d_id"))
    result = Column(String)
    patient = relationship("Patient")
    doctor = relationship("Doctor")

    
Base.metadata.create_all(engine)

Session=sessionmaker(bind=engine)
s=Session()


p1 = Patient(id=46,name="Purav")
p2 = Patient(id=34,name="Ranjit")

s.add(p1)
s.add(p2)
s.commit()

d1 = Doctor(d_id=90,d_name="Dr Sharma")
d2 = Doctor(d_id=91,d_name="Dr Verma")

s.add(d1)
s.add(d2)
s.commit()


r1 = Report(
    patient=p1,
    doctor=d1,
    result="Autism"
)

r2 = Report(
    patient=p2,
    doctor=d2,
    result="Normal"
)

s.add(r1)
s.add(r2)

s.commit()



reports = s.query(Report).all()

for r in reports:

    print("Report ID:", r.r_id)
    print("Patient:", r.patient.name)
    print("Doctor:", r.doctor.d_name)
    print("Result:", r.result)
    print()