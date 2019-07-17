import os
from flask import Flask, render_template, request,jsonify, request, url_for, redirect, session
import docx2txt

app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route("/")
def index():
    return render_template("upload.html")


@app.route("/upload", methods=['POST'])
def upload():

    target = os.path.join(APP_ROOT, 'images/')

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        filename = file.filename
        destination = "/".join([target, filename])
        file.save(destination)
    
    if request.method == 'POST':
        text = docx2txt.process(file)
        word1 = 'relevant time'
        word2 = 'good building practice'
        word3 = 'having been supplied or placed on the market in breach of the Construction Products Regulations'
        word4 = 'all the reasonable skill'
        word5 = 'Consultant\'s profession'
        word6 = 'successors' 
        word7 = 'warrants' 
        word8 = 'it has complied'
        word9 = 'time of specification or use'
        word10 = 'and ensure the completed Project complies with'
        word11 = 'to ensure'
        word12 = 'proceedings for breach of this clause'
        word13 = 'duties or liabilities under this agreement shall not be negated or diminished'
        word14 = 'professional indemnity insurance'
        word15 = 'ending 12 years after the date of making good of defects of the Project'
        word16 = 'on customary and usual terms and conditions prevailing for the time being in the insurance market'
        word17 = 'do not require the Consultant to discharge any liability before being entitled to recover from the insurers'
        word18 = 'would not adversely affect the rights of any person to recover from the insurers under the Third Parties (Rights Against Insurers) Act 2010'
        word19 = 'settle or compromise any claim with the insurers that relates to a claim by the Beneficiary against the Consultant'
        word20 = 'by any act or omission lose or affect the Consultant\'s right to make, or proceed with, that claim against the insurers'
        word21 = 'The Beneficiary may not commence any legal action against the Consultant under this agreement after 12 years from the date of making good of defects of all of the Project'    
        word22 = 'The Beneficiary may assign the benefit' 
        word23 = 'no greater liability'   
    return render_template('home.html', text=text, display=False, word1=word1,
    word2=word2, word3=word3, word4=word4,word5=word5, word6=word6, 
    word7=word7, word8=word8, word9=word9, word10=word10, word11=word11, 
    word12=word12, word13=word13, word14=word14, word15=word15, word16=word16,
    word17=word17, word18=word18, word19=word19, word20=word20, word21=word21, word22=word22,
    word23=word23)

if __name__ == '__main__':
    app.run(port=5000, debug=True)