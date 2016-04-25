from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc, func
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, App, User
from flask import session as login_session
import random
import string

# Connect to Database and create database session

engine = create_engine('sqlite:///vrappswithusers.db')
Base.metadata.bind = engine


DBSession = sessionmaker(bind=engine)
session = DBSession()


def showUsers():
	userRecord = session.query(User).all()
	for user in userRecord:
		print user.name
		print user.id
		print user.email
		print user.picture
		print "<br>"

def removeUser(id):
	user = session.query(User).filter_by(id = id).one()
	print "delete user name: " + user.name + "id#" + str(user.id)
	session.delete(user)
	session.commit()

def removeApp(id):
	app = session.query(App).filter_by(id = id).one()
	print "delete app name: " + str(app.id)
	session.delete(app)
	session.commit()

def showApp(appname):
	app = session.query(App).filter_by(name = appname).one()
	print app.name
	print app.category_id
	print app.user_id

def addCategory(name):
	newCategory = Category(name = name)


def showApp(appname):
	apps = session.query(App).filter_by(name = appname).all()
	for app in apps:
		print app.name
		print app.id

removeApp(10)





