document.addEventListener('DOMContentLoaded', function () {
    var dropdowns = document.querySelectorAll('.dropdown');
    var profileMenuButton = document.getElementById('profileMenuButton');
    var profileMenu = document.getElementById('profile-menu');
    var datesMenu = document.getElementById('dates-menu');

    profileMenuButton.addEventListener('click', function (event) {
        var isMenuVisible = profileMenu.style.display === 'block';
        closeAllMenus();
        if (!isMenuVisible) {
            profileMenu.style.display = 'block';
        }
        event.stopPropagation();
    });

    dropdowns.forEach(function (dropdown) {
        dropdown.addEventListener('click', function (event) {
            var menuId = event.target.getAttribute('data-menu') + '-menu';
            var menu = document.getElementById(menuId);

            var isMenuVisible = menu.style.display === 'block';
            closeAllMenus();
            if (!isMenuVisible) {
                menu.style.display = 'block';
                positionMenu(event.target, menu);

                if (menuId === 'dates-menu') {
                    initCalendar(menu);
                }
            }
            event.stopPropagation();
        });
    });

    function closeAllMenus() {
        document.querySelectorAll('.dropdown-content').forEach(function (menu) {
            menu.style.display = 'none';
        });
        dropdowns.forEach(function (elem) {
            elem.classList.remove('active');
        });
    }

    function positionMenu(dropdown, menu) {
        var dropdownRect = dropdown.getBoundingClientRect();
        menu.style.top = `${dropdownRect.bottom}px`;
        menu.style.left = `${dropdownRect.left}px`;
    }

    window.addEventListener('click', function () {
        closeAllMenus();
    });

    function initCalendar(menuElement) {
        if (!menuElement.querySelector('.fullcalendar')) {
            var calendarEl = document.createElement('div');
            calendarEl.className = 'fullcalendar';
            menuElement.appendChild(calendarEl);

            var calendar = new FullCalendar.Calendar(calendarEl, {
                locale: 'ru',
                initialView: 'dayGridMonth',
                dateClick: function (info) {
                    alert('Выбранная дата: ' + info.dateStr);
                }
            });
            calendar.render();
        }
    }
});
