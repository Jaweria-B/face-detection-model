import streamlit as st
import cv2

def takeImage():
    uploaded_file = st.file_uploader("Choose a image", type = ['jpg', 'png'])
    
    if uploaded_file is not None:   
        img = uploaded_file.getvalue()
        if img:
            st.success("Image Uploaded Successfully")
        return img

def main():
    st.header("Face Detection Model")
    st.write("""Unlock the Faces: Discover the Hidden Expressions with Precision.""")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        inp_img = takeImage() 
    
    
    if inp_img:
        with open("input.jpg","wb") as f:
            f.write(inp_img)
        
        with col2:
            st.write(
                """
                #### Image Entered
                """
            )
            st.image(inp_img)


        image = cv2.imread('./input.jpg')
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        with st.spinner("Processing..."):
            faceCascade = cv2.CascadeClassifier("./data/haarcascade_frontalface_default.xml")
            eye_cascade = cv2.CascadeClassifier("./data/haarcascade_eye_tree_eyeglasses.xml")

            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.075,
                minNeighbors=5,
                minSize=(15, 15)
            )

            for (x,y,w,h) in faces:
                cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = image[y:y+h, x:x+w]
                eyes = eye_cascade.detectMultiScale(roi_gray)
                for (ex,ey,ew,eh) in eyes:
                    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

            for (x, y, w, h) in faces:
                cv2.rectangle(image, (x, y), (x + w, y + h), (0,0,255), 2)

        status = cv2.imwrite('output.jpg', image)
        print("[INFO] Image besiktas2.jpg written to filesystem: ", status)

        st.divider()

        if len(faces) != 0:
            st.write(f"""### Output""")
            st.image('./output.jpg')
            st.write(f"""#### Information:""")
            if len(faces) > 1:
                st.write("Found {0} Faces in the image!".format(len(faces)))
            else:
                st.write("Found {0} Faces in the image!".format(len(faces)))
        else:
            st.write(f"""### Output""")
            st.write(
                f"Couldn't find any face in the image. Please enter any other image."
            )


if __name__ == "__main__":
    main()