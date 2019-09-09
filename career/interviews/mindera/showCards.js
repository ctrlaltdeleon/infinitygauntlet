var cardIndex = 1;

showCards(cardIndex);

function goThroughCards(amount) {
  showCards((cardIndex += amount));
}

// This needs more work, I need to rethink about array values vs length vs incremental amounts.
// Although semi-functional, sits unwell with me. :(
function showCards(amount) {
  var cards = document.getElementsByClassName("card");

  // Reaches max length.
  if (amount > cards.length) {
    cardIndex = 1;
  }

  // Reaches below min length.
  if (amount < 1) {
    cardIndex = cards.length;
  }

  console.log("amount: ", amount);
  console.log("cardIndex: ", cardIndex);

  for (var index = 0; index < cards.length; index++) {
    cards[index].style.display = "none";
  }

  // I realize the problem is that it's not rendering in the order wanted.
  // In this case instead of 780, it's displaying 078.
  if (cardIndex === 8) {
    cards[7].style.display = "inline-block";
    cards[8].style.display = "inline-block";
    cards[0].style.display = "inline-block";
  } else if (cardIndex === 9) {
    cards[8].style.display = "inline-block";
    cards[0].style.display = "inline-block";
    cards[1].style.display = "inline-block";
  } else {
    cards[cardIndex - 1].style.display = "inline-block";
    cards[cardIndex].style.display = "inline-block";
    cards[cardIndex + 1].style.display = "inline-block";
  }
}
