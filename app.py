from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/test', methods=['GET','POST'])
def test():
    if request.method == 'GET':
        return jsonify({'response':'Get Request Called'})
    
    elif request.method == 'POST':
        req_Json = request.json
        no = req_Json['no']
        if no%2==0:
            return jsonify({"response":"NO is EVEN"})
        else:
            return jsonify({"response":"NO is ODD"})


if __name__ == '__main__':
    app.run(debug=True)