//hinzufügen und entfernen von Artikeln

var updateBtns = document.getElementsByClassName("update-cart");
for (i = 0; i < updateBtns.length; i++) {
  updateBtns[i].addEventListener("click", function () {
    var productId = this.dataset.product;
    var action = this.dataset.action;
    console.log("ProduktID:", productId, "Aktion:", action);
    console.log("Kunde:", user);

    //user ist in index.html definiert
    if (user == "AnonymousUser") {
      addCookieItem(productId, action);
    }
  });
}

// Warenkorb wird via Cookie gefüllt
function addCookieItem(productId, action) {
  console.log("addCookieItem");
  // hinzugfügen von Artikeln
  if (action == "add") {
    // wenn Menge:0 auf 1 gesetzt
    if (cart[productId] == undefined) {
      cart[productId] = { quantity: 1 };
    } else {
      // wenn Menge 1 oder höher + 1
      cart[productId]["quantity"] += 1;
    }
  }
  // Menge -1
  if (action == "remove") {
    cart[productId]["quantity"] -= 1;
    console.log("Artikel entfernt");
    // wenn Menge <= 0, Artiekl entfernen
    if (cart[productId]["quantity"] <= 0) {
      console.log("Artikel gelöscht");
      delete cart[productId];
    }
  }
  console.log("WK:", cart);
  document.cookie = "cart=" + JSON.stringify(cart) + ";domain=;path=/";
  // wenn ";domain=path=/" nicht gesetzt wird, wird der Warenkorb jedesmal neu gesetzt
  location.reload();
}
