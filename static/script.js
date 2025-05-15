document.getElementById('shopButton').addEventListener('click', function(e) {
    e.preventDefault();
    alert('Welcome to the shop! (This is a demo - add your store link here)');
});

document.addEventListener('DOMContentLoaded', function() {
    const btn = document.getElementById('userDropdownBtn');
    const dropdown = document.getElementById('userDropdown');

    if (btn && dropdown) {
        btn.addEventListener('click', function(e) {
            e.stopPropagation();
            dropdown.classList.toggle('show');
        });

        // Close dropdown when clicking outside
        document.addEventListener('click', function(e) {
            if (!dropdown.contains(e.target)) {
                dropdown.classList.remove('show');
            }
        });
    }
});