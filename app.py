import streamlit as st
from PIL import Image

st.set_page_config(page_title="Test Upload Ảnh", layout="centered")

st.title("🖼️ Kiểm tra Upload Ảnh Streamlit")
st.write("Tải lên một ảnh và xem kích thước của nó.")

st.subheader("Tải ảnh của bạn lên đây:")
uploaded_file = st.file_uploader("Chọn một tệp ảnh", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:

    st.success(f"Đã tải lên thành công tệp: {uploaded_file.name}")

    try:
        image = Image.open(uploaded_file)

        st.image(image, caption=f"Ảnh đã tải lên: {uploaded_file.name}", use_column_width=True)

        width, height = image.size

        st.subheader("Thông tin kích thước ảnh:")
        st.write(f"- Chiều rộng: **{width}** pixels")
        st.write(f"- Chiều cao: **{height}** pixels")

    except Exception as e:
        st.error(f"Lỗi khi xử lý ảnh: {e}")
        st.warning("Hãy đảm bảo bạn đã tải lên một tệp ảnh hợp lệ (PNG, JPG, JPEG).")

else:
    st.info("Chưa có tệp nào được tải lên.")

# --- Thông tin thêm (Tùy chọn) ---
st.sidebar.header("Về ứng dụng này")
st.sidebar.info("Ứng dụng demo cơ bản để test upload và lấy kích thước ảnh bằng Streamlit.")
