import streamlit as st
from streamlit_extras.stylable_container import stylable_container as sc
from streamlit_extras.tags import tagger_component
from utils.utils import read_json

st.set_page_config(
    page_title='My Projects',
    layout='wide',
    initial_sidebar_state="expanded"
)
st.title('My projects')

projects = read_json('projects.json')


for idx, p in enumerate(projects):
    with st.container(border=True):
        
        text_col, image_col = st.columns(2, gap='large', vertical_alignment='center')

        with text_col:
            st.markdown(f"# {p['name']}")
            tagger_component(
                content='',
                tags=p['tags']
            )
            st.markdown(p['description'])
            st.link_button(p['button_label'], url=p['url'])

        with image_col:
            media = p['media']
            if media['type'] == 'image':
                st.image(media['path'])
            else:
                st.video(media['path'], loop=True, autoplay=True)

        