from flask import Flask, request, render_template, redirect, url_for
import pandas as pd

app = Flask(__name__)

# 讀取Excel文件
file_path = './報到處選手名單.xlsx'
df = pd.read_excel(file_path, engine='openpyxl')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        if name:
            try:
                result = df.loc[df['選手'] == name]
                if not result.empty:
                    player_number = int(result['選手證號碼'].values[0])
                    player_name = result['選手'].values[0]
                    team_name = result['隊名'].values[0]
                    size = result['衣服尺寸'].values[0]
                    first = result['項目1'].values[0]
                    if pd.notna(result['項目2'].values[0]):
                        second = result['項目2'].values[0]
                    else:
                        second = "無項目2"
                    # second = result['衣服尺寸'].values[0]

                    if len(player_name) < 5:
                        font_size = 20
                    else:
                        font_size = 30

                    # 將 "v" 寫回到對應的單元格
                    # df.loc[df['選手證號碼'] == name, '註記'] = "v"
                    # df.to_excel(file_path, index=False, engine='openpyxl')

                    return render_template('index.html', player_name=player_name, player_number=player_number, size=size, font_size=font_size, first=first, second=second,team_name=team_name)
                else:
                    return render_template('index.html', error="找不到對應的選手信息")
            except (IndexError, ValueError):
                return render_template('index.html', error="找不到對應的選手信息")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
