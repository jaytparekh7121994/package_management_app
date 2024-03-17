from wtforms import StringField, SubmitField, IntegerField
from flask_wtf import FlaskForm

class AddCustomerForm(FlaskForm):

    name = StringField('Customer Name: ')
    submit = SubmitField('Add Customer')

class AddPackageForm(FlaskForm):
    
    product = StringField('Product Name: ')
    submit = SubmitField("Add Package")

class DeletePackageForm(FlaskForm):

    id = StringField("Package Id: ")
    submit= SubmitField("Remove Package")

class AssignCustomerForm(FlaskForm):

    package_id = IntegerField("Package Id: ")
    customer_id = IntegerField("Customer Id: ")
    submit = SubmitField("Assign Package to Customer")


class DeleteCustomerForm(FlaskForm):

    id = StringField("Customer Id: ")
    submit = SubmitField("Remove Customer")