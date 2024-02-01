from core.engine import Base
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Table, Boolean
from sqlalchemy.orm import relationship


class Gymnastic(Base):
    __tablename__ = "gymnastic"

    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    name = Column(String, nullable=False, index=True)
    description = Column(String)
    sets = relationship("Set", lazy="selectin", join_depth=2)
    is_collect_statistic = Column(Boolean, default=False, nullable=False)

    def __str__(self):
        return self.name


gymnastic_program_day = Table(
    "gymnastic_program_day", Base.metadata,
    Column("gymnastic_id", ForeignKey("gymnastic.id", ondelete="CASCADE"), primary_key=True, index=True),
    Column("program_day_id", ForeignKey("program_day.id", ondelete="CASCADE"), primary_key=True)
)


class Program(Base):
    __tablename__ = "program"

    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    name = Column(String, nullable=False, index=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    description = Column(String)


class ProgramDay(Base):
    __tablename__ = "program_day"

    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    name = Column(String, nullable=False, index=True)
    program_id = Column(Program, ForeignKey('program.id'))
    program = relationship("Program", lazy="selectin", join_depth=2)
    gymnastic_list = relationship(
        "Gymnastic",
        secondary=gymnastic_program_day,
        lazy="selectin",
        join_depth=2
    )

    def __str__(self):
        return self.name


class Training(Base):
    __tablename__ = "training"

    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    program_day_id = Column(ProgramDay, ForeignKey('program_day.id'))
    program_day = relationship("ProgramDay", lazy="selectin")

    def __str__(self):
        return f"Training {self.start_date}"


class Set(Base):
    __tablename__ = "set"

    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    start_date = Column(DateTime)
    comment = Column(String)
    training_id = Column(Training, ForeignKey('training.id'), nullable=False)
    training = relationship("Training", lazy="selectin")
    gymnastic_id = Column(Gymnastic, ForeignKey('gymnastic.id'), nullable=False)
    gymnastic = relationship("Gymnastic", lazy="selectin")
    repetition_count = Column(Integer, nullable=False)

    def __str__(self):
        return f"{self.start_date} - {self.gymnastic.name}"
