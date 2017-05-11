from app import app
from app.development import db
from db_create import db_create

db.drop_all()
db_create(db)
app.run(host='127.0.0.1', port=8943,debug=True)
