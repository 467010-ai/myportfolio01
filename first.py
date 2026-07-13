<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portfolio | SOP สื่อสารมวลชน</title>
    
    <!-- นำเข้าฟอนต์ Prompt จาก Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;500;600&display=swap" rel="stylesheet">

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: "Prompt", sans-serif;
        }

        body {
            background: #111827;
            color: white;
            line-height: 1.8;
        }

        header {
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
            background: linear-gradient(135deg, #111827, #1e3a8a);
        }

        header h1 {
            font-size: 55px;
            font-weight: 600;
            letter-spacing: 2px;
            background: linear-gradient(to right, #ffffff, #60a5fa);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        header p {
            margin-top: 10px;
            font-size: 22px;
            color: #9ca3af;
        }
        
        header .faculty {
            color: #60a5fa;
            font-weight: 500;
        }

        section {
            max-width: 900px;
            margin: auto;
            padding: 60px 25px;
            display: flex;
            flex-direction: column;
            gap: 40px; /* เว้นระยะห่างระหว่างการ์ด */
        }

        .card {
            background: #1f2937;
            padding: 35px;
            border-radius: 18px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, .35);
        }

        h2 {
            color: #60a5fa;
            margin-bottom: 25px;
            font-size: 32px;
            font-weight: 500;
        }

        p {
            margin-bottom: 18px;
            color: #e5e7eb;
            font-weight: 300;
        }

        /* ----------------------------------------------- */
        /* ส่วนที่แก้ไขเพิ่มเติม: ปรับแต่ง About Card ให้เข้ากับ Dark Mode */
        /* ----------------------------------------------- */
        .about-card {
            display: flex;
            align-items: center;
            gap: 30px;
        }

        .about-card img {
            width: 160px;
            height: 160px;
            border-radius: 50%;
            object-fit: cover;
            border: 4px solid #60a5fa;
            flex-shrink: 0;
        }

        .about-text {
            display: flex;
            flex-direction: column;
            gap: 8px;
        }

        .about-text h3 {
            font-size: 24px;
            color: #ffffff;
            font-weight: 500;
            margin-bottom: 5px;
        }

        .about-text .school {
            color: #9ca3af;
            font-size: 16px;
            margin-bottom: 10px;
        }

        /* สไตล์ของแท็กทักษะ (Skills Tags) */
        .skills {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin-top: 10px;
        }

        .skills span {
            background-color: #374151;
            color: #9ca3af;
            padding: 5px 14px;
            border-radius: 50px;
            font-size: 14px;
            font-weight: 400;
            transition: all 0.2s ease;
        }

        .skills span:hover {
            background-color: #60a5fa;
            color: #111827;
            transform: scale(1.05);
        }

        footer {
            text-align: center;
            padding: 40px;
            color: #9ca3af;
            font-size: 14px;
            border-top: 1px solid #1f2937;
        }

        /* รองรับการแสดงผลบนมือถือ */
        @media (max-width: 650px) {
            header h1 { font-size: 40px; }
            header p { font-size: 18px; }
            
            .about-card {
                flex-direction: column;
                text-align: center;
            }
            .skills {
                justify-content: center;
            }
        }
    </style>
</head>
<body>

    <header>
        <div>
            <h1>PORTFOLIO</h1>
            <p>Statement of Purpose</p>
            <p class="faculty">คณะสื่อสารมวลชน</p>
        </div>
    </header>

    <section>
        
        <!-- การ์ดแนะนำตัว (About Card) -->
        <div class="card">
            <div class="about-card">
                <!-- ตรวจสอบให้แน่ใจว่ามีรูปภาพอยู่ในโฟลเดอร์ assets/profile.jpg นะครับ -->
                <img src="assets/profile.jpg" alt="ณัฐพิพัฒน์ บุญญธิรัตน์">
                
                <div class="about-text">
                    <h3>ณัฐพิพัฒน์ บุญญธิรัตน์</h3>
                    <p class="school">นักเรียนระดับชั้นมัธยมศึกษาปีที่ 6 โรงเรียนกระทุ่มแบน "วิเศษสมุทคุณ"</p>
                    
                    <p>ผมมีความสนใจด้านการสื่อสาร การเรียนรู้ภาษา และการสร้างสรรค์สื่อ เพราะเชื่อว่าสื่อสามารถถ่ายทอดข้อมูล ความรู้ และสร้างแรงบันดาลใจให้ผู้คนได้</p>
                    <p>ผมชื่นชอบการออกแบบกราฟิก การถ่ายภาพ การตัดต่อวิดีโอ และการสร้างคอนเทนต์ จึงมุ่งพัฒนาทักษะด้านการสื่อสาร เพื่อเตรียมความพร้อมสำหรับการศึกษาต่อในคณะสื่อสารมวลชน</p>
                    
                    <div class="skills">
                        <span>Communication</span>
                        <span>Graphic Design</span>
                        <span>Photography</span>
                        <span>Video Editing</span>
                        <span>Content Creator</span>
                    </div>
                </div>
            </div>
        </div>

        <!-- การ์ดแสดงเรียงความ (SOP Card) -->
        <div class="card">
            <h2>Statement of Purpose</h2>
            <p>
                ผมมีความสนใจด้านการสื่อสารและสื่อมวลชนมาโดยตลอด เพราะเป็นสิ่งที่อยู่รอบตัวเราในชีวิตประจำวัน ไม่ว่าจะเป็นข่าวสาร รายการโทรทัศน์ ภาพยนตร์ หรือสื่อออนไลน์ ผมชอบศึกษาวิธีการนำเสนอข้อมูลและการเล่าเรื่องที่สามารถสร้างความเข้าใจและส่งผลต่อผู้คนได้
            </p>
            <!-- คุณสามารถพิมพ์เนื้อหา SOP ย่อหน้าถัดไปเพิ่มตรงนี้ได้เลยครับ -->
        </div>

    </section>

    <footer>
        <p>&copy; 2026 ณัฐพิพัฒน์ บุญญธิรัตน์. All Rights Reserved.</p>
    </footer>

</body>
</html>
