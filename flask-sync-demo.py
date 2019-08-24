from flask import Flask, request, jsonify
#from models import get_question_analysis

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return 'hello world'

@app.route('/api', methods=['POST'])
def api():
    data = request.get_json()
    question = data['question']
    question_analysis = get_question_analysis(question)
    return jsonify(question_analysis)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)