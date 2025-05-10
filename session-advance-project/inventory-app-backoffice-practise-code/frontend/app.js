
const form = document.getElementById('product-form');
const list = document.getElementById('product-list');

form.addEventListener('submit', async (e) => {
  e.preventDefault();

  const product = {
    name: document.getElementById('name').value,
    price: parseFloat(document.getElementById('price').value),
    details: document.getElementById('details').value,
    category: document.getElementById('category').value,
    quantity: parseInt(document.getElementById('quantity').value)
  };

  await fetch("/api/products/", {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(product)
  });

  form.reset();
  loadProducts();
});

function loadProducts() {
  fetch("/api/products/")
    .then(res => res.json())
    .then(data => {
      list.innerHTML = '';
      data.forEach(item => {
        const row = document.createElement('tr');
        row.innerHTML = `
          <td>${item.name}</td>
          <td>₹${item.price}</td>
          <td>${item.quantity}</td>
          <td><button onclick="deleteProduct('${item.id}')">🗑️ Mark Sold</button></td>
        `;
        list.appendChild(row);
      });
    });
}

function deleteProduct(id) {
  fetch(`/api/products/${id}`, {
    method: "DELETE"
  }).then(() => loadProducts());
}


loadProducts();
