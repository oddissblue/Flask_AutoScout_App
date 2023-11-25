# Global dependencies
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired

# Local dependencies:


# AutoScout form:
class AutoScoutForm(FlaskForm):
    car_make_model = SelectField('Car Model', choices=['Mercedes-Benz A 180', 'Opel Astra', 'Opel Corsa', 'Opel Adam',
                                                  'Opel Insignia', 'Opel Cascada', 'Opel Grandland X',
                                                  'Renault Megane', 'Renault Clio', 'Renault Captur',
                                                  'Renault Talisman', 'Renault Kadjar', 'Peugeot 308', 'Peugeot 208',
                                                  'Peugeot 207', 'Peugeot 3008', 'Peugeot 508', 'Peugeot RCZ',
                                                  'Peugeot 206', 'Peugeot 2008', 'Fiat 500', 'Fiat Tipo',
                                                  'Fiat 500X', 'Fiat Panda', 'Fiat 500C', 'SEAT Leon', 'SEAT Ibiza',
                                                  'SEAT Arona', 'SEAT Ateca', 'Skoda Fabia'],
                                                  validators=[DataRequired()])
    car_hp_kW = IntegerField('Car HoursePower Per KiloWatt', validators=[DataRequired()])
    car_mileage = IntegerField('Car Mileage', validators=[DataRequired()])
    car_age = IntegerField('Car Age', validators=[DataRequired()])
    car_engine_size = IntegerField('Car Engine Size', validators=[DataRequired()])
    car_usage_type = SelectField('Car Usage Type', choices=['Used', 'Pre-registered', 'Demonstration', "Employee's car"], validators=[DataRequired()])
    submit = SubmitField('Estimate Car Price')