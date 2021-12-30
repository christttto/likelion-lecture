from flask import Flask
from flask import render_template
from flask import request
import os
import openai
openai.api_key = "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"
app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])

def hello_world():

    if request.method == 'POST':
        user_msg = request.form['msg']
        response = openai.Completion.create(
            engine="davinci",
            prompt=request.form['msg'],
            temperature=0.7,
            max_tokens=60,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        user_msg = response["choices"][0]["text"]
    else:
        user_msg = "Create an outline for an essay about Walt Disney and his contributions to animation:\n\nI: Introduction"
    return render_template('hello.html', output_msg = user_msg)
