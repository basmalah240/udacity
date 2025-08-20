// List of available books in the shop
let products = [
  {
    name: "Beyond Good and Evil",
    author: "Friedrich Nietzsche",
    price: 7,
    quantity: 0,
    productId: 1,
    image: "./images/beyond_good_and_evil.jpeg"
  },
  {
    name: "A Room with a View",
    author: "E.M. Forster",
    price: 12,
    quantity: 0,
    productId: 2,
    image: "./images/a_room_with_a_view.jpeg"
  },
  {
    name: "Emma",
    author: "Jane Austen",
    price: 9,
    quantity: 0,
    productId: 3,
    image: "./images/emma.jpeg"
  },
  {
    name: "Night and Day",
    author: "Virginia Woolf",
    price: 23,
    quantity: 0,
    productId: 4,
    image: "./images/night_and_day.jpeg"
  },
  {
    name: "White Nights",
    author: "Fyodor Dostoevsky",
    price: 4,
    quantity: 0,
    productId: 5,
    image: "./images/white_nights.jpeg"
  },
  {
    name: "Wuthering Heights",
    author: "Emily Bronte",
    price: 8,
    quantity: 0,
    productId: 6,
    image: "./images/wuthering_heights.jpeg"
  }
];

// this is where the selected products will be stored
let cart = [];

// total money the user has paid so far
let totalPaid = 0;

// adds a product to the cart or just increases its quantity if it's already there
function getProductById(productId) {
  return products.find(p => p.productId === productId) || null;
}

function addProductToCart(productId) {
  let product = getProductById(productId);
  if (!product) {
    console.error(`Product with ID ${productId} not found.`);
    return;
  }

  product.quantity++;

  if (!cart.includes(product)) {
    cart.push(product);
  }

}


// increases the quantity of a product in the cart
function increaseQuantity(productId) {
  let product = cart.find(p => p.productId === productId);
  if (product) product.quantity++;
}

// decreases the quantity of a product, and if it reaches 0, removes it from the cart
function decreaseQuantity(productId) {
  let product = cart.find(p => p.productId === productId);
  if (product) {
    product.quantity--;
    if (product.quantity === 0) {
      removeProductFromCart(productId);
    }
  }
}

// removes a product completely from the cart (no matter its quantity)
function removeProductFromCart(productId) {
  let productIndex = cart.findIndex(p => p.productId === productId);
  if (productIndex > -1) {
    cart[productIndex].quantity = 0;
    cart.splice(productIndex, 1);
  }
}

// calculates and returns the total cost of the items in the cart
function cartTotal() {
  return cart.reduce((sum, item) => sum + item.price * item.quantity, 0);
}

// simulates payment by adding the given amount and returns the balance (positive or negative)
function pay(amount) {
  totalPaid += amount;               // Add amount to totalPaid
  let remaining = totalPaid - cartTotal();  // Calculate remaining balance

  if (remaining >= 0) {              // If fully paid or more
    emptyCart();                    // Clear the cart
    totalPaid = 0;                  // Reset totalPaid for next order
  }

  return remaining;                  // Return the balance (pos, zero, or neg)
}



// resets everything: clears the cart and resets totalPaid
function emptyCart() {
  cart.forEach(p => p.quantity = 0);
  cart = [];
  totalPaid = 0;
}
