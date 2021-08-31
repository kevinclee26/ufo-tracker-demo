from flask import Flask, jsonify, render_template
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import Session
import os

app=Flask(__name__)

# connection_url='sqlite:///ufo.sqlite'
connection_url=os.environ.get('DATABASE_URL').replace('postgres', 'postgresql')
engine=create_engine(connection_url)

##### Setting up DB #####
Base=declarative_base()
class ufo(Base):
    __tablename__='ufo'
    id=Column(Integer, primary_key=True)
    shape=Column(String(255))
    lat=Column(Float)
    lon=Column(Float)
    description=Column(String(255))

Base.metadata.create_all(engine)
#########################

@app.route('/')
def home(): 
	return render_template('index.html')

@app.route('/fetch')
def fetch_records():
	# records=engine.execute('select * from ufo').fetchall()
	# return_data=[]
	# for each_record in records: 
	# 	one_row=[]
	# 	for each_column in each_record[1:]: 
	# 		one_row.append(each_column)
	# 	return_data.append(one_row)
	session=Session(engine)
	records=session.query(ufo.shape, ufo.lat, ufo.lon, ufo.description).all()
	# print(records)
	records_dict=[{'shape': each_record[0], 
				   'lat': each_record[1], 
				   'lon': each_record[2], 
				   'description': each_record[3]} for each_record in records]
	session.close()
	# return jsonify(return_data)
	return jsonify(records_dict)

if __name__=='__main__': 
	app.run()