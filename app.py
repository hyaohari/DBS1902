#!/usr/bin/env python
# coding: utf-8

# In[29]:


from flask import Flask


# In[30]:


app = Flask(__name__)


# In[31]:


from flask import request, render_template
import joblib

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        rates = request.form.get("rates")
        print(rates)
        model = joblib.load("DBSReg")
        pred = model.predict([[float(rates)]])
        s = "Predicted DBS share price based on linear regression model is: " + str(pred[0][0])
        model2 = joblib.load("DBSDT")
        pred2 = model2.predict([[float(rates)]])
        t = "Predicted DBS share price based on decision tree model is: " + str(pred2[0])
        model3 = joblib.load("DBSNN")
        pred3 = model3.predict([[float(rates)]])
        u = "Predicted DBS share price based on neural network model is: " + str(pred3[0])
        return(render_template("index.html", result1=s, result2=t, result3=u))
    else:
        return(render_template("index.html", result1="2", result2="2", result3="2"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




