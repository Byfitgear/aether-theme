(function() {
    var stored = localStorage.getItem('aether-dark-mode');
    var isDark = false;

    if (stored === 'true') {
        isDark = true;
    } else if (stored === 'false') {
        isDark = false;
    } else if (!('aether-dark-mode' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches) {
        isDark = true;
    }

    function updateIcons() {
        document.getElementById('icon-sun').classList.toggle('hidden', !isDark);
        document.getElementById('icon-moon').classList.toggle('hidden', isDark);
    }

    updateIcons();

    var btn = document.getElementById('aether-dark-toggle');
    if (btn) {
        btn.addEventListener('click', function() {
            isDark = !isDark;
            document.documentElement.classList.toggle('dark', isDark);
            localStorage.setItem('aether-dark-mode', isDark.toString());
            updateIcons();
        });
    }
})();
