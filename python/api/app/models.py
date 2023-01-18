
from app import db
class Stock(db.Model):
    __tablename__ = 'stocks'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100), nullable=False)
    available = db.Column(db.Boolean)
    position = db.Column(db.String(100), nullable=False)

    def __init__(self, content, position):
        self.content = content
        self.available = True
        self.position = position
        super().__init__()

    def to_json(self):
        return {
            'id': self.id,
            'content': self.content,
            'available': self.available,
            'position': self.position
        }

    def __repr__(self):
        return f"<Stock {self.id} -> {self.content} @ Pos: {str(self.position)}>"
