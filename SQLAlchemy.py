from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///base.db", echo=True)
Session = sessionmaker(engine)
Base = declarative_base()


class Input_text(Base):
    __tablename__ = "input_text"
    id = Column(Integer, primary_key=True)
    input_text = Column(String(50), index=True)

    def __init__(self,input_text):
        self.input_text = input_text

    def __str__(self):
        return f'{self.id}) {self.input_text}'

class Key_skills(Base):
    __tablename__ = "key_skills"
    id = Column(Integer, primary_key=True)
    key_skills = Column(String(200), unique=True)

    def __init__(self,key_skills):
        self.key_skills = key_skills

    def __str__(self):
        return f'{self.id}) {self.key_skills}'

class Input_text_Key_skills(Base):
    __tablename__ = "input_text_key_skills"
    id = Column(Integer, primary_key=True)
    id_input_text = Column(Integer, ForeignKey("input_text.id"))
    id_key_skills = Column(Integer, ForeignKey("key_skills.id"))
    count = Column(Integer, default=0)
    percent = Column(Float, default=0)

    def __init__(self,id_input_text,id_key_skills,count,percent):
        self.id_input_text = id_input_text
        self.id_key_skills = id_key_skills
        self.count = count
        self.percent = percent

    def __str__(self):
        return f'{self.id}) {self.id_input_text} | {self.id_key_skills} | {self.count} | {self.percent} |'

Base.metadata.create_all(engine)
