document.addEventListener('DOMContentLoaded', function() {
  const navLinks = document.querySelectorAll('.navbar-custom .nav-link');

  for (const link of navLinks) {
    link.addEventListener('click', function(e) {
      e.preventDefault();
      const targetId = this.getAttribute('href').substring(1);
      const target = document.getElementById(targetId);
      if (target) {
        const offset = target.offsetTop - 70;
        window.scrollTo({
          top: offset,
          behavior: 'smooth'
        });
      }
    });
  }
});

