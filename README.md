# Quản lý điểm sinh viên - Streamlit

Project thực hành Python: dùng Pandas tính điểm tổng kết, xếp loại, thống kê, vẽ biểu đồ bằng Matplotlib và làm Web App bằng Streamlit.

## Cấu trúc thư mục

```
uth-qlsv-streamlit/
├── app.py                       # Web App Streamlit
├── requirements.txt             # thư viện cần cài khi deploy
├── TenSTT_pythonproject.ipynb   # notebook chạy trên Colab (#0 -> #5)
└── README.md
```

## Kế hoạch thực hiện

| Bước | Việc cần làm | Kết quả |
|---|---|---|
| 1 | Mở `TenSTT_pythonproject.ipynb` trên Colab (File → Upload notebook), đổi tên theo tên + STT của mình | Notebook trên Colab |
| 2 | Sửa họ tên, MSSV ở ô đầu tiên, rồi Runtime → Run all | Có kết quả từng ô #1 → #5 |
| 3 | Chụp màn hình code + kết quả từng ô, ghép thành `TenSTT_pythonproject.pdf` | File PDF nộp bài |
| 4 | Sửa dòng `st.caption(...)` cuối `app.py` thành họ tên + MSSV thật | Footer đúng thông tin |
| 5 | Chạy thử trên máy (xem bên dưới) | App chạy ở localhost |
| 6 | Đưa code lên GitHub | Repo public |
| 7 | Deploy lên Streamlit Community Cloud | Link Web App để nộp |

## Chạy thử trên máy

```bash
pip install -r requirements.txt
streamlit run app.py
```

Mở trình duyệt tại http://localhost:8501

## Đưa lên GitHub

Cách dễ nhất (không cần dùng lệnh):

1. Vào https://github.com → **New repository** → đặt tên `uth-qlsv-streamlit`, chọn **Public** → Create.
2. Bấm **uploading an existing file** → kéo thả `app.py` và `requirements.txt` → **Commit changes**.

Hoặc dùng git:

```bash
git init
git add app.py requirements.txt README.md
git commit -m "Quan ly diem sinh vien"
git branch -M main
git remote add origin https://github.com/tnt2706/uth-qlsv-streamlit.git
git push -u origin main
```

## Deploy lên Streamlit

1. Vào https://share.streamlit.io → đăng nhập bằng GitHub.
2. Bấm **Create app** → **Deploy a public app from GitHub**.
3. Chọn repo `uth-qlsv-streamlit`, branch `main`, main file `app.py` → **Deploy**.
4. Đợi 1–2 phút, copy link dạng `https://xxx.streamlit.app` để nộp.

## Nộp bài

- File `TenSTT_pythonproject.pdf` (ảnh chụp code + kết quả trên Colab)
- Link Web App Streamlit
