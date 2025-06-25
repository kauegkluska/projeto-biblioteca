function loadHTML(id, path) {
  fetch(path)
    .then(response => {
      if (!response.ok) {
        throw new Error('Erro ao carregar ' + path);
      }
      return response.text();
    })
    .then(html => {
      document.getElementById(id).innerHTML = html;
    })
    .catch(error => {
      console.error(error);
    });
}

window.addEventListener('DOMContentLoaded', () => {
  loadHTML('header', 'layout/header.html');
  loadHTML('menu', 'layout/navbar.html');
  loadHTML('footer', 'layout/footer.html');
});
