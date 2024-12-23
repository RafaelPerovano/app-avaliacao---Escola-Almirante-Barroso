from flask import Flask, request, render_template, redirect, jsonify, session, url_for
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
import psycopg2
from db import cursor, conn

cursor.execute("SELECT * from avaliacoes")

mostra = cursor.fetchall()
print(mostra)