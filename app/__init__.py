"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaakdjhp8u791guqvog-a.oregon-postgres.render.com",
        database="todol",
        user="todol_user",
        password="7XlVW7y9yTgelUaAmzYx2DzyE7ciUkQL")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import heregit 
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
