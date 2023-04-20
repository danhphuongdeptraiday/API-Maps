
from flask import Flask, render_template
app = Flask(__name__)

search_url ="https://maps.googleapis.com/maps/api/place/textsearch/output?parameters"
details_url= "https://maps.googleapis.com/maps/api/place/details/output?parameters"
@app.route("/")
def main():
    return render_template('index.html')
@app.route("/mapPage") 
def mapPage():
   return render_template('mapPage.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000)
