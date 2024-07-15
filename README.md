# 成大羽球公開賽報到處簡易系統，以下說明針對 windows 作業系統，Mac OS 或是 Linux 請另尋它法，理論上大同小異。

* 此系統需要安裝 python 並按照需求安裝相關套件，請自行完成

## 螢幕顯示號碼尺寸 (停留45秒，人多時方便確認衣服尺寸)

* 在正確的路徑資料夾開啟 cmd window 輸入 "python ./test.py" 執行本地端，輸入選手證編號即可顯示選手資訊方便報到處給物資
* 建議改進 :
1. 重複輸入可以把前者自動刪除
2. 新增方法可以再輸入錯之後把螢幕上錯誤資訊刪除

![image](https://github.com/user-attachments/assets/5f144b85-136d-40c8-9140-a55ebe23f16a)

## 輸入名字查找選手編號網頁系統

* "find_number.py" 是利用 flask 架起來的網路架構，由於沒有 server ，必須使用 ngrok 輔助，本資料夾也有 ngrok，但每年版本可能不同，建議去官網下載

  * 執行方式請先在正確的路徑資料夾開啟 cmd window 輸入 "python ./find_number.py" 執行本地端，假設只是要把電腦放在報到處方便大家查編號，可以在該電腦開啟 "http://127.0.0.1:5000" 就好，這樣就不會受到 ngrok 影響，但外網無法存取

   ![image](https://github.com/user-attachments/assets/2a8d726a-a5a4-4eb9-b921-3491eb758dc5)

  * 若要讓外網可以進入，打開 ngrok 並執行 "ngrok http 5000"，執行後應會出現類似下圖畫面，請打開 Forwarding 那行的網址

   ![image](https://github.com/user-attachments/assets/4f208195-41f5-4dec-8b4c-23aadef71406)

  * 打開網址會出現這樣的畫面

  ![image](https://github.com/user-attachments/assets/5d81c313-a365-4635-ae3d-864078eb9026)

  * 常見問題
  
    1. 很多選手打開看到這個畫面以為壞了
    2. ios 似乎都沒問題，部分 android 的手機無法開啟需要多留意

  * 點擊 visit site 即可進入頁面並進行搜尋

  ![image](https://github.com/user-attachments/assets/13f14495-b621-4815-acc8-2fd7f4c4cbc4)

* [示範影片(畫質有點差)](https://www.youtube.com/watch?v=RBIWmHeSh7Q)

* "templates" 是用 html 寫的網頁架構，很陽春，可以修改

* 記得把 excel 表單放在同一層資料夾，必要的話 test.py 以及 find_number.py 內的路徑及名稱必須更動

* 利用 ngrok 這樣的方式每次執行得到的網址都不一樣，且網路速度大概至少 30m (手機網路即可，新館一樓網路太慢)，要確保電腦隨時開著，若重新執行每次得到的網址都不同

* 若有人同名同姓，"find_number.py" 會優先顯示選手證號碼小的選手，還尚未修改需要注意
