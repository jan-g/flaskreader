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
        words = [('relevant time', 'Replace "relevant time" with "time of specification" - Level 4'),
                 ('good building practice', 'GOOD BUILDING PRACTICE REPLACEMENT'),
                 ('having been supplied or placed on the market in breach of the Construction Products Regulations', ''),
                 ('all the reasonable skill', ''),
                 ('Consultant\'s profession', ''),
                 ('successors', ''),
                 ('warrants', ''),
                 ('it has complied', ''),
                 ('time of specification or use', ''),
                 ('and ensure the completed Project complies with', ''),
                 ('to ensure', ''),
                 ('proceedings for breach of this clause', ''),
                 ('duties or liabilities under this agreement shall not be negated or diminished', ''),
                 ('professional indemnity insurance', ''),
                 ('ending 12 years after the date of making good of defects of the Project', ''),
                 ('on customary and usual terms and conditions prevailing for the time being in the insurance market', ''),
                 ('do not require the Consultant to discharge any liability before being entitled to recover from the, insurers', ''),
                 ('would not adversely affect the rights of any person to recover from the insurers under the Third Parties, (Rights Against Insurers) Act 2010', ''),
                 ('settle or compromise any claim with the insurers that relates to a claim by the Beneficiary against the, Consultant', ''),
                 ('by any act or omission lose or affect the Consultant\'s right to make, or proceed with, that claim, against the insurers', ''),
                 ('The Beneficiary may not commence any legal action against the Consultant under this agreement after 12, years from the date of making good of defects of all of the Project', ''),
                 ('The Beneficiary may assign the benefit', ''),
                 ('no greater liability', ''),
        ]
    return render_template('home.html', text=highlight_phrases(text, words), display=False, words=words)


def highlight_phrases(text, phrases):
    for phrase, replacement in phrases:
        text = replace_single_phrase(text, phrase)
    return text


def replace_single_phrase(text, phrase):
    return text.replace(phrase, "<b>" + phrase + "</b>")


if __name__ == '__main__':
    app.run(port=5000, debug=True)