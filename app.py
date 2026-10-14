import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. Tạo DataFrame
df = pd.DataFrame({
    "Ho_ten": ["Nguyễn Văn An", "Trần Thị Bình", "Lê Minh Chi", "Phạm Quốc Dũng", "Hoàng Thu Hà",
               "Vũ Ngọc Lan", "Đặng Hoàng Minh", "Bùi Thành Nam", "Đỗ Hồng Phúc", "Ngô Thùy Trang"],
    "Chuyen_can": [9, 10, 8, 10, 9, 7, 10, 8, 9, 10],
    "Giua_ky": [7.5, 8, 6, 9, 7, 4.5, 8.5, 7, 7.5, 9.5],
    "Cuoi_ky": [7.5, 8, 5.5, 9, 7, 3.5, 9, 6.5, 7, 9],
})

# 2. Tính điểm tổng kết
df["Tong_ket"] = (0.2 * df["Chuyen_can"] + 0.3 * df["Giua_ky"] + 0.5 * df["Cuoi_ky"]).round(2)


# 3. Xếp loại
def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7.0:
        return "Khá"
    elif diem >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"


df["Xep_loai"] = df["Tong_ket"].apply(xep_loai)

# 4. Thống kê
diem_tb = round(df["Tong_ket"].mean(), 2)
sv_cao_nhat = df.loc[df["Tong_ket"].idxmax()]
sv_thap_nhat = df.loc[df["Tong_ket"].idxmin()]
so_sv_dat = (df["Tong_ket"] >= 5).sum()

# ===== Giao diện Web App =====
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

st.subheader("Bảng điểm")
st.dataframe(df)

st.subheader("Thống kê")
st.write("Điểm trung bình của lớp:", diem_tb)
st.write("Sinh viên có điểm cao nhất:", sv_cao_nhat["Ho_ten"], "-", sv_cao_nhat["Tong_ket"])
st.write("Sinh viên có điểm thấp nhất:", sv_thap_nhat["Ho_ten"], "-", sv_thap_nhat["Tong_ket"])
st.write("Số sinh viên đạt:", so_sv_dat, "/", len(df))

st.subheader("Xem điểm từng sinh viên")
ten = st.selectbox("Chọn sinh viên", df["Ho_ten"])
sv = df[df["Ho_ten"] == ten].iloc[0]
st.write("Chuyên cần:", sv["Chuyen_can"])
st.write("Giữa kỳ:", sv["Giua_ky"])
st.write("Cuối kỳ:", sv["Cuoi_ky"])
st.write("Điểm tổng kết:", sv["Tong_ket"])
st.write("Xếp loại:", sv["Xep_loai"])

# 5. Biểu đồ
st.subheader("Biểu đồ điểm tổng kết")
fig, ax = plt.subplots()
ax.barh(df["Ho_ten"].str.split().str[-1], df["Tong_ket"])
ax.invert_yaxis()
ax.set_title("Điểm tổng kết của 10 sinh viên")
ax.set_xlabel("Điểm tổng kết")
ax.set_ylabel("Sinh viên")
ax.set_xlim(0, 10)
st.pyplot(fig)

# Thông tin người tạo
st.caption("Người tạo: Họ và tên - MSSV: 123456")
