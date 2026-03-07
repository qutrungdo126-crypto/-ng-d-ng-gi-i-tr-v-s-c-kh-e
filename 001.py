import streamlit as st
import random
import time
from sklearn.linear_model import LinearRegression
import feedparser

st.sidebar.title("🎶 Danh sách nghệ sĩ")
selected_artist = st.sidebar.radio("Chọn nghệ sĩ:", ["Đen Vâu", "Hà Anh Tuấn", "Sơn Tùng M-TP", "Những bản nhạc giúp tâm trạng vui vẻ hơn"])

videos = {
    "Đen Vâu": [
        ("Nấu ăn cho em", "https://www.youtube.com/watch?v=ukHK1GVyr0I"),
        ("Mang tiền về cho mẹ", "https://www.youtube.com/watch?v=UVbv-PJXm14"),
        ("Trời hôm nay nhiều mây cực!", "https://www.youtube.com/watch?v=MBaF0l-PcRY"),
        ("Hai triệu năm", "https://www.youtube.com/watch?v=LSMDNL4n0kM")
    ],
    "Hà Anh Tuấn": [
        ("Tuyết rơi mùa hè", "https://www.youtube.com/watch?v=pTh3KCD7Euc"),
        ("Nước ngoài", "https://www.youtube.com/watch?v=pU3O9Lnp-Z0"),
        ("Tháng tư là lời nói dối của em", "https://www.youtube.com/watch?v=UCXao7aTDQM"),
        ("Xuân thì", "https://www.youtube.com/watch?v=3s1r_g_jXNs")
    ],
    "Sơn Tùng M-TP": [
        ("Lạc trôi", "https://www.youtube.com/watch?v=Llw9Q6akRo4"),
        ("Chúng ta không thuộc về nhau", "https://www.youtube.com/watch?v=qGRU3sRbaYw"),
        ("Muộn rồi mà sao còn", "https://www.youtube.com/watch?v=xypzmu5mMPY"),
        ("Hãy trao cho anh", "https://www.youtube.com/watch?v=knW7-x7Y7RE")
    ],
    "Những bản nhạc giúp tâm trạng vui vẻ hơn":[
        ("Những bản nhạc giúp tâm trạng vui vẻ hơn", "https://www.youtube.com/watch?v=SlsH6PbDJZk&t=898s"),
        ("Lỡ Duyên", "https://www.youtube.com/watch?v=fq_H4A3HgD4&list=RDfq_H4A3HgD4&start_radio=1&rv=fq_H4A3HgD4"),
        ("Bài hát về tình yêu quê hương đất nước", "https://www.youtube.com/watch?v=GOMGeUetqlI&list=RDSlsH6PbDJZk&index=3"),
        ("Đi giữa trời rực rỡ", "https://www.youtube.com/watch?v=D1Uf9vREh6Q&list=RDSlsH6PbDJZk&index=3"),
        ("STAY HOME, STAY HAPPY, STAY HÀANHTUẤN", "https://www.youtube.com/watch?v=MMgPOQ9gJhM&list=RDEMrx5Xy48sg-WCr9qiaw1hhg&index=2"),
        ("Focus Time", "https://www.youtube.com/watch?v=Lcmlq9utGYk")
    ]
}

st.title("🎧 Ứng dụng giải trí và sức khỏe")

tab1, tab2, tab3, tab4,tab5 = st.tabs(["🎤 MV yêu thích", "📰 Đọc báo", "📄Kiểm tra sức khỏe","🔘Trình độ học sinh theo điểm","🎮Game"])

with tab1:
    st.header(f"Các bài hát của {selected_artist} 🎵")
    for title, url in videos[selected_artist]:
        st.subheader(title)
        st.video(url)
with tab2:
    st.header("📰 Tin tức mới nhất ")
    tabA, tabB, tabC = st.tabs(["💥 Tin tức mới nhất từ VnExpress", "💰Cập nhật giá vàng", "🦾Báo Thể Thao" ])
    with tabA:
        st.header("📰 Tin tức mới nhất từ VnExpress")
        feed = feedparser.parse("https://vnexpress.net/rss/tin-moi-nhat.rss")
        for entry in feed.entries[:5]:
            st.subheader(entry.title)
            st.write(entry.published)
            st.write(entry.link)
    with tabB:
        st.header("💰 Cập nhật giá vàng từ Vietnamnet")

        feed = feedparser.parse("https://vietnamnet.vn/rss/kinh-doanh.rss")
        gold_news = [entry for entry in feed.entries if "vàng" in entry.title.lower() or "giá vàng" in entry.summary.lower()]

        if gold_news:
            for entry in gold_news[:5]:  # Hiện 5 bài gần nhất
                st.subheader(entry.title)
                st.write(entry.published)
                st.write(entry.link)
        else:
            st.warning("💔Không tìm thấy bản tin giá vàng gần đây.") 
    with tabC:
        st.header("🔲The latest news from VnExpress")
        feed = feedparser.parse("https://vietnamnet.vn/rss/the-thao.rss")
        for entry in feed.entries[:10]:
            st.subheader(entry.title)
            st.write(entry.published)
            st.write(entry.link)
with tab3:
    st.header("😁Sức Khỏe")
    tabC, tabD, tabE, tabF, tabG = st.tabs(["📊Tính chỉ số BMI", "💦Khuyến nghị lượng nước uống mỗi ngày", "👟Kiểm tra số bước đi phù hợp mỗi ngày", "🕐Dự đoán giờ ngủ","💤Kiểm tra giờ đi ngủ theo tuổi"])
    with tabC:
        st.header("📊Kiểm tra chỉ số BMI")
        can_nang = st.number_input("Nhập cân nặng của bạn (kg)", min_value=10.0, max_value = 200.0, step=0.1)
        chieu_cao = st.number_input("Nhập cân chiều cao của bạn (m)", min_value=1.0, max_value = 2.5, step=0.1)
        Bmi_min = 18.5
        Bmi_max = 24.9
        can_nang_min = Bmi_min * (chieu_cao** 2)
        can_nang_max = Bmi_max * (chieu_cao** 2)
        giam_can = can_nang - can_nang_max
        tang_can = can_nang_min - can_nang
        if st.button("📏 Tính BMI"):
            if chieu_cao > 0:
                bmi = can_nang / (chieu_cao ** 2)
                st.success(f"Chỉ số BMI của bạn là: {bmi:.2f}")

                if bmi < 18.5:
                    st.warning("Bạn đang thiếu cân, nên ăn uống đầy đủ và dinh dưỡng hơn.")
                    st.warning("Bạn nên tăng :  ")
                    st.warning( f"{tang_can :2f} kg")
                elif 18.5 <= bmi < 25:
                    st.info("Bạn có cân nặng bình thường. Hãy tiếp tục duy trì lối sống lành mạnh.")
                elif 25 <= bmi < 30:
                    st.warning("Bạn đang thừa cân. Nên cân đối chế độ ăn và tập thể dục.")
                    st.warning("Bạn nên giảm :  ")
                    st.warning( f"{giam_can :2f} kg")
                else:
                    st.error("Bạn đang béo phì. Nên gặp chuyên gia dinh dưỡng hoặc bác sĩ để được tư vấn.")
                    st.warning("Bạn nên giảm :  ")
                    st.warning( f"{giam_can :2f} kg")
    with tabD: 
            st.title("💦Khuyến nghị lượng nước uống mỗi ngày")
            tuoi = st.number_input("Nhập tuổi của bạn:", min_value=1, max_value=100, value = 18, step=1)
            if st.button("🧾 Kiểm tra lượng nước cần uống"):
                if tuoi < 4:
                    st.info("Khuyến nghị: 1.3 lít/ngày")
                elif 4 <= tuoi <= 8:
                    st.info("Khuyến nghị: 1.7 lít/ngày")
                elif 9 <= tuoi <= 13:
                    st.info("Khuyến nghị: 2.1 đến 2.4 lít/ngày")
                elif 14 <= tuoi <= 18:
                    st.info("Khuyến nghị: 2.3 đến 3.3 lít/ngày")
                elif 19 <= tuoi <= 50:
                    st.info("Khuyến nghị: 2.7 lít/ngày đối với nữ, 3.7 lít/ngày đối với nam")
                elif tuoi > 50:
                    st.info("Khuyến nghị: khoảng 2.5 đến 3.0 lít/ngày (phụ thuộc vào sức khỏe và mức độ vận động)")
                else:
                    st.warning("Vui lòng nhập độ tuổi hợp lệ.")
    with tabE:
        st.title("👟Kiểm tra số bước đi phù hợp mỗi ngày")
        age2 = st.number_input("Nhập tuổi của bạn: ", min_value=0, max_value=100, value = 30, step=1)
        if st.button("Kiểm tra số bước"):
            st.success(f"Tuổi của bạn: {age2:.0f}")
            if age2 < 18:
                st.info("🔹 Bạn nên đi **12.000-15.000 bước** mỗi ngày.")
            elif 17 < age2 <= 39:
                st.info("🔹 Bạn nên đi **8.000-10.000 bước** mỗi ngày.")
            elif 39 < age2 <= 64:
                st.warning("🔸 Bạn nên đi **7.000-9.000 bước** mỗi ngày.")
            elif age2 > 64:
                st.warning("🔸 Bạn nên đi **6.000-8.000 bước** mỗi ngày.")
            else:
                st.error("⚠️ Có lỗi xảy ra. Vui lòng kiểm tra lại thông tin.")
    with tabF:
        st.header("🔮 Dự đoán giờ ngủ mỗi đêm")
        #Tuoi, mức độ hoạt động thể chất, thời gian dùng máy tính 
        x = [[10, 1, 8], [20, 5, 6], [25, 8, 3], [30, 6, 5], [35, 2, 9], [40, 4, 3]]
        y = [10, 8, 6, 7, 9.5, 9]
        model = LinearRegression()
        model.fit(x, y)
        st.write("Nhập thông tin cá nhân: ")
        age = st.number_input("Tuổi của bạn", min_value= 5, max_value=100, value=25)
        activity = st.slider("Số giờ hoạt động thể chất (1 = ít, 10 = rất nhiều)", 1, 10, 5)
        screen_time = st.number_input("Thời gian dùng màn hình trong 1 ngày (giờ)", min_value=0, max_value=24, value=6)

        if st.button("Dự đoán ngay "):
            input_data = [[age, activity, screen_time]]
            result = model.predict(input_data)[0]
            st.success(f"Bạn nên ngủ khoảng {result:.1f} giờ mỗi đêm")

            if result < 6.5:
                st.warning("có thể bạn cần nghỉ ngơi nhiều hơn để cải thiện sức khỏe. ")
            elif result > 9:
                st.info("có thể bạn đang vận động nhiều, bạn cần ngủ bù hợp lý nhé ")
            else:
                st.success("Lượng ngủ lý tưởng, hãy giữ thói quen tốt ")
    with tabG:
        st.title('💤Kiểm tra thời gian ngủ mỗi ngày')
        tabX, tabY = st.tabs(['Trẻ sơ sinh/Mới tập đi', 'Trẻ nhỏ/Người lớn'])

        with tabX:
            thang = st.number_input('Nhập số tháng tuổi: ', min_value=0, max_value=12, value=1, step=1)
            if st.button('📅Tính thời gian cần ngủ theo tháng tuổi'):
                if thang < 4:
                    st.info('Cần ngủ 14 - 17 tiếng mỗi ngày')
                else:
                    st.info('Cần ngủ 12 - 15 tiếng mỗi ngày')

        with tabY:
            tuoi = st.number_input('Nhập độ tuổi của bạn: ', min_value=0, max_value=100, value=18, step=1)
            if st.button('📆Tính thời gian cần ngủ'):
                if tuoi < 3:
                    st.info('Cần ngủ 11 - 14 tiếng mỗi ngày')
                elif tuoi < 6:
                    st.info('Cần ngủ 10 - 13 tiếng mỗi ngày')
                elif tuoi < 14:
                    st.info('Cần ngủ 9 - 11 tiếng mỗi ngày')
                elif tuoi < 18:
                    st.info('Cần ngủ 8 - 10 tiếng mỗi ngày')
                elif tuoi < 65:
                    st.info('Cần ngủ 7 - 9 tiếng mỗi ngày')
                else:
                    st.info('Cần ngủ 7 - 8 tiếng mỗi ngày')
    
with tab4:
    st.title("🔘Trình độ học sinh theo điểm số")
    score = st.number_input("Nhập điểm gần đây của bạn vào(trên 100 điểm):  ", min_value=0, max_value=100, value = 50, step=1)
    if score >= 90:
        st.info ("💖Bạn đang làm rất tốt, tiếp tục phát huy")
        st.info ("Giữ sự tập trung vào các lĩnh vực chủ đề mới nhé.")
    elif score >=51 and score <=89:
        st.info ("🌹Bạn đang làm việc ở cấp độ khá tốt")
        st.info ("Nhưng bạn nên cố gắng hơn để đạt điểm tốt hơn")
    elif score >=20 and score <=50:
        st.info ("🥀Bạn đang ở cấp độ trung bình - kém")
        st.info ("một số bài tập thêm có thể giúp bạn nâng cao thành tích")
    else:
        st.info ("💔Bạn đã trượt môn")
        st.info (" bạn nên học thêm 1 kèm 1 cấp tốc.")
with tab5:
    tabA, tabB, tabC, TabD, TaBE = st.tabs(["🎮 Game đoán số", "🎮 Game tung xúc sắc","🥊Kéo - Búa - Bao","🧩 Game Đuổi hình bắt chữ", "🎲 Quay Số May Mắn"])
    with st.sidebar:
        st.video("https://dn720301.ca.archive.org/0/items/rpreplay-final-1680875953/RPReplay_Final1680875953.mp4", autoplay=True, muted=True)
    with tabA:
        st.header("🎯 Game đoán số bí mật từ 1 - 100")
        st.image("https://m.media-amazon.com/images/I/71Agu95C-jL._AC_UF894,1000_QL80_.jpg")
        if "secret" not in st.session_state:
            st.session_state.secret = random.randint(1, 100)
            st.session_state.tries = 0

        guess = st.number_input("Nhập số dự đoán 1 - 100",min_value=1,max_value=100,step=1)
        if st.button("Đoán !!!!!"):
            st.session_state.tries += 1
            if guess < st.session_state.secret:
                st.warning("😀 Số bí mật lớn hơn ")
                st.image("https://i.kym-cdn.com/editorials/icons/original/000/013/755/mon.jpg")
            elif guess > st.session_state.secret:
                st.warning("😀 Số bí mật nhỏ hơn ")
                st.image("https://i.kym-cdn.com/editorials/icons/original/000/013/755/mon.jpg")
            else:
                st.success(f"🏆 chính xác ! Bạn đoán đúng sau {st.session_state.tries} lần. ")
                st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR2pBfdCwgvKb7E8RBYkSluf3u3EdNxv54GuQ&s")
        if st.button("🎮Chơi lại"):
                st.session_state.secret = random.randint(1, 100)
                st.session_state.tries = 0
    with tabB:
        st.header("🎮 Game tung xúc sắc")
        st.image("https://gilkalai.wordpress.com/wp-content/uploads/2017/09/dice.png")
        st.write("Luật chơi")
        st.write("Bạn lắc xúc sắc 1 cách random")
        if st.button("Tung xúc sắc🎲"):
            roll = random.randint(1, 6)
            img_placeholder = st.empty()
            img_placeholder.image("https://downloadwap.com/thumbs3/screensavers/d/new/misc/dice-169064.gif")
            time.sleep(5)
            img_placeholder.empty()
            st.success(f"Bạn đã tung được số {roll} !!!!")
            if roll == 1:
                st.image("http://www.clker.com/cliparts/m/v/m/J/4/V/dice-1-md.png")
            if roll == 2:
                st.image("https://www.clker.com/cliparts/a/Y/E/o/z/t/dice-2-md.png")
            if roll == 3:
                st.image("https://www.clker.com/cliparts/O/I/r/9/W/x/dice-3-md.png")
            if roll == 4:
                st.image("https://www.clker.com/cliparts/r/z/d/a/L/V/dice-4-md.png")
            if roll == 5:
                st.image("https://www.clker.com/cliparts/U/N/J/F/T/x/dice-5-md.png ")
            if roll == 6:
                st.image("https://www.clker.com/cliparts/l/6/4/3/K/H/dice-6-md.png")
    with tabC:
        st.header("Kéo - Búa - Bao")
        st.image("https://static.tvtropes.org/trope_videos_transcoded/images/sd/q7uwxt.jpg")
        st.write("Luật chơi")
        st.write("Bạn nút để ra một trong kéo, búa hoặc bao. Hãy cố gắng thắng con bot nha! ")
        st.write("Kéo thắng bao")
        st.write("Búa thắng kéo")
        st.write("Bao thắng búa")
        user = st.selectbox("Bạn chọn: ", ["Kéo", "Búa", "Bao"])
        bot = random.choice(["Kéo", "Búa", "Bao"])
        if st.button("Ra tay nào!!!"):
            st.write(f"Bot chọn: {bot}")
            if user == bot:
                st.warning("Hòa !!!")
                st.image("https://i1.sndcdn.com/artworks-ecyyzfetWzmHLDpo-X7ICfQ-t500x500.jpg")
            elif (user == "Kéo" and bot == "Bao") or (user == "Bao" and bot == "Búa") or (user == "Búa" and bot == "Kéo"):
                st.success("Bạn thắng")
                st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR1MBsQ9GnV0RNq9b_rJA63UN8m4e0Xq6HpGQ&s")
            else:
                st.error("Bạn thua")
                st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTGlF-k_0Gsm39dJSSZCSEJUF-UsSkm_SAkHg&s")
    with TabD:
        st.header("🧩 Game Đuổi hình bắt chữ")

        puzzles = [
        {
                "image": "https://cdn.lazi.vn/storage/uploads/dhbc/1469120972_tra-hoi.jpg",
                "answer": "tra hỏi"
        },
        {
                "image": "https://cdn.lazi.vn/storage/uploads/dhbc/1469120797_khoa-so.jpg",
                "answer": "khóa sổ"
        },
        {
                "image": "https://cdn.lazi.vn/storage/uploads/dhbc/1469120784_kien-truc-su.jpg",
                "answer": "kiến trúc sư"
        },
        {
                "image": "https://cdn.lazi.vn/storage/uploads/dhbc/1468933376_thong-so.jpg",
                "answer": "thông số"
        },
        {
            "image": "https://cdn.lazi.vn/storage/uploads/dhbc/1468933376_thong-so.jpg",
            "answer": "thông số"
        },
        {
            "image": "https://cdn.lazi.vn/storage/uploads/dhbc/1468932212_thua-tuong.jpg",
            "answer": "thua tướng"
        },
        {
            "image": "https://cdn.lazi.vn/storage/uploads/dhbc/1468933353_nhac-thinh-phong.jpg",
            "answer": "nhạc thính phòng"
        },
        {
            "image": "https://cdn.lazi.vn/storage/uploads/dhbc/1468933365_sau-sac.jpg",
            "answer": "sâu sắc"
        },
        {
            "image": "https://cdn.lazi.vn/storage/uploads/dhbc/1468933365_sau-sac.jpg",
            "answer": "sâu sắc"
        }]
        if "dhbc_index" not in st.session_state:
           if "dhbc_index" not in st.session_state:
            st.session_state.score = 0
            st.session_state.dhbc_index = random.randint(0, len(puzzles) - 1)
            st.session_state.start_time = time.time()
            st.session_state.duration = 45
            st.session_state.finished = False
            st.session_state.result = ""

        score_box = st.empty()
        score_box.info(f"Điểm của bạn: {st.session_state.score}")

        puzzle = puzzles[st.session_state.dhbc_index]

        # ==== Hiển thị hình ====
        st.image(puzzle["image"], width=300)
        # ==== Đếm giờ ====
        elapsed = int(time.time() - st.session_state.start_time)
        remaining = st.session_state.duration - elapsed

        if remaining > 0 and not st.session_state.finished:
            st.warning(f"⏳ Còn lại: {remaining} giây")
        else:
            st.session_state.finished = True
            st.error("⏰ Hết giờ!")
        # ==== Nhập đáp án ====
        guess = st.text_input("Nhập đáp án:", disabled=st.session_state.finished)

        # ==== Nút kiểm tra ====
        if st.button("Kiểm tra") and not st.session_state.finished:
            if guess.lower().strip() == puzzle["answer"].lower():
                st.session_state.result = "correct"
                st.session_state.finished = True
                st.session_state.score += 10
            else:
                st.session_state.result = "wrong"
                st.session_state.score -= 2
        # ==== Hiển thị kết quả ====
        if st.session_state.result == "correct":
            st.success("🎉 Chính xác!")
            st.balloons()
        elif st.session_state.result == "wrong":
            st.error("❌ Sai rồi, thử lại!")

        # ==== Nêu hết giờ ====
        if st.session_state.finished and remaining <= 0:
            st.info(f"Đáp án đúng là: **{puzzle['answer']}**")

        # ==== Nút vòng mới ====
        if st.button("🔄 Vòng mới"):
            st.session_state.dhbc_index = random.randint(0, len(puzzles)-1)
            st.session_state.start_time = time.time()
            st.session_state.finished = False
            st.session_state.result = ""
            st.rerun()
    with TaBE:
        st.title("🎲 Quay Số May Mắn")
        # Khởi tạo dữ liệu
        if "prizes" not in st.session_state:
            st.session_state.new_prizes = []
        if "weights" not in st.session_state:
            st.session_state.weights = []

        # =========================
        # THÊM PHẦN THƯỞNG
        # =========================
        st.subheader("➕ Thêm phần thưởng")

        col1, col2 = st.columns(2)
        with col1:
            new_prize = st.text_input("Tên phần thưởng")
        with col2:
            weight = st.number_input("Tỷ lệ trúng (%)", 1, 100, 10)

        if st.button("Thêm"):
            if new_prize:
                st.session_state.new_prizes.append(new_prize)
                st.session_state.weights.append(weight)
                st.success(f"Đã thêm: {new_prize}")
        # =============================
        # DANH SÁCH PHẦN THƯỞNG
        # =============================
        st.subheader("🎁 Danh sách phần thưởng")
        if st.session_state.new_prizes:
            for i, prize in enumerate(st.session_state.new_prizes):
                st.write(
                    f"{i+1}. {prize} | 🎯 Tỷ lệ: {st.session_state.weights[i]}%"
                )
        else:
            st.info("Chưa có phần thưởng")

        # =========================
        # VÒNG QUAY
        # =========================
        st.subheader("🎡 Quay số")

        if st.button("QUAY NGAY 🎯"):
            if st.session_state.new_prizes:
                spin_placeholder = st.empty()
                # Animation quay
                for i in range(15):
                    spin_placeholder.markdown(
                        f"### 🎲 Đang quay... {random.choice(st.session_state.new_prizes)}"
                    )
                    time.sleep(0.1)
                # Chọn kết quả theo tỷ lệ
                result = random.choices(
                    st.session_state.new_prizes,
                    weights = st.session_state.weights,
                    k=1
                )[0]
                spin_placeholder.empty()
                st.balloons()
                st.success(f"Chúc mừng bạn đã trúng {result}")
            else:
                st.warning("⚠ Chưa có phần thưởng")
