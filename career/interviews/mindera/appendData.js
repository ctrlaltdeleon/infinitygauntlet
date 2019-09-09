var apiUrl = "/career/interviews/mindera/db.json";

fetch(apiUrl)
  .then(response => {
    return response.json();
  })
  .then(data => {
    // Go a level deeper to work with the cards instead of the whole object.
    console.log("Work with the JSON data here: ", data.cards);
    appendData(data.cards);
  })
  .catch(err => {
    console.log("Work with the errors here:", err);
  });

function appendData(cards) {
  for (var index = 0; index < cards.length; index++) {
    var v = cards[index];
    var amountOfCardsOnScreen = 3;

    // Create each card dynamically.
    var card = document.createElement("div");
    card.className = "card";
    card.appendChild(document.createElement("img")).src = v.image_url;
    var title = document.createElement("div");
    title.className = "title";
    card.appendChild(title).innerHTML = v.title;
    var author = document.createElement("div");
    author.className = "author";
    card.appendChild(author).innerHTML = "Author: " + v.author;
    var text = document.createElement("div");
    text.className = "text";
    card.appendChild(text).innerHTML = v.text;
    var learn = document.createElement("a");
    learn.className = "learn";
    learn.setAttribute("href", "./batman.jpg");
    card.appendChild(learn).innerHTML = "Learn More";

    // Have 3 cards initially given.
    if (index < amountOfCardsOnScreen) {
      card.style.display = "inline-block";
    } else {
      card.style.display = "none";
    }

    document.getElementsByClassName("cards")[0].appendChild(card);
  }
}
