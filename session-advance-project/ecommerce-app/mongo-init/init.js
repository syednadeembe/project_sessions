db = db.getSiblingDB('ecommerce');

db.products.insertMany([
  {
    name: "Laptop",
    price: 75000,
    description: "High-end laptop",
    in_stock: true
  },
  {
    name: "Phone",
    price: 40000,
    description: "Smartphone with great camera",
    in_stock: true
  }
]);
