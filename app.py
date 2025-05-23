import streamlit as st
import boto3
import json
import base64
from PIL import Image
import io

bedrock_runtime = boto3.client(
    service_name='bedrock-runtime',
    region_name='us-west-2'
)

def generate_image(prompt):
    body = {
        "prompt": prompt,
        "mode": "text-to-image",
        "aspect_ratio": "1:1",
        "output_format": "jpeg"
    }

    response = bedrock_runtime.invoke_model(
        modelId="stability.sd3-5-large-v1:0",
        accept="application/json",
        contentType="application/json",
        body=json.dumps(body)
    )

    raw_body = response["body"].read().decode("utf-8")
    response_body = json.loads(raw_body)
    return response_body["images"][0]

def base64_to_pil(base64_string):
    imgdata = base64.b64decode(base64_string)
    return Image.open(io.BytesIO(imgdata))

st.set_page_config(page_title="SD3.5 Image Generator", layout="centered")
st.title("🖼️ Stable Diffusion 3.5 (Bedrock)")

prompt = st.text_input("Introduce tu prompt en inglés:")

if "prompt_log" not in st.session_state:
    st.session_state.prompt_log = []

if st.button("Generar Imagen"):
    with st.spinner("Generando imagen..."):
        try:
            base64_img = generate_image(prompt)
            img = base64_to_pil(base64_img)
            st.image(img, caption="Imagen generada", use_container_width=True)

            buf = io.BytesIO()
            img.save(buf, format="PNG")
            byte_im = buf.getvalue()

            st.download_button(
                label="📥 Descargar imagen",
                data=byte_im,
                file_name="imagen_sd3.png",
                mime="image/png"
            )

            st.session_state.prompt_log.append(prompt)
        except Exception as e:
            st.error(f"Ocurrió un error: {e}")

if st.session_state.prompt_log:
    st.subheader("🕓 Historial de prompts generados")
    for i, p in enumerate(reversed(st.session_state.prompt_log[-5:]), 1):
        st.markdown(f"{i}. *{p}*")
