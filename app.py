#メインファイルから環境変数の読み込み
from dotenv import load_dotenv

load_dotenv()

# 各種ライブラリの読み込み
import streamlit as st
#from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# 環境変数の読み込み
#load_dotenv()

def get_llm_response(user_message, selected_theme):
    """
    LLMからの回答を取得する処理
    """
    # モデルのオブジェクトを用意
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.5)

    # 選択テーマに応じて使用するプロンプトのシステムメッセージを分岐
    if selected_theme == theme_1:
        system_message = """
            あなたはプレミアリーグの各チーム戦力把握の専門家です。各チームの所属選手とスタッツやパフォーマンス、怪我人の状況情報、出場停止選手情報、マネージャーやコーチ陣の戦術志向や戦術浸透度、チームの財政状況等の豊富な知識を持っています。ユーザーの質問には、数値的指標を根拠に基づいた適切なアドバイスを提供
            してください。

            あなたの役割は、テレビショウに出演する解説者として、最新のチーム状況と今後の対戦日程から勝敗予想してリバプールFCの最終順位を予想して下さい。

            回答には、できるだけ具体的な説明を加え、優勝確率をパーセンテージで示してください。
        """
    else:
        system_message = """
            あなたは世界中のチームの所属選手の特徴を把握する専門家です。リバプールFCの怪我人有無による選手層やチーム戦術透度、チームの財政状況等の豊富な知識を持っています。
            
            あなたの役割は、リバプールFCの最新スタッツから優勝確率を上げるために有益な補強選手候補を提案し、選手の特徴と獲得することにより期待される役割をわかりやすく説明することです。
            ユーザーの質問には、数値的指標を根拠に基づいた適切なアドバイスを提供してください。

            回答には、具体的な選手名や獲得の可能性について言及してください。



        """
    
    # メッセージリストの用意
    messages = [
        SystemMessage(content=system_message),
        HumanMessage(content=user_message)
    ]
    # LLMからの回答取得
    response = llm(messages)

    return response.content


# 案内文の表示
st.title("LIVERPOOL FCの25～26シーズンプレミアリーグ優勝確率予想・優勝に向けた補強選手候補のチャット相談アプリ")
st.write("LIVERPOOL FCの25～26シーズンプレミアリーグ優勝確率予想・優勝に向けた補強選手候補に関する生成AIチャット相談アプリです。以下の選択肢から相談したいテーマを選択の上、チャット欄から相談内容を送信すると、専門家AIが的確な回答を行ってくれます。")

# テーマの選択肢を用意
theme_1 = "優勝確率予想"
theme_2 = "補強選手候補"

# 相談テーマ選択用のラジオボタン
selected_theme = st.radio(
    "【テーマ】",
    [theme_1, theme_2]
)

# 区切り線
st.divider()

# チャット欄
user_message = st.text_input(label="相談内容を入力してください")

# ボタン
if st.button("送信"):
    # 区切り線
    st.divider()
    # LLMからの回答取得
    response = get_llm_response(user_message, selected_theme)
    # LLMからの回答表示
    st.write(response)