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
});
