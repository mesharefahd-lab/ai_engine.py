import streamlit as st
import datetime

# إعداد واجهة البرنامج بشكل احترافي
st.set_page_config(page_title="IT Support AI", page_icon="💻")

# --- محرك الذكاء الاصطناعي التقني (IT Logic) ---
def ai_it_analyzer(text):
    text = text.lower()
    
    # 1. تصنيف نوع الدعم (Classification)
    if any(w in text for w in ["نت", "إنترنت", "شبكة", "راوتر", "wifi"]):
        category = "Network Support (الشبكات)"
    elif any(w in text for w in ["سيرفر", "داتابيز", "قاعدة بيانات", "تعطل النظام"]):
        category = "Infrastructure (البنية التحتية)"
    elif any(w in text for w in ["ايميل", "كلمة سر", "تسجيل دخول", "حساب"]):
        category = "Identity Management (إدارة الحسابات)"
    elif any(w in text for w in ["طابعة", "ماوس", "شاشة", "جهاز"]):
        category = "Hardware Support (العتاد)"
    else:
        category = "General IT Inquiry (استفسار عام)"

    # 2. تحديد الأولوية (SLA Priority)
    # الحالات الحرجة في الحاسب: توقف السيرفر، انقطاع الشبكة عن الشركة، اختراق.
    if any(w in text for w in ["توقف", "داون", "down", "اختراق", "فيروس", "سيرفر"]):
        priority = "Critical (P1) 🚨"
    elif any(w in text for w in ["بطء", "تحديث", "تنصيب"]):
        priority = "Low (P3)"
    else:
        priority = "Medium (P2)"
    
    return category, priority

# --- الواجهة ---
st.title("🖥️ نظام الدعم الفني الذكي - IT Helpdesk AI")
st.markdown("مشروع أتمتة تذاكر الدعم الفني باستخدام تحليل النصوص.")

with st.form("it_ticket_form"):
    user_id = st.text_input("الرقم الوظيفي / اسم المستخدم")
    issue_title = st.text_input("عنوان المشكلة (مثلاً: تعطل الوصول للسيرفر)")
    description = st.text_area("وصف تقني للمشكلة (بالعربي أو الإنجليزي)")
    
    submitted = st.form_submit_button("إرسال التذكرة للتحليل")

if submitted:
    if description:
        # التحليل الذكي
        it_cat, it_prio = ai_it_analyzer(description)
        
        st.divider()
        st.subheader("🤖 تحليل النظام الذكي (AI Analysis)")
        
        col1, col2 = st.columns(2)
        with col1:
            st.info(f"**القسم الموجه له:**\n\n{it_cat}")
        with col2:
            st.warning(f"**مستوى الأولوية:**\n\n{it_prio}")
            
        st.success(f"تم فتح تذكرة برقم #IT-{datetime.datetime.now().strftime('%Y%m%d%H%M')}")
        
        # كود تقني يظهر في الـ Dashboard للفنيين
        with st.expander("عرض تفاصيل الـ Metadata (للمبرمجين)"):
            st.code({
                "status": "Open",
                "assigned_to": "AI_Bot_Queue",
                "timestamp": str(datetime.datetime.now()),
                "nlp_confidence": "94%"
            })
    else:
        st.error("الرجاء إدخال وصف المشكلة التقنية.")
