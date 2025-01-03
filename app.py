from flask import Flask, request, jsonify, render_template
from capture import capture_webpage_as_base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# API Route to capture webpage and return Base64 image
@app.route('/capture-webpage', methods=['POST'])
def capture_webpage():
    try:
        data = request.get_json(silent=True)
        if not data or 'url' not in data:
            return jsonify({"error": "Invalid JSON or missing 'url' parameter"}), 400
        
        url = data['url']
        base64_image = capture_webpage_as_base64(url)
        
        if isinstance(base64_image, dict):  # Error handling
            return jsonify(base64_image), 500

        return jsonify({"base64_image": base64_image}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
