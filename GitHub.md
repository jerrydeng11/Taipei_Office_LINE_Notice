# GitHub

## 建立GitHub專案

1. 開啟 [GitHub](https://github.com/)
2. + => New repostory
3. Repository name `Taipei_Office_LINE_Notice`
4. 勾選 `Private`
5. 點擊 `Create repository`

設定分享

1. Settings
2. Manage access
3. 輸入帳號密碼
4. 點擊 `Invite a collaborator`
5. 輸入分享對象GitHub帳號
6. 點擊綠色按鈕

命令行上創建新的存儲庫

```bash
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:jerrydeng11/Taipei_Office_LINE_Notice.git
git push -u origin main
```
