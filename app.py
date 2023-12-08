import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def list_files():
    directory = '../grep1'
    # 确保文件列表是按字典顺序排序的
    files = sorted([f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))])
    return render_template('list_files.html', files=files)

@app.route('/article/<filename>')
def article(filename):
    directory = '../grep1'
    # 同样，获取排序后的文件列表
    files = sorted([f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))])
    file_path = os.path.join(directory, filename)
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        # 找出当前文件在列表中的位置
        current_index = files.index(filename)
        # 获取下一个文件的名称，如果当前文件是列表中的最后一个，则返回第一个文件
        next_index = (current_index + 1) % len(files)
        # 獲取上一個文件的名稱，如果當前文件是列表中的第一個，則返回最後一個文件
        previous_index = (current_index - 1) % len(files)

        next_filename = files[next_index]
        previous_filename = files[previous_index]
        return render_template('article.html', content=content, next_filename=next_filename, previous_filename=previous_filename)
    else:
        return "文章不存在"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

