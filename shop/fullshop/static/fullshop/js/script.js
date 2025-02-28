document.addEventListener('DOMContentLoaded', function() {
    const toggleBtn = document.getElementById('toggle-btn');
    const socialBar = document.querySelector('.social-bar');

    // Добавляем обработчик события на кнопку
    toggleBtn.addEventListener('click', function() {
        // Переключаем класс active у панели
        socialBar.classList.toggle('active');
    });
});

