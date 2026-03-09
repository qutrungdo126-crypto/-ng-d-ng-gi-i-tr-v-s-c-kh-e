import streamlit as st
import random
import time
from sklearn.linear_model import LinearRegression
import feedparser

st.sidebar.title("🎶 Danh sách nghệ sĩ")
selected_artist = st.sidebar.radio(
    "Chọn nghệ sĩ:",
    ["Low G","Đen Vâu", "Sơn Tùng M-TP", "Những bản nhạc giúp tâm trạng vui vẻ hơn"]
)

# ================= SPOTIFY EMBEDS =================

spotify_embeds = {

    "Low G": """
    <iframe style="border-radius:12px"
    src="https://open.spotify.com/embed/artist/6TITnFVRcl0AcZ4syE7Toe"
    width="100%" height="352" frameborder="0"
    allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture">
    </iframe>
    """,

    "Đen Vâu": """
    <iframe style="border-radius:12px"
    src="https://open.spotify.com/embed/artist/1LEtM3AleYg1xabW6CRkpi"
    width="100%" height="352" frameborder="0"
    allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture">
    </iframe>
    """,

    "Sơn Tùng M-TP": """
    <iframe style="border-radius:12px"
    src="https://open.spotify.com/embed/artist/5dfZ5uSmzR7VQK0udbAVpf"
    width="100%" height="352" frameborder="0"
    allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture">
    </iframe>
    """
}

# ================= YOUTUBE VIDEOS =================

videos = {

    "Những bản nhạc giúp tâm trạng vui vẻ hơn":[
        ("Playlist vui vẻ", "https://www.youtube.com/watch?v=SlsH6PbDJZk"),
        ("Lỡ Duyên", "https://www.youtube.com/watch?v=fq_H4A3HgD4"),
        ("Nhạc quê hương", "https://www.youtube.com/watch?v=GOMGeUetqlI"),
        ("Đi giữa trời rực rỡ", "https://www.youtube.com/watch?v=D1Uf9vREh6Q"),
        ("Stay Happy", "https://www.youtube.com/watch?v=MMgPOQ9gJhM"),
        ("Focus Time", "https://www.youtube.com/watch?v=Lcmlq9utGYk")
    ]
}

# ================= MAIN TITLE =================

st.title("🎧 Ứng dụng giải trí và sức khỏe")

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🎤 MV yêu thích",
    "📰 Đọc báo",
    "📄Kiểm tra sức khỏe",
    "🔘Trình độ học sinh theo điểm",
    "🎮Game"
])

# ================= MUSIC TAB =================

with tab1:

    st.header(f"Các bài hát của {selected_artist} 🎵")

    if selected_artist in spotify_embeds:
        st.markdown(spotify_embeds[selected_artist], unsafe_allow_html=True)

    elif selected_artist in videos:
        for title, url in videos[selected_artist]:
            st.subheader(title)
            st.video(url)

# ================= NEWS TAB =================

with tab2:

    st.header("📰 Tin tức")

    tabA, tabB, tabC = st.tabs([
        "💥 VnExpress",
        "💰 Giá vàng",
        "⚽ Thể thao"
    ])

    with tabA:

        feed = feedparser.parse("https://vnexpress.net/rss/tin-moi-nhat.rss")

        for entry in feed.entries[:5]:

            st.subheader(entry.title)
            st.write(entry.published)
            st.write(entry.link)

    with tabB:

        feed = feedparser.parse("https://vietnamnet.vn/rss/kinh-doanh.rss")

        gold_news = [
            entry for entry in feed.entries
            if "vàng" in entry.title.lower()
        ]

        if gold_news:
            for entry in gold_news[:5]:

                st.subheader(entry.title)
                st.write(entry.published)
                st.write(entry.link)

        else:

            st.warning("Không tìm thấy tin giá vàng")

    with tabC:

        feed = feedparser.parse("https://vietnamnet.vn/rss/the-thao.rss")

        for entry in feed.entries[:10]:

            st.subheader(entry.title)
            st.write(entry.published)
            st.write(entry.link)

# ================= HEALTH TAB =================

with tab3:

    st.header("😁 Sức khỏe")

    tabC, tabD, tabE, tabF = st.tabs([
        "BMI",
        "Uống nước",
        "Số bước",
        "Dự đoán giờ ngủ"
    ])

    with tabC:

        weight = st.number_input("Cân nặng (kg)", 10.0, 200.0)
        height = st.number_input("Chiều cao (m)", 1.0, 2.5)

        if st.button("Tính BMI"):

            bmi = weight / (height**2)
            st.success(f"BMI của bạn: {bmi:.2f}")

    with tabD:

        age = st.number_input("Tuổi", 1, 100)

        if st.button("Khuyến nghị"):

            if age < 18:
                st.info("2 - 2.5 lít/ngày")
            else:
                st.info("2.5 - 3.7 lít/ngày")

    with tabE:

        age2 = st.number_input("Tuổi của bạn", 1, 100)

        if st.button("Kiểm tra bước"):

            if age2 < 18:
                st.info("12000 bước/ngày")
            elif age2 < 40:
                st.info("10000 bước/ngày")
            else:
                st.info("8000 bước/ngày")

    with tabF:

        x = [[10,1,8],[20,5,6],[25,8,3],[30,6,5]]
        y = [10,8,6,7]

        model = LinearRegression()
        model.fit(x,y)

        age = st.number_input("Tuổi",5,100)
        activity = st.slider("Hoạt động",1,10)
        screen = st.number_input("Giờ màn hình",0,24)

        if st.button("Dự đoán"):

            result = model.predict([[age,activity,screen]])[0]
            st.success(f"Bạn nên ngủ {result:.1f} giờ")

# ================= SCORE TAB =================

with tab4:

    st.title("🔘 Trình độ học sinh")

    score = st.number_input("Điểm",0,100)

    if score >= 90:
        st.success("Xuất sắc")
    elif score >= 50:
        st.info("Khá")
    elif score >= 20:
        st.warning("Trung bình")
    else:
        st.error("Trượt")

# ================= GAME TAB =================
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
            "image": "https://cdn.lazi.vn/storage/uploads/dhbc/1468933353_nhac-thinh-phong.jpg",
            "answer": "nhạc thính phòng"
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

