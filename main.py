
# ==================随堂练习要求====================================
# 补充第21行代码，从pickle文件中取出Python数据
# 补充第45行代码，将Python数据存入pickle文件中
#===================================================================
from flask import Flask,render_template,request,redirect
from getnews import get_news
from savefile import save_path

# 引入pickle 模块
import pickle

app = Flask(__name__)


with open("works.pickle",'rb') as f:
    
# ==============补充第21行代码=============================================================
# 要求:使用pickle模块的load函数从打开的pickle文件(f)中取出数据；
# 注意：load函数有一个参数是打开的文件变量名f
    works = pickle.load(f)

#============================================================================


@app.route('/processwork',methods=['POST'])
def process_work():
    title = request.values.get("title")
    link = request.values.get("link")
    file = request.files.get('file')
    if title and link and file:
        fname = file.filename
        fpath = save_path(fname)
        file.save(fpath)
        
        new_work = {"title":title,"link":link,"file":fname}
        works.append(new_work)
        
# ==============补充第45行代码=============================================================
# 要求:使用pickle模块的dump函数将python数据works存储到打开的pickle文件(f)中；
# 注意：dump函数有两个参数:
#      第一个是需要存储的数据works
#      第二个是打开的文件变量名f
        with open("works.pickle",'wb') as f:
            pickle.dump(works,f)
            
# =====================================================
        return redirect("/")
        
    else:
        return render_template("uploadwork.html")




@app.route('/')
def index():
    hot_news = get_news()
    return render_template('index.html', news = hot_news,works = works)
  
        
@app.route('/privatepic')
def private():
    who = request.values.get("who")
    animal = request.values.get("animal")
    food = request.values.get("food")
    if who == '快乐星球' and animal == "狗" and food == "汉堡包":
        img_list = ['兔子.jpg', '小丸子.png', '小熊.jpg']
        return render_template("privatepic.html",pictures = img_list)
    return render_template("privatepic.html")

@app.route("/uploadwork")
def upload_work():
    return render_template("uploadwork.html")

app.run()