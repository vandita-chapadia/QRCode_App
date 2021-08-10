import os.path
from PIL import Image
import streamlit as st
import numpy as np
import qrcode
import os
import time
import cv2
timestr=time.strftime("%Y%m%d-%H%M%S")
qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=14)


def load_image(img):
    im=Image.open(img)
    return im




def main():
    menu=["Home","DecodeQR","About"]

    choice=st.sidebar.selectbox("Menu",menu)

    if choice == "Home":
        st.subheader("Home")
        with st.form(key='myqr_form'):
            row_text=st.text_area("Text Here")
            submit_button=st.form_submit_button("Generate")

        if submit_button:
            col1,col2 =st.columns(2)
            with col1:
                qr.add_data(row_text)
                qr.make(fit=True)
                img=qr.make_image(fill_color='black',back_color='white')
                img_filename='generate_image_{}.png'.format(timestr)
                path_for_images=os.path.join('image_folder',img_filename)
                img.save(path_for_images)

                final_img=load_image(path_for_images)
                st.image(final_img)


            with col2:
                st.info("Original Text")
                st.write(row_text)


    elif choice == "DecodeQR":
        st.subheader("Decode QR")

        image_file=st.file_uploader("Upload Image",type=['jpg','png','jpeg'])

        if image_file is not None:
            file_bytes=np.asarray(bytearray(image_file.read()),dtype=np.uint8)
            opencv_img=cv2.imdecode(file_bytes,1)
            c1, c2 = st.columns(2)
            with c1:
                st.image(opencv_img)
            with c2:
                st.info("Decoded QR Code")
                det=cv2.QRCodeDetector()
                retval,point,straingt_qrcode=det.detectAndDecode(opencv_img)
                st.write(retval)




    else:
        st.subheader("About")
        st.write("This Application is about to Generate QR Code from given data in Textfield and also Decode QR Code by Uploading QR Code image in png,jpg,jpeg format")




if __name__ == '__main__':
    main()