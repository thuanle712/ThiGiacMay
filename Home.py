import streamlit as st

st.set_page_config(page_title='Trang chủ', page_icon=':bar_chart:', layout='wide')
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.pixabay.com/photo/2019/04/24/11/27/flowers-4151900_960_720.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
add_bg_from_url() 

# Title
st.title('Báo cáo cuối kỳ: Thị Giác Máy')


header = '<p style="font-family: Courier; color: #A40412; font-size: 30px; text-align:;"><b>SV: Lê Ngọc Thuận</b>   __MSSV: 20146435</p>'
st.markdown(header, unsafe_allow_html=True)

header = '<p style="font-family: Courier; color: #A40412; font-size: 30px; text-align:;"><b>GVHD: Trần Tiến Đức</b></p>'
st.markdown(header, unsafe_allow_html=True)


with st.columns(3)[1]:
    st.image('logo.jpg')


c1, c2, c3 = st.columns(3)
with c1:
    st.info('**Web Tham khảo:[@streamlit.io](https://streamlit.io/gallery)**', icon="💡")
with c2:
    st.info('**GitHub:[@streamlit/code](https://github.com/alitaslimi/cross-chain-monitoring/blob/main/Home.py)**', icon="💻")
with c3:
    st.info('**Dữ liệu:[flipsidecrypto.xyz](https://flipsidecrypto.xyz)**', icon="🧠")

