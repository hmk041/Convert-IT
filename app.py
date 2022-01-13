from flask import Flask, render_template
import mainScript,YTdownloader


app = Flask(__name__)

@app.route('/')


def index():
    data = YTdownloader.video_title
    return render_template('index.html', filePath=data)


if __name__ == "__main__":
    app.run(debug=False)

    