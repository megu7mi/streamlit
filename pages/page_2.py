import streamlit as st
import datetime

with st.form(key='profile_form'):
    name = st.text_input('名前')
    print(name)  #python側ターミナルに表示される
    address = st.text_input('住所')

    #age_category = st.selectbox(
    age_category = st.radio(
        '年齢層',
        ('子ども(18歳未満)', '大人(18歳以上)'))

    hobby = st.multiselect(
        '趣味',
        ('スポーツ', '読書', 'プログラミング', 'アニメ・映画', '釣り', '料理'))

    mail_subscribe = st.checkbox('メールマガジンを購読する')
    height = st.slider('身長', min_value=110, max_value=210)
    start_date = st.date_input(
        '開始日', 
        datetime.date(2022, 7, 1))
    color = st.color_picker('テーマカラー', '#00f900')

    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')
    if submit_btn:
        st.text(f'ようこそ: {name}さん {address}に書籍をおくりました。')
        st.text(f'年齢層: {age_category}')
        st.text(f'趣味: {",".join(hobby)}')
    print(f'submit_btn: {submit_btn}')
    print(f'cancel_btn: {cancel_btn}')
