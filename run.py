from app import app
from app.development import db
from db_create import db_create

db.drop_all()
db_create(db)
app.run(host='0.0.0.0',debug=True)
