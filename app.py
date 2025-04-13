import streamlit as st
import pandas as pd
import random

st.title("席替えアプリ")
row = st.number_input("行数", min_value=1, value=5)
col = st.number_input("列数", min_value=1, value=2)

# セッション状態を初期化（固定席を保存するため）
if "fixed_seats" not in st.session_state:
    st.session_state.fixed_seats = {}

# 名前入力欄
st.write("名前を入力してください")
# 空行処理など
names = st.text_area("名前", height=100)
names = names.split("\n")
names = [name for name in names if name.strip() != ""]
st.write("名前の数:", len(names))

# 固定席の説明
st.write("※セルをクリックすると固定席になります。固定席は席替え時に変更されません。")

data = []
clicked = st.button("シャッフル")

# データフレームを作成
if clicked or "df" in st.session_state:
    # 名前をシャッフルして席替え
    if len(names) > row * col:
        st.write("人数が多すぎます")
    else:
        # 前回と行数・列数が変わった場合は固定席をリセット
        if "prev_row" in st.session_state and "prev_col" in st.session_state:
            if st.session_state.prev_row != row or st.session_state.prev_col != col:
                st.session_state.fixed_seats = {}

        # 行数・列数を保存
        st.session_state.prev_row = row
        st.session_state.prev_col = col

        # シャッフル対象の名前リスト（固定席以外）
        available_names = names.copy()
        for pos in st.session_state.fixed_seats.values():
            if pos in available_names:
                available_names.remove(pos)

        random.shuffle(available_names)

        # データフレームを構築
        data = [["" for _ in range(col)] for _ in range(row)]
        name_index = 0

        # 固定席を配置
        for (r, c), name in st.session_state.fixed_seats.items():
            if r < row and c < col and name in names:
                data[r][c] = name

        # 残りの席を配置
        for r in range(row):
            for c in range(col):
                if data[r][c] == "" and name_index < len(available_names):
                    data[r][c] = available_names[name_index]
                    name_index += 1

        # データフレームを作成
        df = pd.DataFrame(data)
        st.session_state.df = df

# データフレームを表示・編集可能にする
if "df" in st.session_state:
    edited_df = st.data_editor(st.session_state.df, disabled=False, key="seat_editor")

    # 編集された値を固定席として記録
    if edited_df is not None and not edited_df.equals(st.session_state.df):
        for r in range(len(edited_df)):
            for c in range(len(edited_df.columns)):
                if edited_df.iloc[r, c] != st.session_state.df.iloc[r, c]:
                    st.session_state.fixed_seats[(r, c)] = edited_df.iloc[r, c]
        st.session_state.df = edited_df

    # 固定席の一覧を表示
    if st.session_state.fixed_seats:
        st.write("固定席:")
        fixed_seats_text = []
        for (r, c), name in st.session_state.fixed_seats.items():
            if r < row and c < col:  # 現在の表示範囲内にあるもののみ表示
                fixed_seats_text.append(f"[{r+1}行{c+1}列] {name}")
        st.write(", ".join(fixed_seats_text))

# 固定席をリセットするボタン
if st.button("固定席をリセット"):
    st.session_state.fixed_seats = {}
    st.rerun()
