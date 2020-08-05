import sqlalchemy
from .db_session import SqlAlchemyBase


class Hardware(SqlAlchemyBase):
    __tablename__ = 'hardware'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, nullable=False)
    name = sqlalchemy.Column(sqlalchemy.String)
    spec = sqlalchemy.Column(sqlalchemy.String)
    price = sqlalchemy.Column(sqlalchemy.String)
    picture = sqlalchemy.Column(sqlalchemy.String)
    hardware_type = sqlalchemy.Column(sqlalchemy.String)
    url = sqlalchemy.Column(sqlalchemy.String)