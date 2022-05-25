from flask import Flask, render_template

#initalizing flask 
app = Flask(__name__)


#home page
@app.route("/")
def home():
    print("Client request was recieved")
    return(
        render_template("index.html")
    )


if __name__ == "__main__":
    app.run(debug=True)
