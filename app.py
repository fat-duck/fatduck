from flask import Flask
from reader import csv_reader  # reader package is the reader/ directory
from timetable import scheduler


app = Flask(__name__)


@app.route('/', methods=['GET'])
def json_output():
    return csv_reader.main()


if __name__ == '__main__':
    app.run(
        host='localhost',
        port='5000',
        debug=None,
        load_dotenv=True)
