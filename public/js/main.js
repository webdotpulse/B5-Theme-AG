// Main JS for Arsela Gjonaj

document.addEventListener('DOMContentLoaded', () => {
    // Go to Top Button
    const goToTopBtn = document.getElementById('goToTopBtn');

    if (goToTopBtn) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 300) {
                goToTopBtn.classList.remove('d-none');
            } else {
                goToTopBtn.classList.add('d-none');
            }
        });

        goToTopBtn.addEventListener('click', () => {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

    // Language Changer Mock Functionality
    const langItems = document.querySelectorAll('.lang-item');
    const langDisplay = document.querySelector('#languageDropdown');

    if (langItems.length > 0 && langDisplay) {
        langItems.forEach(item => {
            item.addEventListener('click', (e) => {
                e.preventDefault();
                const lang = e.target.getAttribute('data-lang');
                langDisplay.innerHTML = `<i class="bi bi-globe"></i> ${lang}`;
            });
        });
    }

    // Gallery Lightbox Logic
    const galleryItems = document.querySelectorAll('.gallery-item');
    const lightboxCarousel = document.getElementById('lightboxCarousel');

    if (galleryItems.length > 0 && lightboxCarousel) {
        // Initialize carousel but pause it
        const carousel = new bootstrap.Carousel(lightboxCarousel, {
            interval: false // Disable auto-cycling
        });

        galleryItems.forEach(item => {
            item.addEventListener('click', () => {
                const slideIndex = parseInt(item.getAttribute('data-bs-slide-to'));
                carousel.to(slideIndex);
            });
        });
    }

    // Admin Sidebar Toggle
    const sidebarToggle = document.getElementById('sidebarToggle');
    const adminSidebar = document.getElementById('adminSidebar');

    if (sidebarToggle && adminSidebar) {
        sidebarToggle.addEventListener('click', () => {
            adminSidebar.classList.toggle('show');
        });

        // Close sidebar when clicking outside on mobile
        document.addEventListener('click', (e) => {
            if (window.innerWidth < 992) {
                if (!adminSidebar.contains(e.target) && !sidebarToggle.contains(e.target) && adminSidebar.classList.contains('show')) {
                    adminSidebar.classList.remove('show');
                }
            }
        });
    }
});
