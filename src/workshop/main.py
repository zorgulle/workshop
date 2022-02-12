from flask_api import FlaskAPI

app = FlaskAPI(__name__)

@app.route("/", methods=['GET'])
def index():
    return {'mame': "toto"}

def main():
    app.run('0.0.0.0', debug=True)

if __name__ == "__main__":
    main()
