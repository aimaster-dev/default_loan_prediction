from flask import Flask , jsonify , request
from flask_cors import CORS
import lightgbm as lgb
bst = lgb.Booster(model_file='model.txt')
app=Flask(__name__)
CORS(app)
cors=CORS(app,resources={r"/*":{"origins":"*"}})
@app.route('/' , methods=['POST'])
def index():
	def get_or_none(dictionary,key):
		try:
			return(dictionary[key])
		except Exception as e:
			return None
	Gender=get_or_none(request.get_json(),'Gender')
	Married=get_or_none(request.get_json(),'Married')
	Dependents=get_or_none(request.get_json(),'Dependents')
	Education=get_or_none(request.get_json(),'Education')
	Self_employed=get_or_none(request.get_json(),'Self_employed')
	try:
		ApplicantIncome=float(get_or_none(request.get_json(),'ApplicantIncome'))
	except Exception as e:
		ApplicantIncome=None
	try:
		CoapplicantIncome=float(get_or_none(request.get_json(),'CoapplicantIncome'))
	except Exception as e:
		CoapplicantIncome=None
	try:
		LoanAmount=float(get_or_none(request.get_json(),'LoanAmount'))
	except Exception as e:
		LoanAmount=None
	try:
		Loan_Amount_Term=float(get_or_none(request.get_json(),'Loan_Amount_Term'))
	except Exception as e:
		Loan_Amount_Term=None
	try:
		Credit_History=float(get_or_none(request.get_json(),'Credit_History'))
	except Exception as e:
		Credit_History=None
	Property_Area=get_or_none(request.get_json(),'Property_Area')
	res=bst.predict([[ApplicantIncome , CoapplicantIncome , Loan_Amount_Term , Loan_Amount_Term , Credit_History , int(Gender=='Female') , int(Gender=='Male') , int(Married=='No') , int(Married=='Yes') , int(Dependents=='0') , int(Dependents=='1') , int(Dependents=='2') , int(Dependents=='3+') , int(Education=='Graduate') , int(Education=='Under Graduate') , int(Self_employed=='No') , int(Self_employed=='Yes') , int(Property_Area=='Rural') , int(Property_Area=='Semiurban') , int(Property_Area=='Urban')]])
	print(res)
	return(jsonify({'result':res[0]}))
if __name__=='__main__':
	app.run(debug=True)
