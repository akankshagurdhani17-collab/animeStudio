from flask import Flask,render_template,request
from google import genai

from dotenv import load_dotenv
from urllib3.util import url
import os

load_dotenv()

key=os.getenv('gemini_api_key')
app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':

        n1=request.form['inp1']
        n2=request.form['inp2']
        n3=request.form['inp3']
        n4=request.form['inp4']
        n5=request.form['inp5']
        n6=request.form['inp6']
        n7=request.form['inp7']

        client = genai.Client(api_key=key)

        response = client.models.generate_content(
            model="gemini-3.5-flash", contents=f"Hi I am {n7},I want to create a anime story in the comics form"
                                               f"with proper dialogues written in oval callout and"
                                               f"pictures of every charaters with the expression"
                                               f"according to the dialogue and dialogues must"
                                               f"be visible properly and read dialogue in good voice give option on webpage"
                                               f"which voice you want to"
                                               f"prefer male or female or no voice and anyone can change it anytime from any episode and"
                                               f"whenever someone hover over the dialogue or oval callout part the voice must read dialogue and add all type of "
                                               f"voice of noise or any type of quarrel as well,the genre of the comics"
                                               f"will be {n1} and the main character will"
                                               f"be {n2} with suppoting character{n3} and want other"
                                               f"characters as well of your choice to make story "
                                               f"more intresting the story theme will be {n4} the main"
                                               f"character will have the special power {n5}"
                                               f"the tone of the story will be {n6}"
                                               f"total number of episodes will be {n7}"
                                               f"create good and modern story episodes in html "
                                               f"format with character's pictures and"
                                               f"good graphics just like we watch on tv of every character in "
                                               f"all episodes and give good background in every image according {n4} theme mentioned in story so that user can relate"
                                               f"it"
                                               f"Do not add extra information on the page just provide pure html content"
                                               f"as a result"
        )

        return render_template('result.html',result=response.text)

#app.run(debug=True)