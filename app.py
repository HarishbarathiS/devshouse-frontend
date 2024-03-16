from flask import Flask, render_template

app = Flask(__name__)

# Example JSON data
visualize_data = {
    "Table1": [
        ["Name", "age", "ID","phone no."],
        ["harish", 19, "001","982834324"],
        ["nidish", 20, "002","234324232"],
        ["harish", 19, "001","982834324"],
        ["nidish", 20, "002","234324232"],
        ["harish", 19, "001","982834324"],
        ["harish", 19, "001","982834324"],
    ],
    "Table2": [
        ["Name", "age", "ID","phone no."],
        ["harish", 19, "001","982834324"],
        ["nidish", 20, "002","234324232"],
        ["harish", 19, "001","982834324"],
        ["nidish", 20, "002","234324232"],
        ["harish", 19, "001","982834324"],
    ],
    "Table3": [
        ["Name", "age", "ID","phone no."],
        ["harish", 19, "001","982834324"],
        ["nidish", 20, "002","234324232"],
        ["harish", 19, "001","982834324"],
        ["nidish", 20, "002","234324232"],
        ["harish", 19, "001","982834324"],
    ],
    "Table4": [
        ["Name", "age", "ID","phone no."],
        ["harish", 19, "001","982834324"],
        ["nidish", 20, "002","234324232"],
        ["harish", 19, "001","982834324"],
        ["nidish", 20, "002","234324232"],
        ["harish", 19, "001","982834324"]
    ],
    "Table5": [
        ["Name", "age", "ID","phone no."],
        ["harish", 19, "001","982834324"],
        ["nidish", 20, "002","234324232"],
        ["harish", 19, "001","982834324"],
        ["nidish", 20, "002","234324232"],
        ["harish", 19, "001","982834324"]
    ]
}

diff_data = {
    "Table2": [
        ["Name", "age", "ID","phone no."],
        ["harish", 19, "001","982834324"],
        ["nidish", 20, "002","234324232"],
        ["harish", 19, "001","982834324"],
        ["nidish", 20, "002","234324232"],
        ["harish", 19, "001","982834324"],
    ],
    "Table3": [
        ["Name", "age", "ID","phone no."],
        ["harish", 19, "001","982834324"],
        ["nidish", 20, "002","234324232"],
        ["harish", 19, "001","982834324"],
        ["nidish", 20, "002","234324232"],
        ["harish", 19, "001","982834324"],
    ],
}




@app.route('/visualize')
def visualize():
    # Render the HTML template and pass JSON data to it
    return render_template('visualize.html', data=visualize_data)

@app.route('/diff')
def diff():
    # Render the HTML template and pass JSON data to it
    return render_template('diff.html', data=diff_data)


if __name__ == '__main__':
    app.run(debug=True)
