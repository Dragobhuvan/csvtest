from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/compare', methods=['POST'])
def compare_csv_files():
    # Retrieve the file paths from the request form
    file1 = request.form['file1']
    file2 = request.form['file2']

    # Read the CSV files into Pandas DataFrames
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    # Compare the two sheets
    diff = pd.concat([df1, df2]).drop_duplicates(keep=False)

    # Prepare the differences as a string
    if not diff.empty:
        differences = diff.to_string(index=False)
    else:
        differences = "No differences found between the two sheets."

    # Render the template with the differences
    return render_template('results.html', differences=differences)

if __name__ == '__main__':
    app.run(debug=True)
