import sqlalchemy
from .db_session import SqlAlchemyBase


class Configurator(SqlAlchemyBase):
    __tablename__ = 'configurator'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, nullable=False)
    name = sqlalchemy.Column(sqlalchemy.String)
    motherboard = sqlalchemy.Column(sqlalchemy.String)
    cpu = sqlalchemy.Column(sqlalchemy.String)
    ram = sqlalchemy.Column(sqlalchemy.String)
    gpu = sqlalchemy.Column(sqlalchemy.String)
    drive = sqlalchemy.Column(sqlalchemy.String)
    ps = sqlalchemy.Column(sqlalchemy.String)
    case = sqlalchemy.Column(sqlalchemy.String)
