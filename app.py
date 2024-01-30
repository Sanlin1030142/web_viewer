import os
from flask import Flask, render_template

app = Flask(__name__)

def sort_key(file_name):
    # 假設文件名是 "chapter_1.txt"，"chapter_10.txt" 等
    # 移除 "chapter_" 和 ".txt"，然後將剩下的部分轉換為整數
    return int(file_name.replace("chapter_", "").replace(".txt", ""))

# 增加系統首頁 / 的路由
# 使用index.html模板
@app.route('/')
def index():
    books_directory = './books/'
    # 获取所有子目录的名称
    books = [d for d in os.listdir(books_directory) if os.path.isdir(os.path.join(books_directory, d))]

    # 检查每本书的封面图片是否存在
    book_covers = {}
    for book in books:
        cover_path = 'img/' + book + '.png'
        full_cover_path = os.path.join('static', cover_path)
        if os.path.isfile(full_cover_path):
            book_covers[book] = cover_path
        else:
            book_covers[book] = 'img/cover.png'  # 默认封面

    return render_template('index.html', books=books, book_covers=book_covers)

@app.route('/list_files/<book_name>')
def list_files(book_name):
    directory = os.path.join('./books/', book_name)
    # 确保文件列表是按字典顺序排序的
    files = sorted([f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))], key=sort_key)
    return render_template('list_files.html', files=files, book_name=book_name)

@app.route('/article/<book_name>/<filename>')
def article(book_name, filename):
    directory = os.path.join('./books/', book_name)
    # 获取排序后的文件列表
    files = sorted([f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))], key=sort_key)
    file_path = os.path.join(directory, filename)

    if os.path.exists(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except UnicodeDecodeError:
            with open(file_path, 'r', encoding='gb2312') as f:
                content = f.read()

        # 更改content中的换行符，以便在HTML中正确显示
        content = content.replace('\n', '<br>')
        content = content.replace('<br/>', '<br>')

        # 找出当前文件在列表中的位置
        current_index = files.index(filename)
        # 获取下一个文件的名称，如果当前文件是列表中的最后一个，则返回第一个文件
        next_index = (current_index + 1) % len(files)
        # 获取上一个文件的名称，如果当前文件是列表中的第一个，则返回最后一个文件
        previous_index = (current_index - 1) % len(files)

        next_filename = files[next_index]
        previous_filename = files[previous_index]
        return render_template('article.html', content=content, next_filename=next_filename, previous_filename=previous_filename, book_name=book_name)
    else:
        return "文章不存在"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

