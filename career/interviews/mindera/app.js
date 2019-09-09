// Reviving shortly...

// (function() {
//   var Slider = function(elem, slidesLength) {
//     var cards_per_view = slidesLength,
//       last_card_index = -1,
//       current_slider_pos = 0,
//       card_width = 334,
//       start_card = 0;

//     var s = this;

//     s.init = function() {
//       s.getServerData();

//       var prev = document.getElementById("prev"),
//         next = document.getElementById("next");

//       prev.onclick = function() {
//         s.onClickPrev();
//       };
//       next.onclick = function() {
//         s.onClickNext();
//       };
//     };

//     s.getServerData = function(callback) {
//       var xhr = new XMLHttpRequest(),
//         data = null,
//         start = last_card_index + 1,
//         end = start + cards_per_view;

//       xhr.open(
//         "GET",
//         "http://127.0.0.1:3000/cards?_start=" + start + "&_end=" + end,
//       );
//       xhr.setRequestHeader("Content-Type", "application/json");
//       xhr.onload = function() {
//         if (xhr.status === 200) {
//           data = JSON.parse(xhr.responseText);
//           data.forEach(s.addLiElement);
//           if (data.length > 0) {
//             if (data.length < cards_per_view) {
//               last_card_index += data.length;
//             } else {
//               last_card_index = end - 1;
//             }
//           }

//           if (callback && start_card + cards_per_view - 1 < last_card_index) {
//             callback();
//           }
//         } else {
//           console.log(xhr.status);
//         }
//       };
//       xhr.send();
//     };

//     s.addLiElement = function(obj, index) {
//       var li = document.createElement("li"),
//         ul = document.getElementById(elem),
//         li_html = "";

//       li_html =
//         '<div class="card-image">\
//                     <img src="' +
//         obj.image_url +
//         '" />\
//                 </div>\
//                 <div class="card-content">\
//                     <div class="card-container">\
//                         <img src="" />\
//                         <div class="card-header">\
//                             <h2 class="card-title">' +
//         obj.title +
//         '</h2>\
//                             <h3 class="card-author">' +
//         obj.author +
//         '</h3>\
//                         </div>\
//                     </div>\
//                     <p class="card-text">' +
//         obj.text +
//         '</p>\
//                     <div class="card-container">\
//                         <a class="card-link" href="">Learn More</a>\
//                     </div>\
//                 </div>';

//       li.innerHTML = li_html;
//       li.className = "card";
//       ul.appendChild(li);
//     };

//     s.slideTo = function(d) {
//       var ul = document.getElementById(elem);

//       direction = d == "right" ? 1 : -1;
//       current_slider_pos = parseInt(
//         current_slider_pos + direction * card_width,
//       );

//       ul.style.transform = "translateX(" + current_slider_pos + "px)";
//       start_card -= direction;
//     };

//     s.onClickPrev = function() {
//       if (current_slider_pos < 0) {
//         s.slideTo("right");
//       }
//     };

//     s.onClickNext = function() {
//       if (
//         last_card_index >= start_card + cards_per_view - 1 ||
//         start_card == 0
//       ) {
//         s.getServerData(function() {
//           s.slideTo("left");
//         });
//       }
//     };

//     s.init();

//     return s;
//   };

//   window.Slider = Slider;
// })();

// var slider = new Slider("cards-slider", 4);
