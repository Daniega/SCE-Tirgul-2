from app import app
from db_create import db_create
from app import db

db.drop_all()
db_create()
app.run(host='0.0.0.0', debug=True)
