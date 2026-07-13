# myportfolio01
<section id="about">
/* กำหนดฟอนต์และสไตล์พื้นฐานให้กับ Card */
.about-card {
  display: flex;
  align-items: center;
  gap: 24px;
  background-color: #ffffff;
  padding: 24px;
  border-radius: 16px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  max-width: 650px;
  margin: 20px auto;
  font-family: 'Kanit', sans-serif; /* แนะนำให้ใช้ฟอนต์แนวโมเดิร์น */
  transition: transform 0.3s ease;
}

/* เพิ่มลูกเล่นเวลาเอาเมาส์ไปวาง (Hover Effect) */
.about-card:hover {
  transform: translateY(-5px);
}

/* จัดการส่วนรูปภาพโปรไฟล์ */
.about-card img {
  width: 150px;
  height: 150px;
  border-radius: 50%; /* ปรับรูปเป็นวงกลม */
  object-fit: cover;
  border: 3px solid #6c5ce7; /* เพิ่มเส้นขอบสีเด่นๆ ตามธีมที่ชอบ */
  flex-shrink: 0;
}

/* จัดการส่วนกล่องข้อความ */
.about-text {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

/* หัวข้อชื่อ-นามสกุล */
.about-text h3 {
  margin: 0;
  font-size: 1.5rem;
  color: #2d3436;
}

/* รายละเอียดและคำโปรย */
.about-text p {
  margin: 0;
  font-size: 0.95rem;
  color: #636e72;
  line-height: 1.6;
}

/* จัดวางกลุ่มแท็กทักษะ (Skills) */
.skills {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 8px;
}

/* ตกแต่งแท็กทักษะแต่ละชิ้น */
.skills span {
  background-color: #f1f2f6;
  color: #57606f;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 0.85rem;
  font-weight: 500;
  transition: all 0.2s ease;
}

/* ลูกเล่นเวลาชี้ไปที่แท็กทักษะ */
.skills span:hover {
  background-color: #6c5ce7;
  color: #ffffff;
}

/* รองรับการแสดงผลบนมือถือ (Responsive) */
@media (max-width: 600px) {
  .about-card {
    flex-direction: column;
    text-align: center;
    padding: 20px;
  }
  
  .skills {
    justify-content: center;
  }
}
</section>
<!DOCTYPE html>
<html lang="th">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Portfolio | SOP สื่อสารมวลชน</title>

<style>
*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:"Prompt",sans-serif;
}

body{
    background:#111827;
    color:white;
    line-height:1.8;
}

header{
    height:100vh;
    display:flex;
    justify-content:center;
    align-items:center;
    text-align:center;
    background:linear-gradient(135deg,#111827,#1e3a8a);
}

header h1{
    font-size:55px;
}

header p{
    margin-top:15px;
    font-size:22px;
    color:#d1d5db;
}

section{
    max-width:900px;
    margin:auto;
    padding:70px 25px;
}

.card{
    background:#1f2937;
    padding:35px;
    border-radius:18px;
    box-shadow:0 10px 30px rgba(0,0,0,.35);
}

h2{
    color:#60a5fa;
    margin-bottom:25px;
    font-size:32px;
}

p{
    margin-bottom:18px;
    color:#e5e7eb;
}

footer{
    text-align:center;
    padding:30px;
    color:#9ca3af;
}
</style>

</head>
<body>

<header>
    <div>
        <h1>Portfolio</h1>
        <p>Statement of Purpose</p>
        <p>คณะสื่อสารมวลชน</p>
    </div>
</header>

<section>

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

<footer>
© 2026 Portfolio | Nutpipat Boonyatirat
</footer>

</body>
</html>
