import streamlit as st
import sys
import cv2
import numpy as np
from PIL import Image
import Chapter3 as c3
import Chapter4 as c4
import Chapter9 as c9

st.set_page_config(
    page_title="Image Processing",
    page_icon="📸",
)
st.markdown("<h2 style = 'text-align: center; font-size: 40px; font-family: comic sans ms, cursive; color: #800000;'>Image Processing</h2>", unsafe_allow_html=True)
st.sidebar.header("Digital Image Processing")

def imgin_header():
    imgin_Title = '<p style="font-family: Courier; color: #3333ff; font-size: 24px;"><b>Original Uploaded Image</b></p>'
    st.markdown(imgin_Title, unsafe_allow_html=True)
def imgout_header():
    imgout_Title = '<p style="font-family: Courier; color: #3333ff; font-size: 24px;"><b>Image after being processed</b></p>'
    st.markdown(imgout_Title, unsafe_allow_html=True)
def download_info():
    download_notice = '<p style="font-family: monospace; font-size: 14px; color: #c2c2d6;"><i>For downloading, please right click on the image.</i></p>'
    st.markdown(download_notice, unsafe_allow_html=True) 
    

option = st.sidebar.selectbox('Choose topic', ['--Select topic--', 'Chương 3', 'Chương 4', 'Chương 9'])
if option == 'Chương 3':
    img_upload = st.file_uploader('Upload Image', type=['jpg', 'tif', 'bmp', 'gif', 'png'])
    if img_upload is not None:
            global imgin
            filepath = 'D:\ProjectCuoiKy\ProcessingImage\Chuong3\\' + img_upload.name
            imgin = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
            imgin_header()
            st.image(imgin)

            c3_function = st.sidebar.selectbox('Please pick up a function', [
                '--Select function--','Negative', 'Logarit', 'Power', 'PieceWiseLinear', 'Histogram',
                'HistogramEqualization', 'LocalHistogram', 'HistogramStatistics',
                'SmoothingGauss', 'Smoothing', 'MedianFilter', 'Sharpen', 'UnSharpMasking', 'Gradient'])
            # Negative
            if c3_function == 'Negative':
                global imgout
                imgout = np.zeros(imgin.shape, np.uint8)
                c3.Negative(imgin,imgout)
                imgout_header()
                st.image(imgout)
                download_info()
                state = '<p style="font-family: didot, serif; color: #000000; font-size: 18px; texxt-align: left;">Current selected function: Negative</p>'
                st.sidebar.markdown(state, unsafe_allow_html=True)
                quote = '<p style="font-family: didot; color: #81293B; font-size: 18px; texxt-align: left;"><i>Hàm làm âm ảnh: ảnh từ trắng thành đen và từ đen thành trắng.</i></p>'
                st.sidebar.markdown(quote, unsafe_allow_html=True)
            # Logarit
            elif c3_function == 'Logarit':
                imgout = np.zeros(imgin.shape, np.uint8)
                c3.Logarit(imgin,imgout)
                imgout_header()
                st.image(imgout)
                download_info()
                state = '<p style="font-family: didot, serif; color: #000000; font-size: 18px; texxt-align: left;">Current selected function: Logarit</p>'
                st.sidebar.markdown(state, unsafe_allow_html=True)
                quote = '<p style="font-family: cursive; color: #81293B; font-size: 16px; texxt-align: left;"><i>Kết quả hàm Logarit: ảnh sáng ít thì làm cho sáng nhiều, ảnh đen nhiều làm cho ảnh đen ít.</i></p>'
                st.sidebar.markdown(quote, unsafe_allow_html=True)
            # Power
            elif c3_function == 'Power':
                imgout = np.zeros(imgin.shape, np.uint8)
                c3.Power(imgin,imgout)
                imgout_header()
                st.image(imgout)
                download_info()
                state = '<p style="font-family: didot, serif; color: #000000; font-size: 18px; texxt-align: left;">Current selected function: Power</p>'
                st.sidebar.markdown(state, unsafe_allow_html=True)
                quote = '<p style="font-family: cursive; color: #81293B; font-size: 16px; texxt-align: left;"><i>Hàm xử lý ảnh bằng phương pháp lũy thừa ảnh: làm cho ảnh tối hơn hay sáng hơn đều được.</i></p>'
                st.sidebar.markdown(quote, unsafe_allow_html=True)
            # PieceWiseLinear
            elif c3_function == 'PieceWiseLinear':
                imgout = np.zeros(imgin.shape, np.uint8)
                c3.PiecewiseLinear(imgin,imgout)
                imgout_header()
                st.image(imgout)
                download_info()
                state = '<p style="font-family: didot, serif; color: #000000; font-size: 18px; texxt-align: left;">Current selected function: PieceWiseLinear </p>'
                st.sidebar.markdown(state, unsafe_allow_html=True)
                quote = '<p style="font-family: cursive; color: #81293B; font-size: 16px; texxt-align: left;"><i>Hàm xử lý bằng phương pháp PieceWise: kết quả làm cho ảnh kéo độ tương phản, phạm vi mức cường độ làm ảnh sáng hơn.</i></p>'
                st.sidebar.markdown(quote, unsafe_allow_html=True)
            # Histogram
            elif c3_function == 'Histogram':
                imgout = np.zeros((imgin.shape[0], 256, 3), np.uint8) + 255
                c3.Histogram(imgin,imgout)
                imgout_header()
                st.image(imgout)
                download_info()
                state = '<p style="font-family: didot, serif; color: #000000; font-size: 18px; texxt-align: left;">Current selected function: Histogram</p>'
                st.sidebar.markdown(state, unsafe_allow_html=True)
                quote = '<p style="font-family: cursive; color: #81293B; font-size: 16px; texxt-align: left;"><i>Hàm xử lý ảnh Histogram, kết quả của ảnh là dạng biểu đồ thể hiện tần suẩt theo dạng cột dữ liệu tương ứng. </i></p>'
                st.sidebar.markdown(quote, unsafe_allow_html=True)
            # HistogramEqualization            
            elif c3_function == 'HistogramEqualization':
                imgout = np.zeros(imgin.shape, np.uint8)
                cv2.equalizeHist(imgin, imgout)
                imgout_header()
                st.image(imgout)
                download_info()
                state = '<p style="font-family: didot, serif; color: #000000; font-size: 18px; texxt-align: left;">Current selected function: HistogramEqualization</p>'
                st.sidebar.markdown(state, unsafe_allow_html=True)
                quote = '<p style="font-family: cursive; color: #81293B; font-size: 16px; texxt-align: left;"><i>Hàm xử lý ảnh HistogramEqualization, làm cho ảnh đẹp và kết quả tốt hơn.</i></p>'
                st.sidebar.markdown(quote, unsafe_allow_html=True)
            # LocalHistogram
            elif c3_function == 'LocalHistogram':
                imgout = np.zeros(imgin.shape, np.uint8)
                c3.LocalHistogram(imgin, imgout)
                imgout_header()
                st.image(imgout)
                download_info()
                state = '<p style="font-family: didot, serif; color: #000000; font-size: 18px; texxt-align: left;">Current selected function: LocalHistogram</p>'
                st.sidebar.markdown(state, unsafe_allow_html=True)
                quote = '<p style="font-family: cursive; color: #81293B; font-size: 16px; texxt-align: left;"><i>Hàm xử lý bằng LocalHistogram, kết quả của hàm làm rõ 1 vùng trong ảnh.</i></p>'
                st.sidebar.markdown(quote, unsafe_allow_html=True)
            # HistogramStatistics
            elif c3_function == 'HistogramStatistics':
                imgout = np.zeros(imgin.shape, np.uint8)
                c3.HistogramStatistics(imgin, imgout)
                imgout_header()
                st.image(imgout)
                download_info()
                state = '<p style="font-family: didot, serif; color: #000000; font-size: 18px; texxt-align: left;">Current selected function: HistogramStatistics </p>'
                st.sidebar.markdown(state, unsafe_allow_html=True)
                quote = '<p style="font-family: cursive; color: #81293B; font-size: 16px; texxt-align: left;"><i>Hàm xử lý ảnh bằng HistogramStatistics, kết quả của hàm đưa ra thống kê 1 vùng trong ảnh.</i></p>'
                st.sidebar.markdown(quote, unsafe_allow_html=True)
            # SmoothingGauss
            elif c3_function == 'SmoothingGauss':
                imgout = c3.SmoothingGauss(imgin)
                imgout_header()
                st.image(imgout)
                download_info()
                state = '<p style="font-family: didot, serif; color: #000000; font-size: 18px; texxt-align: left;">Current selected function: SmoothingGauss</p>'
                st.sidebar.markdown(state, unsafe_allow_html=True)
                quote = '<p style="font-family: cursive; color: #81293B; font-size: 16px; texxt-align: left;"><i>Hàm xử lý ảnh SmoothingGauss, kết quả làm cho ảnh bị nhèo đậm.</i></p>'
                st.sidebar.markdown(quote, unsafe_allow_html=True)
            # Smoothing
            elif c3_function == 'Smoothing':
                imgout = c3.Smoothing(imgin)
                imgout_header()
                st.image(imgout)
                download_info()
                state = '<p style="font-family: didot, serif; color: #000000; font-size: 18px; texxt-align: left;">Current selected function: Smoothing</p>'
                st.sidebar.markdown(state, unsafe_allow_html=True)
                quote = '<p style="font-family: cursive; color: #81293B; font-size: 16px; texxt-align: left;"><i>Hàm xử lý ảnh Smoothing, kết quả làm cho ảnh bị nhèo.</i></p>'
                st.sidebar.markdown(quote, unsafe_allow_html=True)
            # MedianFilter
            elif c3_function == 'MedianFilter':
                imgout = np.zeros(imgin.shape, np.uint8)
                c3.MedianFilter(imgin, imgout)
                imgout_header()
                st.image(imgout)
                download_info()
                state = '<p style="font-family: didot, serif; color: #000000; font-size: 18px; texxt-align: left;">Current selected function: MedianFilter</p>'
                st.sidebar.markdown(state, unsafe_allow_html=True)
                quote = '<p style="font-family: cursive; color: #81293B; font-size: 16px; texxt-align: left;"><i>Hàm xử lý ảnh bằng MedianFilter, kết quả lọc nhiễu ảnh, lọc các điểm ảnh</i></p>'
                st.sidebar.markdown(quote, unsafe_allow_html=True)
            # Sharpen
            elif c3_function == 'Sharpen':
                imgout = c3.Sharpen(imgin)
                imgout_header()
                st.image(imgout)
                download_info()
                state = '<p style="font-family: didot, serif; color: #000000; font-size: 18px; texxt-align: left;">Current selected function: Sharpen</p>'
                st.sidebar.markdown(state, unsafe_allow_html=True)
                quote = '<p style="font-family: cursive; color: #81293B; font-size: 16px; texxt-align: left;"><i>Hàm xử lý Sharpen, kết quả làm ảnh nét hơn.</i></p>'
                st.sidebar.markdown(quote, unsafe_allow_html=True)
            # UnSharpMasking
            elif c3_function == 'UnSharpMasking':
                imgout = c3.UnSharpMasking(imgin)
                imgout_header()
                st.image(imgout)
                download_info()
                state = '<p style="font-family: didot, serif; color: #000000; font-size: 18px; texxt-align: left;">Current selected function: UnSharpMasking</p>'
                st.sidebar.markdown(state, unsafe_allow_html=True)
                quote = '<p style="font-family: cursive; color: #81293B; font-size: 16px; texxt-align: left;"><i>Hàm xử lý UnSharpMasking, kết quả làm ảnh làm ảnh nét hơn.</i></p>'
                st.sidebar.markdown(quote, unsafe_allow_html=True)
            # Gradient
            elif c3_function == 'Gradient':
                imgout = c3.Gradient(imgin)
                imgout_header()
                st.image(imgout)
                download_info()
                state = '<p style="font-family: didot, serif; color: #000000; font-size: 18px; texxt-align: left;">Current selected function: Gradient</p>'
                st.sidebar.markdown(state, unsafe_allow_html=True)
                quote = '<p style="font-family: cursive; color: #81293B; font-size: 16px; texxt-align: left;"><i>Hàm xử lý Gradient, kết quả của hàm Gradient: đạo hàm ống kính tách biên, làm rõ cạnh biên của ảnh.</i></p>'
                st.sidebar.markdown(quote, unsafe_allow_html=True)
            else:
                st.image('waiting.gif', caption='Wait for processing...')
                state = '<p style="font-family: didot, serif; color: #000000; font-size: 18px; texxt-align: left;">Current selected function: Gradient</p>'
                st.sidebar.markdown(state, unsafe_allow_html=True)
                quote = '<p style="font-family: cursive; color: #81293B; font-size: 16px; texxt-align: left;"><i>None</i></p>'
                st.sidebar.markdown(quote, unsafe_allow_html=True)

elif option == 'Chương 4':
    img_upload = st.file_uploader('Upload Image', type=['jpg', 'tif', 'bmp', 'gif', 'png'])
    if img_upload is not None:
        filepath = 'D:\ProjectCuoiKy\ProcessingImage\Chuong4\\' + img_upload.name
        imgin = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
        imgin_header()
        st.image(imgin)

        c4_function = st.sidebar.selectbox('Please pick up a function', [
            '--Select function--','Spectrum', 'FrequencyFilter', 'DrawFilter', 'RemoveMoire'])
        # Spectrum
        if c4_function == 'Spectrum':
            imgout = c4.Spectrum(imgin)
            imgout_header()
            st.image(imgout)
            download_info()
            state = '<p style="font-family: didot, serif; color: #000000; font-size: 18px; texxt-align: left;">Current selected function: Spectrum</p>'
            st.sidebar.markdown(state, unsafe_allow_html=True)
            quote = '<p style="font-family: cursive; color: #81293B; font-size: 16px; texxt-align: left;"><i>Hàm xử ảnh Spectrum, kết quả: xử lý quang phổ bằng các công thức tần số sóng điện từ, ánh sáng, điểm ảnh.</i></p>'
            st.sidebar.markdown(quote, unsafe_allow_html=True)
        # FrequencyFilter
        elif c4_function == 'FrequencyFilter':
            imgout = c4.FrequencyFilter(imgin)
            imgout_header()
            st.image(imgout)
            download_info()
            state = '<p style="font-family: didot, serif; color: #000000; font-size: 18px; texxt-align: left;">Current selected function: FrequencyFilter</p>'
            st.sidebar.markdown(state, unsafe_allow_html=True)
            quote = '<p style="font-family: cursive; color: #81293B; font-size: 16px; texxt-align: left;"><i>Hàm xử lý ảnh FrequencyFilter, kết quả: bọ lọc cho tín hiệu có tần số thấp hơn tần số cắt đã chọn, hàm làm suy giảm tín hiệu có tần số cao hơn tần số cắt để xử lý ảnh.</i></p>'
            st.sidebar.markdown(quote, unsafe_allow_html=True)
        # DrawFilter
        elif c4_function == 'DrawFilter':
            imgout = c4.DrawFilter(imgin)
            imgout_header()
            st.image(imgout)
            download_info()
            state = '<p style="font-family: didot, serif; color: #000000; font-size: 18px; texxt-align: left;">Current selected function: DrawFilter</p>'
            st.sidebar.markdown(state, unsafe_allow_html=True)
            quote = '<p style="font-family: cursive; color:#81293B; font-size: 16px; texxt-align: left;"><i>Hàm xử lý ảnh DrawFilter, kết quả: xử lý lọc ảnh cơ bản.</i></p>'
            st.sidebar.markdown(quote, unsafe_allow_html=True)
        # RemoveMoire
        elif c4_function == 'RemoveMoire':
            imgout = c4.RemoveMoire(imgin)
            imgout_header()
            st.image(imgout)
            download_info()
            state = '<p style="font-family: didot, serif; color: #000000; font-size: 18px; texxt-align: left;">Current selected function: RemoveMoire</p>'
            st.sidebar.markdown(state, unsafe_allow_html=True)
            quote = '<p style="font-family: cursive; color: #81293B; font-size: 16px; texxt-align: left;"><i>Hàm xử lý ảnh RemoveMoire, kết quả: xóa các điểm nhiễu ảnh.</i></p>'
            st.sidebar.markdown(quote, unsafe_allow_html=True)
        else:
            st.image('waiting.gif', caption='Wait for processing...')
            state = '<p style="font-family: didot, serif; color: #000000; font-size: 18px; texxt-align: left;">Current selected function: RemoveMoire</p>'
            st.sidebar.markdown(state, unsafe_allow_html=True)
            quote = '<p style="font-family: cursive; color: #81293B; font-size: 16px; texxt-align: left;"><i>None</i></p>'
            st.sidebar.markdown(quote, unsafe_allow_html=True)

elif option == 'Chương 9':
    img_upload = st.file_uploader('Upload Image', type=['jpg', 'tif', 'bmp', 'gif', 'png'])
    if img_upload is not None:
        filepath = 'D:\ProjectCuoiKy\ProcessingImage\Chuong9\\' + img_upload.name
        imgin = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
        imgin_header()
        st.image(imgin)

        c9_function = st.sidebar.selectbox('Please pick up a function', [
            '--Select function--','Erosion', 'Dilation', 'OpeningClosing', 'Boundary', 'HoleFill', 
            'MyConnectedComponent', 'ConnectedComponent', 'CountRice'])
        # Erosion
        if c9_function == 'Erosion':
            imgout = np.zeros(imgin.shape, np.uint8)
            c9.Erosion(imgin, imgout)
            imgout_header()
            st.image(imgout)
            download_info()
            state = '<p style="font-family: didot, serif; color: #000000; font-size: 18px; texxt-align: left;">Current selected function: Erosion</p>'
            st.sidebar.markdown(state, unsafe_allow_html=True)
            quote = '<p style="font-family: cursive; color: #81293B; font-size: 16px; texxt-align: left;"><i>Hàm xử lý ảnh Erosion, kết quả: làm bào mòn ảnh.</i></p>'
            st.sidebar.markdown(quote, unsafe_allow_html=True)
        # Dilation
        elif c9_function == 'Dilation':
            imgout = np.zeros(imgin.shape, np.uint8)
            c9.Dilation(imgin, imgout)
            imgout_header()
            st.image(imgout)
            download_info()
            state = '<p style="font-family: didot, serif; color: #000000; font-size: 18px; texxt-align: left;">Current selected function: Dilation</p>'
            st.sidebar.markdown(state, unsafe_allow_html=True)
            quote = '<p style="font-family: cursive; color: #81293B; font-size: 16px; texxt-align: left;"><i>Hàm xử lý ảnh Dilation, kết quả: làm giãn nở ảnh, làm mập ảnh.</i></p>'
            st.sidebar.markdown(quote, unsafe_allow_html=True)
        # OpeningClosing
        elif c9_function == 'OpeningClosing':
            imgout = np.zeros(imgin.shape, np.uint8)
            c9.OpeningClosing(imgin, imgout)
            imgout_header()
            st.image(imgout)
            download_info()
            state = '<p style="font-family: didot, serif; color: #000000; font-size: 18px; texxt-align: left;">Current selected function: OpeningClosing</p>'
            st.sidebar.markdown(state, unsafe_allow_html=True)
            quote = '<p style="font-family: cursive; color: #81293B; font-size: 16px; texxt-align: left;"><i>Hàm xử lý ảnh OpeningClosing, kết quả: dùng để xóa nhiễu ảnh.</i></p>'
            st.sidebar.markdown(quote, unsafe_allow_html=True)
        # Boundary
        elif c9_function == 'Boundary':
            imgout = c9.Boundary(imgin)
            imgout_header()
            st.image(imgout)
            download_info()
            state = '<p style="font-family: didot, serif; color: #000000; font-size: 18px; texxt-align: left;">Current selected function: Boundary</p>'
            st.sidebar.markdown(state, unsafe_allow_html=True)
            quote = '<p style="font-family: cursive; color: #81293B; font-size: 16px; texxt-align: left;"><i>Hàm xử lý ảnh Boundary, kết quả: phân biệt điểm ảnh, khoanh vùng điểm biên của ảnh.</i></p>'
            st.sidebar.markdown(quote, unsafe_allow_html=True)
        # HoleFill
        elif c9_function == 'HoleFill':
            imgout = c9.HoleFill(imgin)
            imgout_header()
            st.image(imgout)
            download_info()
            state = '<p style="font-family: didot, serif; color: #000000; font-size: 18px; texxt-align: left;">Current selected function: HoleFill</p>'
            st.sidebar.markdown(state, unsafe_allow_html=True)
            quote = '<p style="font-family: cursive; color: #81293B; font-size: 16px; texxt-align: left;"><i>Hàm xử lý ảnh HoleFill, kết quả: lắp 1 chỗ trống trên ảnh.</i></p>'
            st.sidebar.markdown(quote, unsafe_allow_html=True)
        # MyConnectedComponent
        elif c9_function == 'MyConnectedComponent':
            imgout = c9.MyConnectedComponent(imgin)
            imgout_header()
            st.image(imgout)
            download_info()
            state = '<p style="font-family: didot, serif; color: #000000; font-size: 18px; texxt-align: left;">Current selected function: MyConnectedComponent</p>'
            st.sidebar.markdown(state, unsafe_allow_html=True)
            quote = '<p style="font-family: cursive; color: #81293B; font-size: 16px; texxt-align: left;"><i>Hàm xử lý ảnh MyConnectedComponent, kết quả: phát hiện được thành phần liên thông và đếm có bao nhiêu miếng xương gà.</i></p>'
            st.sidebar.markdown(quote, unsafe_allow_html=True)
        # ConnectedComponent
        elif c9_function == 'ConnectedComponent':
            imgout = c9.ConnectedComponent(imgin)
            imgout_header()
            st.image(imgout)
            download_info()
            state = '<p style="font-family: didot, serif; color: #000000; font-size: 18px; texxt-align: left;">Current selected function: ConnectedComponent</p>'
            st.sidebar.markdown(state, unsafe_allow_html=True)
            quote = '<p style="font-family: cursive; color: #81293B; font-size: 16px; texxt-align: left;"><i>Hàm xử lý ảnh ConnectedComponent, kết quả: xác định thành phần liên thông, đếm có bao nhiêu miếng xương gà và tách ảnh.</i></p>'
            st.sidebar.markdown(quote, unsafe_allow_html=True)
        # CountRice
        elif c9_function == 'CountRice':
            imgout = c9.CountRice(imgin)
            imgout_header()
            st.image(imgout)
            download_info()
            state = '<p style="font-family: didot, serif; color: #000000; font-size: 18px; texxt-align: left;">Current selected function: CountRice</p>'
            st.sidebar.markdown(state, unsafe_allow_html=True)
            quote = '<p style="font-family: cursive; color: #81293B; font-size: 16px; texxt-align: left;"><i>Hàm xử lý ảnh CountRice, kết quả: đếm được bao nhiêu hạt gạo.</i></p>'
            st.sidebar.markdown(quote, unsafe_allow_html=True)
        else:
            st.image('waiting.gif', caption='Wait for processing...')
            state = '<p style="font-family: didot, serif; color: #000000; font-size: 18px; texxt-align: left;">Current selected function: CountRice</p>'
            st.sidebar.markdown(state, unsafe_allow_html=True)
            quote = '<p style="font-family: cursive; color: #81293B; font-size: 16px; texxt-align: left;"><i>None</i></p>'
            st.sidebar.markdown(quote, unsafe_allow_html=True)
else:
    st.image('welcome.png', use_column_width=True)



        