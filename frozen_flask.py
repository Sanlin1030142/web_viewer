from flask_frozen import Freezer
from app import app  # 從您的 Flask 應用程序導入 app 實例


app.config['FREEZER_DESTINATION'] = 'build'  # 指定凍結檔案的目錄
freezer = Freezer(app)  # 創建一個 Freezer 實例

if __name__ == '__main__':
    freezer.freeze()  # 開始凍結過程，生成靜態檔案
