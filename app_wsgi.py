import pandas as pd
import numpy as np
import sklearn
from flask import Flask, render_template, request

app = Flask(__name__, static_folder='static')


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/results', methods=['Get', 'Post'])
def lo():
    loc = request.form['location']
    rt = request.form['type']
    print(rt)
    price = request.form['price']
    data = pd.read_csv("AB_NYC_2019.csv")
    pd.set_option('display.max_rows', 5)
    pd.set_option('display.max_columns', 5)

    data.drop(['id', 'host_id', 'host_name', 'last_review',
               'reviews_per_month'], 1, inplace=True)
    data['name'].fillna('Name not provided', inplace=True)

    spec_data = data.loc[data['neighbourhood_group'] == loc]
    spec_data = spec_data[spec_data.price != 0]

    spec_data = spec_data.loc[spec_data['room_type'] == rt]

    spec_data = spec_data[spec_data.price >= int(price)]
    final_data = spec_data.sort_values(by=['price'])
    d = [name for name in final_data['name']]
    return render_template('results.html', location=loc, data=d, len=5)


if __name__ == "__main__":
    app.run(debug=True)
