from flask import Flask, redirect, url_for, request,jsonify,render_template,send_from_directory
from main_8 import start
from flask_cors import CORS

app = Flask(__name__,template_folder='output')
CORS(app)
@app.route("/output/<path:filepath>")
def hello(filepath):
   return send_from_directory('output',filepath)
@app.route("/output/<path:filepath>")
def data(filepath):
       return send_from_directory('output',filepath)
@app.route('/output/<path:filepath>')
def data2(filepath):
      return send_from_directory('output',filepath)
@app.route('/output/<path:filepath>')
def data3():
       return send_from_directory('output',filepath)
@app.route('/foo', methods=['POST']) 
def foo():
    k = request.json
    print(k)
    # print(k.get("Filter_1"))
    filter_1 = str(k.get("wp_id"))
    filter_2 = k.get("Filter_2")
    filter_3  = k.get("Filter_3")
    try:
      filter_4 = k.get("Filter_4")
    except:
      filter_4 = 5
    if filter_2 == "":
      filter_2 = "All"
    if filter_3 == "":
      filter_3 = "All"
    org_id =  k.get("org_id")
    return start(filter_1,filter_2,filter_3,org_id,filter_4)

    
@app.route("/")
def run_model():
    k = hello()
    return k

if __name__ == "__main__":
    print("sandeep")
    
    app.run(host="0.0.0.0",port="82")

