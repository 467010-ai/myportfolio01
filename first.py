<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portfolio | ณัฐพิพัฒน์ บุญญธิรัตน์</title>
    
    <!-- Google Fonts: Prompt -->
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
            background-color: #111827;
            color: #ffffff;
            line-height: 1.8;
        }

        /* Header Zone */
        header {
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
            background: linear-gradient(135deg, #111827, #1e3a8a);
            padding: 20px;
        }

        header h1 {
            font-size: 55px;
            font-weight: 600;
        }

        header p {
            margin-top: 10px;
            font-size: 22px;
            color: #d1d5db;
        }

        /* Container Section */
        section {
            max-width: 900px;
            margin: auto;
            padding: 50px 25px;
        }

        /* Card Component */
        .card {
            background: #1f2937;
            padding: 35px;
            border-radius: 18px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.35);
            margin-bottom: 40px;
        }

        h2 {
            color: #60a5fa;
            margin-bottom: 20px;
            font-size: 32px;
            border-bottom: 2px solid #374151;
            padding-bottom: 10px;
        }

        p {
            margin-bottom: 16px;
            color: #e5e7eb;
            font-size: 16px;
        }

        /* About Section Custom Layout */
        .about-card {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 25px;
            text-align: center;
        }

        @media (min-width: 640px) {
            .about-card {
                flex-direction: row;
                text-align: left;
            }
        }

        .about-card img {
            width: 160px;
            height: 160px;
            border-radius: 50%;
            object-fit: cover;
            border: 4px solid #60a5fa;
            box-shadow: 0 4px 15px rgba(0,0,0,0.3);
            flex-shrink: 0;
        }

        .about-text h3 {
            font-size: 26px;
            color: #ffffff;
            margin-bottom: 5px;
        }

        .subtitle {
            color: #9ca3af;
            font-size: 15px;
            margin-bottom: 15px;
            font-weight: 300;
        }

        /* Footer */
        footer {
            text-align: center;
            padding: 30px;
            color: #9ca3af;
            border-top: 1px solid #1f2937;
            font-size: 14px;
        }
    </style>
</head>
<body>

    <!-- Header Section -->
    <header>
        <div>
            <h1>Portfolio</h1>
            <p>Statement of Purpose</p>
            <p>คณะสื่อสารมวลชน</p>
        </div>
    </header>

    <!-- Main Content Section -->
    <section>
        
        <!-- About Me Card -->
        <div id="about" class="card">
            <h2>About Me</h2>
            <div class="about-card">
                <!-- ตรวจสอบโฟลเดอร์รูปภาพ assets/profile.jpg บน GitHub ด้วยนะครับ -->
                <img src="assets/profile.jpg" alt="ณัฐพิพัฒน์ บุญญธิรัตน์">
                
                <div class="about-text">
                    <h3>ณัฐพิพัฒน์ บุญญธิรัตน์</h3>
                    <p class="subtitle">นักเรียนระดับชั้นมัธยมศึกษาปีที่ 6 โรงเรียนกระทุ่มแบน "วิเศษสมุทคุณ"</p>
                    
                    <p>ผมมีความสนใจด้านการสื่อสาร การเรียนรู้ภาษา และการสร้างสรรค์สื่อ เพราะเชื่อว่าสื่อสามารถถ่ายทอดข้อมูล ความรู้ และสร้างแรงบันดาลใจให้ผู้คนได้</p>
                    <p>ผมชื่นชอบการออกแบบกราฟิก การถ่ายภาพ การตัดต่อวิดีโอ และการสร้างคอนเทนต์ จึงมุ่งพัฒนาทักษะด้านการสื่อสาร เพื่อเตรียมความพร้อมสำหรับการศึกษาต่อในคณะสื่อสารมวลชน</p>
                </div>
            </div>
        </div>

        <!-- SOP Card -->
        <div class="card">
            <h2>Statement of Purpose</h2>

            <p>
                ผมมีความสนใจด้านการสื่อสารและสื่อมวลชนมาโดยตลอด เพราะเป็นสิ่งที่อยู่รอบตัวเราในชีวิตประจำวัน ไม่ว่าจะเป็นข่าวสาร รายการโทรทัศน์ ภาพยนตร์ หรือสื่อออนไลน์ ผมชอบศึกษาวิธีการนำเสนอข้อมูลและการเล่าเรื่องที่สามารถสร้างความเข้าใจและส่งผลต่อผู้คนได้
            </p>

            <p>
                ในช่วงที่ศึกษาอยู่ระดับมัธยมศึกษา ผมได้พัฒนาทักษะการสื่อสารผ่านการเรียนภาษาอังกฤษ การทำงานกลุ่ม และการเข้าร่วมกิจกรรมต่าง ๆ ซึ่งช่วยให้ผมมีความกล้าแสดงออก รับฟังความคิดเห็นของผู้อื่น และสามารถทำงานร่วมกับผู้อื่นได้อย่างมีประสิทธิภาพ
            </p>

            <p>
                ผมเลือกศึกษาต่อในสาขาสื่อสารมวลชน เพราะต้องการเรียนรู้ทั้งภาคทฤษฎีและภาคปฏิบัติเกี่ยวกับการผลิตสื่อ การสื่อสารข่าวสาร และการสร้างเนื้อหาที่มีคุณภาพ เพื่อนำความรู้ไปพัฒนาตนเองและประกอบอาชีพในสายงานสื่อในอนาคต
            </p>

            <p>
                ผมเชื่อว่าความตั้งใจ ความรับผิดชอบ และความพร้อมในการเรียนรู้สิ่งใหม่ ๆ จะช่วยให้ผมประสบความสำเร็จในการศึกษา และสามารถเป็นส่วนหนึ่งในการสร้างสรรค์สื่อที่เป็นประโยชน์ต่อสังคมได้ในอนาคต
            </p>
        </div>

    </section>

    <!-- Footer -->
    <footer>
        © 2026 Portfolio | Nutpipat Boonyatirat
    </footer>

</body>
</html>
