from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify, send_file
import requests
import json
import os
from datetime import datetime
import random
import subprocess


application = Flask(__name__)


#@app.route('/')
#def index():
#   return render_template('')
#    return '<html><body><form action="/turnon" method="get" target="_blank"><label for="status">status:</label><input type="text" id="status" name="status"><br><br><button type="submit">Submit</button></form></body></html>'
#    f = open("/etc/nginx/nginx.conf", "r")
#    output = f.read()
#    return render_template('first.html', nginxconf=output)

@application.route('/',methods = ['POST', 'GET'])
def turnon():

   myheaders = request.headers
   file = "/etc/nginx/conf.d/default.conf"
   if request.method == 'POST':

      config = request.form.get('config')
      f1 = open(file, "w")
      f1.write(config)
      f1.close()

      f = open(file, "r")
      output = f.read()

      return render_template('first.html', nginxconf=output, headers=myheaders)
   else:
      status = request.args.get('status')
      f = open(file, "r")
      output = f.read()

      if str(status) == 'check':
         p = subprocess.Popen("nginx -t | grep nginx", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
         p.wait()
         output1, errors1 = p.communicate()
         return render_template('first.html', nginxconf=output, log=errors1, headers=myheaders)
      if str(status) == 'reload':
         p = subprocess.Popen("nginx -s reload", shell=True, stdout=subprocess.PIPE)
         p.wait()
         output2, errors = p.communicate()
         #print(output2)
         return render_template('first.html', nginxconf=output, log="Service Reloaded", headers=myheaders)

   return render_template('first.html', nginxconf=output, headers=myheaders)

if __name__ == "__main__":
    application.run(host='0.0.0.0', debug=True, port=3001)
