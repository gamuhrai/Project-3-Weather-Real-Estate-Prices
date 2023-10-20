from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
import plotly
import plotly.graph_objs as go
import json

app = Flask(__name__)
app.config['SQLALCHEMY_BINDS'] = {
    'homevalue': 'sqlite:///home_data.db',
    'temperature': 'sqlite:///temperature_data.db'
}
db = SQLAlchemy(app)

class HomeValue(db.Model):
    __bind_key__ = 'homevalue'
    __tablename__ = 'home_data'  # Added the correct table name here
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    value = db.Column(db.Float, nullable=False)

class Temperature(db.Model):
    __bind_key__ = 'temperature'
    __tablename__ = 'temperature_data'  # Added the correct table name here
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    temperature = db.Column(db.Float, nullable=False)

with app.app_context():
    engine_home = db.engines['homevalue']
    HomeValue.__table__.create(engine_home, checkfirst=True)  # Added checkfirst=True here for safety
    
    engine_temp = db.engines['temperature']
    Temperature.__table__.create(engine_temp, checkfirst=True)  # Added checkfirst=True here for safety

@app.route('/')
def index():
    return render_template('index_updated.html')

@app.route('/data/home_value/<city>')
def get_home_value(city):
    data = HomeValue.query.filter_by(city=city).all()
    years = [x.year for x in data]
    values = [x.value for x in data]
    graph = {
        'data': [{'x': years, 'y': values, 'type': 'line', 'name': city}],
        'layout': {'title': f'Home Value for 1 bedroom over the past 5 years in {city}'}
    }
    return json.dumps([graph], cls=plotly.utils.PlotlyJSONEncoder)

@app.route('/data/temperature/<city>')
def get_temperature(city):
    data = Temperature.query.filter_by(city=city).all()
    years = [x.year for x in data]
    temps = [x.temperature for x in data]
    graph = {
        'data': [{'x': years, 'y': temps, 'type': 'line', 'name': city}],
        'layout': {'title': f'Temperature over the past 5 years in {city}'}
    }
    return json.dumps([graph], cls=plotly.utils.PlotlyJSONEncoder)

if __name__ == '__main__':
    app.run(debug=True)
