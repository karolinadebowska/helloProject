import requests
import json
import os

from flask import Flask, render_template, request

app = Flask(__name__)

from dotenv import load_dotenv
load_dotenv()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/hello', methods=["POST"])
def hello():
    #create an array of languages
    language=["Azerbaijan","Vietnamese","Albanian","Maltese","Amharic","Macedonian","Arabic","Marathi","Armenian",
    "Mongolian","German","Polish","Spanish","Chinese","French","Scottish","Korean","Esperanto","Sundanese","Persian"]
    #create an array of languages' code
    code = ["az", "vi", "sq","mt","am","mk","ar","mr","hy","mn","de","pl","es","zh","fr","gd","ko","eo","su","fa"]
    #create an array of colours
    background=["#9932CC","black","#00CED1","#9932CC","#B22222","#696969","#4B0082","#20B2AA","#800000","#800080",
                "#C71585","#FF4500","#DA70D6","#BC8F8F","#4682B4","#9ACD32","#4682B4","#708090","#DB7093","#6B8E23"]
    #create an array of fonts
    font=["#48D1CC","#FFC0CB","#FFDEAD","#FAF0E6","#FFA07A","#FFB6C1","#FAFAD2","#FFFACD","#FFF0F5","#F0E68C",
            "#F0FFF0","#ADFF2F","#FFD700","#FF00FF","#00CED1","#E9967A","#BDB76B","#00FFFF","#7FFF00","#7FFFD4"]
    data = request.values
    return render_template("hello.html",language=language,code=code,font=font,background=background,x=0, hello_data=data,hello="Good morning")

def get_html(url):
    return requests.get(url).text

def get_translation(text,lang):
    URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    KEY = os.getenv('API_KEY')
    TEXT = text
    LANG = lang;
    r=requests.post(URL, data={'key' : KEY,'text' : TEXT,'lang' : LANG} )
    return r.text
#text to translate
text="Good morning"
@app.route("/translate")
def translate():
    lang = request.values.get("code")
    translation = get_translation(text, lang)
    index = translation.find("text")
    #translated word
    translation= translation[index+8:-3]
    print(translation)
    return translation

app.run(debug=True)
