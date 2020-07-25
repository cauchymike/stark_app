from flask import Flask, url_for, render_template, redirect
from forms import JobForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'seunmelody'

##################################################################################
#view section
#################################################################################

@app.route('/', methods = ('GET', 'POST'))
def jobformm():
    form = JobForm()
    if form.validate_on_submit():
        return redirect(url_for('success'))
    return  render_template('index.html', form = form)

@app.route('/success')
def success():
    return 'Application Received, We will contact you soon'

if __name__ == '__main__':
    app.run(debug=False)



