from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . import sql
import os

# Create your views here.

def index(request):
    return render(request, 'index.html')

def recordings(request):
    rec_arr = ['output/'+rec for rec in os.listdir('./frontend/static/output') if rec.endswith('.mp4')] 
    print(rec_arr)
    return render(request, 'recordings.html', {'rec_arr': rec_arr})

def events(request):
    conn = sql.create_connection()
    cur = conn.cursor()
    rows = cur.execute("SELECT * FROM events").fetchall()
    print(rows)
    
    return render(request, 'events.html', {'rows': rows})

def view_video(request, video):
    video_path = video
    return render(request, 'view_video.html', {'video_path': 'output/'+video_path})
    


def logout(request):
    return render(request, 'index.html')