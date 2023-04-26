from flask import Flask,render_template,request
import openai

app = Flask(__name__)
openai.api_key ='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'
conversacion = []

@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    
    if request.form['question']:
        question = 'Yo: ' + request.form['question']
        
        response = openai.Completion.create( 
            engine = 'text-davinci-003',
            prompt = question,
            temperature = 0.9,
            max_tokens = 150,
            top_p=1,
            frequency_penalty = 0,
            presence_penalty = 0.6 
        
           
        )
        answer = 'Asistente:' + response.choices[0].text.strip()
        conversacion.append(question)
        conversacion.append(answer)
        
        return render_template('index.html',chat = conversacion)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True,port=4000)