from flask import Flask,request,jsonify
from threading import Thread
import spam



app = Flask("")

@app.route("/")
def main():
  return "<h1>BoxFreshSpamAPI</h1><br><h1>Developed by Kodai.</h1>"

@app.route('/v1/boxfresh', methods=['post'])
def situmon():
    id = request.form.get('id')
    content=request.form.get('content')
    if id==None or content==None:
      return jsonify(status="引数が足りません"),400
    status=spam.send(id,content)
    if status=="成功":
      return jsonify(status="success"),200
    else:
      return jsonify(status="error"),400
    
def run():
  app.run("0.0.0.0", port=8000)

t = Thread(target=run)
t.start()
