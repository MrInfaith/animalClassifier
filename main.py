from flask import * 
from prediction import classifier
import os
app=Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method=='POST':
        image = request.files['image']
        file=os.listdir('static/uploads')
        if image not in file:
            image.save('static/uploads/' + image.filename)
        image_url = f'static/uploads/{image.filename}'
        predict=classifier(image_url)
        return render_template('predict.html',predict=predict,image=image_url)
    else:
        return redirect('index.html')
if __name__=='__main__':
    app.run(debug=True)
