import tkinter as tk
import pandas as pd

# 讀取Excel文件
file_path = './報到處選手名單.xlsx'
df = pd.read_excel(file_path, engine='openpyxl')

def show_text(event=None):
    number = entry.get()
    if number:
        try:
            # 找到對應的選手信息
            result = df.loc[df['選手證號碼'] == int(number)]
            if not result.empty:
                player_number = int(result['選手證號碼'].values[0])  # 確保號碼是整數型態
                player_name = result['選手'].values[0]
                size = result['衣服尺寸'].values[0]


                display_label = tk.Label(display_window, text=f"姓名: {player_name}, 號碼: {player_number}, 尺寸: {size}", font=("Helvetica", 72))
                # 將 "yes" 寫回到對應的單元格
                df.loc[df['選手證號碼'] == int(number), '註記'] = "v"
                df.to_excel(file_path, index=False, engine='openpyxl')

                
            else:
                display_label = tk.Label(display_window, text="找不到對應的選手信息", font=("Helvetica", 24))
            display_label.pack(pady=5)
            display_window.after(45000, display_label.destroy)  # 30秒後自動刪除標籤
        except (IndexError, ValueError):
            display_label = tk.Label(display_window, text="找不到對應的選手信息", font=("Helvetica", 24))
            display_label.pack(pady=5)
            display_window.after(30000, display_label.destroy)  # 30秒後自動刪除標籤
        entry.delete(0, tk.END)  # 清空輸入框

root = tk.Tk()
root.title("Input Window")

# 輸入框
entry = tk.Entry(root, font=("Helvetica", 24))
entry.grid(row=0, column=0, padx=20, pady=20)
entry.bind("<Return>", show_text)  # 綁定Enter鍵

# 顯示按鈕
button = tk.Button(root, text="顯示選手編號", command=show_text, font=("Helvetica", 24))
button.grid(row=0, column=1, padx=20, pady=20)

# 顯示多次輸入的視窗
display_window = tk.Toplevel(root)
display_window.title("一點不慌啊")

root.mainloop()
