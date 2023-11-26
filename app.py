"""
python -m venv env
pip install flask
python.exe -m pip install --upgrade pip
pip install flask_wtf
pip install pandas
pip install scikit-learn
pip install gunicorn
"""

# Local imports
from forms import AutoScoutForm

# Global imports
from flask import Flask, flash, redirect, url_for, render_template, request
import pickle
import pandas as pd

# App configs
app = Flask(__name__)
app.config['SECRET_KEY'] = 'NYbow8yu5c5Tma96XN2xhQzfedshdjrtit'

# Model loading:
print("Loading Pre-trained Model ...")
with open('MLD_Clf.pkl', 'rb') as file: 
    AutoScout_Model = pickle.load(file)

# Model predection functions:
def AutoScout_Model_pred(new_obs):
    pred = AutoScout_Model.predict(new_obs) # user_input = [car_model, hp_kw, km, car_age, engine_size, car_usage_type]
    return pred # pred = car_price

# AutoScout landing page:
@app.route("/", methods=['GET', 'POST'])
@app.route('/AutoScout', methods=['GET', 'POST'])
def AutoScout():
    form = AutoScoutForm()
    if form.validate_on_submit():
        my_dict = {
        "make_model": form.car_make_model.data,
        "power_kW": form.car_hp_kW.data,
        "mileage": form.car_mileage.data,
        "age": form.car_age.data,
        "engine_size": form.car_engine_size.data,
        "type": form.car_usage_type.data
        }
        new_obs = pd.DataFrame([my_dict])
        new_obs
        pred = AutoScout_Model_pred(new_obs)
        pred = round(pred[0], 2)
        print("Estimated Car Price is ", pred)
        flash(f"Estimated Car Price is: {pred} $", "success")
        return redirect(url_for('AutoScout'))
    return render_template("AutoScout.html", title = 'AutoScout', form = form)