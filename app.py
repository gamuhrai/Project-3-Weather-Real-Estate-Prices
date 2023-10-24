from flask import Flask, render_template, jsonify, send_file
import sqlite3
from flask_sqlalchemy import SQLAlchemy
import plotly
import plotly.graph_objs as go
import json
from datetime import datetime




app = Flask(__name__)
app.config['SQLALCHEMY_BINDS'] = {
    'homevalue': 'sqlite:///home.db',
    'temperature': 'sqlite:///temp.db'
}
db = SQLAlchemy(app)

class HomeValue(db.Model):
    __bind_key__ = 'homevalue'
    __tablename__ = 'home'  # Added the correct table name here
    id = db.Column(db.Integer, primary_key=True)
    City = db.Column(db.String, nullable=False)
    Date = db.Column(db.String, nullable=False) 
    HomeValue = db.Column(db.Float, nullable=False)

class Temperature(db.Model):
    __bind_key__ = 'temperature'
    __tablename__ = 'temp'  # Added the correct table name here
    id = db.Column(db.Integer, primary_key=True)
    City = db.Column(db.String, nullable=False)
    Date = db.Column(db.Integer, nullable=False)
    Temperature = db.Column(db.Float, nullable=False)

with app.app_context():
    engine_home = db.engines['homevalue']
    HomeValue.__table__.create(engine_home, checkfirst=True)  # Added checkfirst=True here for safety
    
    engine_temp = db.engines['temperature']
    Temperature.__table__.create(engine_temp, checkfirst=True)  # Added checkfirst=True here for safety

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data/home/', methods=['GET'])
def get_data_home():
    conn = sqlite3.connect('home.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM home")
    rows = cursor.fetchall()
    conn.close()
    return jsonify({'data': rows})


@app.route('/api/data/temp/', methods=['GET'])
def get_data_temp():
    conn = sqlite3.connect('temp.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM temp")
    rows = cursor.fetchall()
    conn.close()
    return jsonify({'data': rows})



@app.route('/api/data/home/<string:city>', methods=['GET'])
def get_data_home_city(city):
    conn = sqlite3.connect('home.db')
    cursor = conn.cursor()
    query = "SELECT Date, HomeValue FROM home WHERE LOWER(TRIM(City)) = LOWER(TRIM(?))"
    cursor.execute(query, (city,))
    rows = cursor.fetchall()
    conn.close()
    dates = [row[0] for row in rows]
    home_values = [row[1] for row in rows]
    return jsonify({'dates': dates, 'home_values': home_values})


@app.route('/api/data/temp/<string:city>', methods=['GET'])
def get_data_temp_city(city):
    conn = sqlite3.connect('temp.db')
    cursor = conn.cursor()
    query = "SELECT Date, Temperature FROM temp WHERE LOWER(TRIM(City)) = LOWER(TRIM(?))"
    cursor.execute(query, (city,))
    rows = cursor.fetchall()
    conn.close()
    dates = [row[0] for row in rows]
    temperatures = [row[1] for row in rows]
    return jsonify({'dates': dates, 'temperatures': temperatures})

if __name__ == '__main__':
    app.run(debug=True)

