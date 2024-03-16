from flask import Flask, render_template

app = Flask(__name__)

# Example JSON data
json_data = {
    "table1": [
        ["Name", "age", "ID","phone no."],
        ["harish", 19, "001","982834324"],
        ["nidish", 20, "002","234324232"]
    ],
    "table2": [
        ["Name", "age", "ID","phone no."],
        ["harish", 19, "001","982834324"],
        ["nidish", 20, "002","234324232"],
        ["Name", "age", "ID","phone no."],
        ["harish", 19, "001","982834324"],
        ["nidish", 20, "002","234324232"],
    ]
}


h_data = json_data["table1"][0]
val_data = json_data["table1"][1:]


@app.route('/')
def index():
    # Render the HTML template and pass JSON data to it
    return render_template('test1.html', header=h_data,values=val_data)

if __name__ == '__main__':
    app.run(debug=True)
