from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Read CSV file into a DataFrame
df = pd.read_csv("static/Database2.csv")

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/result', methods=['POST'])
def result():
    # Get user inputs from the form
    rank_filter = request.form.get('All India Merit')
    percentile_filter = request.form.get('Percentile Score')
    Location_filter = request.form.get('Location')
    CourseName_filter = request.form.get('Course Name')

    # Create a copy of the original DataFrame for filtering
    filtered_df = df.copy()

    # Apply filters based on user inputs
    if rank_filter:
        filtered_df = filtered_df[filtered_df['All India Merit'] <= int(rank_filter)]
    if percentile_filter:
        filtered_df = filtered_df[filtered_df['Percentile Score'] <= float(percentile_filter)]
    if Location_filter:  # Corrected from percentile_filter to Location_filter
        filtered_df = filtered_df[filtered_df['Location'] == Location_filter]
    if CourseName_filter:  # Corrected from percentile_filter to CourseName_filter
        filtered_df = filtered_df[filtered_df['Course Name'] == CourseName_filter]
    # Extract the specified columns as a list of dictionaries
    data_list = filtered_df.to_dict(orient='records')

    # Render the template with the filtered data
    return render_template('result1.html', data_list=data_list)

if __name__ == '__main__':
    app.run(debug=True, port = 2100)
