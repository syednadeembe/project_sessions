db = db.getSiblingDB('ecommerce');
db.products.insertMany([
  { name: "Demo Item", price: 1999, category: "Electronics", stock: 25 }
]);