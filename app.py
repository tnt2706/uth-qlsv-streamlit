import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

st.set_page_config(page_title="Quản lý điểm sinh viên", page_icon="🎓", layout="centered")

# 1. Tạo DataFrame chứa thông tin 10 sinh viên
df = pd.DataFrame({
    "Họ tên": ["Nguyễn Văn An", "Trần Thị Bình", "Lê Hoàng Cường", "Phạm Minh Dũng", "Hoàng Thu Hà",
               "Vũ Quốc Huy", "Đặng Ngọc Lan", "Bùi Thanh Mai", "Ngô Đức Nam", "Đỗ Phương Thảo"],
    "Chuyên cần": [9.0, 8.5, 7.0, 10.0, 9.5, 6.5, 8.0, 9.0, 7.5, 10.0],
    "Giữa kỳ": [7.5, 8.0, 6.0, 9.0, 8.5, 5.5, 7.0, 8.5, 6.5, 9.5],
    "Cuối kỳ": [8.0, 7.5, 6.5, 9.5, 9.0, 5.0, 7.5, 8.0, 7.0, 9.0],
})

# 2. Tính điểm tổng kết: 20% Chuyên cần + 30% Giữa kỳ + 50% Cuối kỳ
df["Tổng kết"] = (0.2 * df["Chuyên cần"] + 0.3 * df["Giữa kỳ"] + 0.5 * df["Cuối kỳ"]).round(2)


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


df["Xếp loại"] = df["Tổng kết"].apply(xep_loai)

# Màu cho từng loại (dùng cho biểu đồ)
MAU = {"Giỏi": "#2e7d32", "Khá": "#1976d2", "Trung bình": "#f9a825", "Yếu": "#c62828"}

# 4. Thống kê
diem_tb = round(df["Tổng kết"].mean(), 2)
sv_cao_nhat = df.loc[df["Tổng kết"].idxmax()]
sv_thap_nhat = df.loc[df["Tổng kết"].idxmin()]
so_sv_dat = int((df["Tổng kết"] >= 5).sum())

# ===== Giao diện Web App =====
st.title("🎓 QUẢN LÝ ĐIỂM SINH VIÊN")
st.caption("Điểm tổng kết = 20% Chuyên cần + 30% Giữa kỳ + 50% Cuối kỳ")
st.divider()

# --- Thống kê nhanh ---
st.subheader("📊 Thống kê lớp")
c1, c2, c3, c4 = st.columns(4)
c1.metric("Điểm TB lớp", diem_tb)
c2.metric("Cao nhất", sv_cao_nhat["Tổng kết"])
c3.metric("Thấp nhất", sv_thap_nhat["Tổng kết"])
c4.metric("SV đạt (≥ 5)", f"{so_sv_dat}/{len(df)}")

st.success(f"🏆 Sinh viên điểm cao nhất: **{sv_cao_nhat['Họ tên']}** ({sv_cao_nhat['Tổng kết']})")
st.warning(f"📉 Sinh viên điểm thấp nhất: **{sv_thap_nhat['Họ tên']}** ({sv_thap_nhat['Tổng kết']})")

# --- Bảng điểm ---
st.subheader("📋 Bảng điểm")
st.dataframe(
    df,
    width="stretch",
    hide_index=True,
    column_config={
        "Tổng kết": st.column_config.ProgressColumn("Tổng kết", min_value=0, max_value=10, format="%.2f"),
    },
)

# --- Xem điểm từng sinh viên ---
st.subheader("🔍 Xem điểm từng sinh viên")
ten = st.selectbox("Chọn sinh viên", df["Họ tên"])
sv = df[df["Họ tên"] == ten].iloc[0]

with st.container(border=True):
    st.markdown(f"#### {sv['Họ tên']}")
    a, b, c = st.columns(3)
    a.metric("Chuyên cần", sv["Chuyên cần"])
    b.metric("Giữa kỳ", sv["Giữa kỳ"])
    c.metric("Cuối kỳ", sv["Cuối kỳ"])
    d, e = st.columns(2)
    d.metric("Điểm tổng kết", sv["Tổng kết"], delta=round(sv["Tổng kết"] - diem_tb, 2),
             help="Mũi tên: chênh lệch so với điểm trung bình lớp")
    e.metric("Xếp loại", sv["Xếp loại"])

# 5. Biểu đồ
st.subheader("📈 Biểu đồ điểm tổng kết")
ten_ngan = df["Họ tên"].str.split().str[-1]   # lấy tên (từ cuối) cho gọn
mau_cot = df["Xếp loại"].map(MAU)

fig, ax = plt.subplots(figsize=(8, 5.5))
ax.barh(ten_ngan, df["Tổng kết"], color=mau_cot)
ax.invert_yaxis()   # SV đầu danh sách nằm trên cùng
for i, d in enumerate(df["Tổng kết"]):
    ax.text(d + 0.1, i, f"{d:.2f}", va="center")
ax.axvline(5, color="gray", linestyle="--", linewidth=1)   # mốc đạt
ax.set_title("Điểm tổng kết của 10 sinh viên")
ax.set_xlabel("Điểm tổng kết")
ax.set_ylabel("Sinh viên")
ax.set_xlim(0, 10.5)
ax.grid(axis="x", alpha=0.3)
# chú thích màu theo xếp loại
chu_thich = [Patch(color=mau, label=loai) for loai, mau in MAU.items()]
ax.legend(handles=chu_thich, loc="upper center", bbox_to_anchor=(0.5, -0.12), ncol=4, frameon=False)
fig.tight_layout()
st.pyplot(fig)
plt.close(fig)

# Số lượng theo xếp loại
st.write("**Số sinh viên theo xếp loại:**")
st.bar_chart(df["Xếp loại"].value_counts().reindex(MAU.keys(), fill_value=0),
             horizontal=True, height=220, color="#1976d2")

st.divider()
# Thông tin người tạo
st.caption("Người tạo: Bạch Đăng Khôi - MSSV: 066208015812")
