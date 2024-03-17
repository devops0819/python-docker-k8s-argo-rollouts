from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def color_grid():
    colors = ['#'+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
              for i in range(100)]
    return render_template('grid.html', colors=colors)

@app.route('/hello')
def color_grid_api():
    colors = ['#'+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
              for i in range(100)]
    value = colors['srr']
    return render_template('grid.html', colors=colors)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
