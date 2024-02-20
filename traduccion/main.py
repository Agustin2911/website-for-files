import streamlit as st
from translator import *


st.set_page_config(page_title="files_translator",page_icon="📁",layout="centered")
#st.image("images/file.png",use_column_width=True,width=400)
st.title("File Translator")
uploaded_file = st.file_uploader("Selecciona un archivo", type=["pdf", "ppt", "pptx","docx"])
opciones = {"español":"es", "english": "en","português":"pt","Deutsch":"de","uارد":"ur","italiano":"it","Français":"fr","日本語":"ja","chinese":"zh-CN","chezch":"cs","korean":"ko"}
opcion_seleccionada = st.selectbox("Selected de language:", list(opciones.keys()))
valor=opciones[opcion_seleccionada]
archivo_terminado="file_traslated.pdf"
archivo_medio="archivo_medio.docx"
archivo_medio2="archivo_medio2.docx"
if st.button("traslate"):
        if uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                read_docx(uploaded_file,archivo_terminado,valor)
                name=archivo_terminado+".docx"
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.presentationml.presentation":
                read_pptx(uploaded_file,archivo_terminado,valor)
                a=(uploaded_file.name).split(".")
                name=archivo_terminado+"."+a[len(a)-1];
        elif uploaded_file.type == "application/pdf":
                temp_file_path = os.path.join(os.getcwd(), "temp_file.pdf")
                with open(temp_file_path, "wb") as temp_file:
                        temp_file.write(uploaded_file.read())
                pdf_word(temp_file_path,archivo_medio)
                read_docx2(archivo_medio,archivo_medio2,valor)
                docx_pdf(archivo_medio2,archivo_terminado)
                name=archivo_terminado+".pdf"
                #fix
        st.download_button(
                label="Download the file",
                data=open(archivo_terminado, 'rb').read(),
                file_name=name,
                key='boton_descarga'
        )
