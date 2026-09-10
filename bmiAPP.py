import streamlit as st

st.markdown("# :red[🏃คำนวนดัชนีมวลกาย BMI]")
st.write("กรอกข้อมูลนำ้หนักส่วนสูงของคุณ เพื่อเช็คสุขภาพเบื้องต้น")
weight = st.number_input("กรอกน้ำหนักของคุณ (กิโลกรัม):", min_value=1.0, value=1.0)
hight_cm = st.number_input("กรอกน้ำหนักของคุณ (เซนติเมตร):", min_value=1.0, value=1.0)
if st.buttom("คำนวนค่า BMI📝"):
   hight_m = hight_cm / 100
   bmi = weight / (hight_m**2)

   st.write("---")
   st.header(f"ค่า BMI ของคุณคือ: **{bmi:.2f}**")
   
if bmi < 18.5:
 st.wraning("คุณมีน้ำหนักน้อยกว่าเกณฑ์ (ผอม)") 
elif 18.5 <= bmi < 23.0:
  st.success("คุณมีน้ำหนักอยู่ในเกณฑ์ปกติ (สุขภาพดี)") 
elif 23.0 <= bmi < 25.0:
  st.info("คุณมีน้ำหนักเกินเกณฑ์ (ค่อนข้างท้วม)")
elif bmi > 25.00:
   st.error("คูณอยู่ในเกณฑ์อ้วน ควรระวังเรื่องสุขภาพและออกกำลังกาย")

st.divider()
st.write("นางสาวพันธนันท์ เขตสิทธิ เลขที่ 24 ม.4/11")
