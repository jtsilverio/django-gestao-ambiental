window.onload = function () {
    var sidebar = document.getElementById('sidebarMenu');
    var d = document;

    if (sidebar) {
        var sidebarToggle = d.getElementById('sidebar-toggle');

        if (localStorage.getItem('sidebar') === 'contracted') {
            sidebar.classList.add('notransition');
            sidebar.classList.add('contracted');

            setTimeout(function () {
                sidebar.classList.remove('notransition');
            }, 500);

        } else {
            sidebar.classList.add('notransition');
            sidebar.classList.remove('contracted');

            setTimeout(function () {
                sidebar.classList.remove('notransition');
            }, 500);
        }

        sidebarToggle.addEventListener('click', function () {
            if (sidebar.classList.contains('contracted')) {
                sidebar.classList.remove('contracted');
                localStorage.removeItem('sidebar', 'contracted');
            } else {
                sidebar.classList.add('contracted');
                localStorage.setItem('sidebar', 'contracted');
            }
        });
    }
};
