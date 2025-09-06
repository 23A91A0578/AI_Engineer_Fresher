from sqlalchemy import Column, Integer, String, Text, DateTime, JSON
from app.database import Base
import datetime

class Email(Base):
    __tablename__ = "emails"

    id = Column(Integer, primary_key=True, index=True)
    sender = Column(String, nullable=False)
    subject = Column(String, nullable=False)
    body = Column(Text, nullable=False)
    received_at = Column(DateTime, default=datetime.datetime.utcnow)
    sentiment = Column(String, default="Neutral")
    priority = Column(String, default="Not Urgent")
    extracted_info = Column(JSON, default={})
    response_draft = Column(Text, default="")
    status = Column(String, default="Pending")
