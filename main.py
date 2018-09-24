from flask import Flask, render_template, request
from caesar import rotate_string
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def about():
    rot_amount = int(request.form['rotation-amount'])
    new_text = request.form['block_text']
    #run caesar algo
    b_text= rotate_string(new_text, rot_amount)#the return from caesar
     
    return render_template('index.html', new_text_box = b_text)
    

app.run(debug = True)    