from app import db


class Card(db.Model):
    card_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    message = db.Column(db.String)
    likes_count = db.Column(db.Integer)
    board_id = db.Column(db.Integer, db.ForeignKey("board.board_id"))


    def to_dict(self):
        card_dict = {
                "id": self.card_id,
                "message": self.message,
                "likes_count": self.likes_count
                }
                
        if self.board_id:
            card_dict["board_id"] = self.board_id

        return card_dict
