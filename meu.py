import streamlit
import streamlit as st
from streamlit_image_select import image_select


st.set_page_config(page_title='SITE MOZ')

#imagem de fundo#
st.title('Aqui encontras os melhores pratos moçambicanos e claro um pouco de tudo.')
st.write('PARA O CANAL DO YOUTUBE [clique aqui](https://youtu.be/nJWdqldYxc8?si=bVHaPRDRk5XYRbjT)')
st.write('Para hoje iremos ver a receita de gulabos ')
st.subheader('...................................GULABOS.................................')
st.write('IGREDIENTES PARA PREPARAÇAO DA MASSA:')

#imagem de gulabos#
with st.container():
    st.write('#7 OVOS')
    st.write('#500 g de manteiga')
    st.write('#1 lata de leite condensado')
    st.write('#1 colher de cha de raspa de limao')
    st.write('#2 colheres de cha de custarde')
    st.write('#2 colheres de royal')
    st.write('#1 pacote de coco ralado')
    st.write('#Trigo ate dar o ponto')
#modo de preparo#
with st.container():
    st.write('---')
    st.write('MODO DE PREPARO')
    st.write('')
