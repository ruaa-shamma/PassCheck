import os
from flask import  Flask , render_template , request
#Flask: مكتبة تساعدنا نعمل موقع ويب (تطبيق ويب) بلغة Python بسهولة.
#render_template: تستخدم لعرض صفحات HTML.
#request: تستخدم للحصول على البيانات من المستخدم، مثل كلمة السر اللي يدخلها.
#re: مكتبة الـ Regular Expressions، تساعدنا نبحث عن أنماط معينة داخل النصوص، مثل الأرقام أو الحروف الكبيرة.
import re
app= Flask(__name__)     #ننشئ تطبيق فلاسك ونخزن الكائن في متغير app

#كود التحقق من كلمة السر 
def check_pass(password):
    strength=0 # وظيفته تخزين قوة كلمة المرور اثناء التقييم 
    if len(password)>=6:
        strength+=1  #اذا الطول اكبر من 6 خزن التقيم اعطيه نقطه
    if len(password)>=10:# طبعا هون عن طول كلمة السر منحكي 
        strength+=1
    
    if re.search(r"\d",password):
        strength+=1
        
    if re.search(r"[A-Z]", password):
        strength += 1
        
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    #حالات كلمة السر بالنسبة لطول السلسلة وماذا ترجع 
    if strength<=2:
        return "Weak "
    elif strength ==3:
        return "Medium"
    else:
        return "Strong" 

@app.route("/", methods=["GET", "POST"])  
def home():
    result = ""
    if request.method == "POST":
        password = request.form["password"]  # يتحقق إذا المستخدم ضغط على زر وأرسل كلمة السر
        result = check_pass(password)  # يحسب قيمة قوة كلمة المرور
    return render_template("pass.html", result=result)  # يعرض صفحة الويب ويعطيها نتيجة قوة كلمة المرور

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))