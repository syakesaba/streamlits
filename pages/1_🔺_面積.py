import json
import math

import streamlit as st
from geopy.distance import geodesic

st.set_page_config(page_title="1_🔺_面積出すやつ", page_icon="🔺")
st.sidebar.markdown("🔺の面積出すやつ")

st.markdown("# 3点の座標を含むdraw dataをjsonで入力してください")
sample = '[{"type":"polyline","latLngs":[{"lat":34.688321,"lng":135.519201},{"lat":34.704693,"lng":135.527484}],"color":"#a24ac3"},{"type":"polyline","latLngs":[{"lat":34.688321,"lng":135.519201},{"lat":34.702246,"lng":135.506086}],"color":"#a24ac3"},{"type":"polyline","latLngs":[{"lat":34.704693,"lng":135.527484},{"lat":34.702246,"lng":135.506086}],"color":"#a24ac3"},{"type":"circle","latLng":{"lat":34.6984145094219,"lng":135.51767823792733},"radius":1139.748138135289,"color":"#a24ac3"}]'
json_ = st.text_input(label="draw data", help=sample)
try:
    draws = json.loads(json_)
except ValueError as e:
    st.warning(icon="⚠️", body="有効なjsonデータではありません。")
    st.stop()
try:
    polylines = [draw["latLngs"] for draw in draws if draw["type"] == "polyline"]
    if len(polylines) != 3:
        raise ValueError("draw dataに有効な3つのpolylineが含まれておりません")
    distances = []
    for polyline in polylines:
        if len(polyline) != 2:
            raise ValueError("draw dataのpolylineが不正です")
        point1 = (polyline[0]["lat"], polyline[0]["lng"])
        point2 = (polyline[1]["lat"], polyline[1]["lng"])
        distance = geodesic(point1, point2).kilometers
        distances.append(distance)
    if len(set(distances)) == 1:
        st.write(f"一辺が{distances[0]}キロメートルの正三角形です！")
    else:
        st.write("***正三角形ではありません***")
        st.write(f"辺1: {distances[0]}キロメートル")
        st.write(f"辺2: {distances[1]}キロメートル")
        st.write(f"辺3: {distances[2]}キロメートル")
        p = sum(distances) / 2
        S = math.sqrt(p * (p - distances[0]) * (p - distances[1]) * (p - distances[2]))
        st.write(f"周長: {sum(distances)}キロメートル")
        st.write(f"面積: {S}平方キロメートル")
        t = sum(distances) / len(distances)
        tp = sum(distances) / 2
        St = math.sqrt(tp * (tp - t) * (tp - t) * (tp - t))
        st.write(f"正三角形の場合の面積: {St}平方キロメートル")
        st.write(f"想定スコア: {(S/St)*100}%")
except ValueError as e:
    st.warning(icon="⚠️", body=str(e))
except Exception as e:
    st.warning(icon="⚠️", body=str(e.with_traceback()))
