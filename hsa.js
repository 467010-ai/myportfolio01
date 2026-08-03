// ==========================================
// 1. Mobile Menu Toggle
// ==========================================
const hamburger = document.querySelector('.hamburger');
const navLinks = document.querySelector('.nav-links');

hamburger.addEventListener('click', () => {
    navLinks.classList.toggle('active');
});

// ปิดเมนูเมื่อคลิกที่ลิงก์ในหน้ามือถือ
document.querySelectorAll('.nav-links a').forEach(link => {
    link.addEventListener('click', () => {
        navLinks.classList.remove('active');
    });
});

// ==========================================
// 2. Modal Pop-up Functionality
// ==========================================
const modal = document.getElementById('imageModal');
const modalImg = document.getElementById('modalImg');
const modalTitle = document.getElementById('modalTitle');
const modalDesc = document.getElementById('modalDesc');

function openModal(imgSrc, title, description) {
    modal.style.display = "block";
    modalImg.src = imgSrc;
    modalTitle.textContent = title;
    modalDesc.textContent = description;
}

function closeModal() {
    modal.style.display = "none";
}

// ปิด Modal เมื่อคลิกพื้นที่ภายนอกรูป
window.addEventListener('click', (event) => {
    if (event.target === modal) {
        closeModal();
    }
});

// ==========================================
// 3. Navbar background shadow on scroll
// ==========================================
window.addEventListener('scroll', () => {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 50) {
        navbar.style.boxShadow = '0 2px 15px rgba(0, 0, 0, 0.15)';
    } else {
        navbar.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.1)';
    }
});
