var randomNumber1 = Math.floor(Math.random() * 6) + 1;


var randomDiceImage = "dice" + randomNumber1 + ".png";


var randomImageSource = "images/" + randomDiceImage;


var image1 = document.querySelectorAll("img")[0];


image1.setAttribute("src", randomImageSource);

// var randomNumber2 = Math.floor(Math.random() * 6) + 1;

// var randomDiceImage1 = "images/dice" + randomNumber1 + ".png";
// var randomdiceImage2 = "images/dice" + randomNumber2 + ".png";
//
// var image1 = document.querySelectorAll("img")[0];
// var image2 = document.querySelectorAll("img")[1];
//
// image1.setAttribute("src", randomDiceImage1);
// image2.setAttribute("src", randomDiceImage2);
