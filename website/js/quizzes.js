function multiple_choice_check_answer(isCorrect) {
  if (isCorrect) {
    event.target.classList.add("correct")
  }
  else {
    event.target.classList.add("incorrect")
  }
}

function changeclass() {
  let selectedItem = event.target.parentElement.getElementsByClassName("selected")[0];
  if (selectedItem != null)
    selectedItem.classList.remove("selected");
  event.target.classList.add("selected");
}


function fillin_check_answer(blank) {
  if (event.target.value.toLowerCase() == blank.toLowerCase()) {
    event.target.classList.add("correct");
    event.target.disabled = true;
    event.target.parentElement.nextElementSibling.firstElementChild.focus();
  }
}

function matching_check_answer(responseA, responseB) {
  let leftItem = document.getElementById(responseA);
  let rightItem = document.getElementById(responseB);
  if (leftItem.classList.contains("selected") == true && rightItem.classList.contains("selected") == true) {
    leftItem.onclick = function () { return false; };
    leftItem.classList.add("disabled");
    rightItem.onclick = function () { return false; };
    rightItem.classList.add("disabled");
    rightColSelected = false;
    leftColSelected = false;
  }

}

// Drop-down animation
$(".collapsible").click(function (event) {
  this.classList.toggle("active");
  var content = this.nextElementSibling;
  if (content.style.maxHeight) {
    content.style.maxHeight = null;
  } else {
    content.style.display = "block";
    content.style.maxHeight = content.scrollHeight + "px";
  }
});

//Help animation
$(".help-circle").click(function (event) {
  var content = this.parentElement.parentElement.lastElementChild;
  if (content.style.maxWidth) {
    content.style.maxWidth = null;
    content.style.display = "none";
  } else {
    content.style.display = "block";
    content.style.maxWidth = (content.parentElement.scrollWidth * .7) + "px";
  }
});

$(".help-x").click(function (event) {
  var content = this.parentElement;
  if (content.style.maxWidth) {
    content.style.display = "none";
    content.style.maxWidth = null;
  } else {
    content.style.display = "block";
    content.style.maxWidth = (content.parentElement.scrollWidth * .7) + "px";
  }
});

// Event listeners for question responses
$(".matching-response").click(changeclass);
$(".matching-response").click(function () {
  matching_check_answer($(this).attr("data-text"), $(this).attr("data-correct"))
});
$(".mc-response").click(function() {
  multiple_choice_check_answer($(this).attr("data-correct"));
});

// Setup and randomize matching questions
var leftColSelected = false;
var rightColSelected = false;
var ul = document.querySelectorAll('.matching-col');
for (let i = 0; i < ul.length; i++) {
  for (var j = ul[i].children.length; j >= 0; j--) {
    ul[i].appendChild(ul[i].children[Math.random() * j | 0]);

  }
}

// Replace blanks from fillin the blank questions with input boxes
var lines = document.querySelectorAll('.fillin-line');
for (let i = 0; i < lines.length; i++) {
  lines[i].innerHTML = lines[i].innerHTML.replace(/_+/, "<input class='blank' type='text' oninput='fillin_check_answer(this.parentElement.dataset.blank)'>");
  lines[i].firstElementChild.setAttribute('size', lines[i].dataset.blank.length);
}