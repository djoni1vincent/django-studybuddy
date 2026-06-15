// Menu

const dropdownMenu = document.querySelector(".dropdown-menu");
const dropdownButton = document.querySelector(".dropdown-button");

if (dropdownButton) {
  dropdownButton.addEventListener("click", () => {
    dropdownMenu.classList.toggle("show");
  });
}

// Topics More Toggle

const topicsToggle = document.getElementById("topicsMore");
if (topicsToggle) {
  let expanded = false;
  topicsToggle.addEventListener("click", () => {
    expanded = !expanded;
    const hiddenItems = document.querySelectorAll(".topics__more");
    hiddenItems.forEach((item) => {
      item.style.display = expanded ? "list-item" : "none";
    });
    const chevron = topicsToggle.querySelector("svg");
    if (chevron) {
      chevron.style.transform = expanded ? "rotate(180deg)" : "rotate(0deg)";
    }
    topicsToggle.querySelector("svg").previousSibling.textContent = expanded
      ? " Less"
      : "More ";
  });
}

// Upload Image
const photoInput = document.querySelector("#avatar");
const photoPreview = document.querySelector("#preview-avatar");
if (photoInput)
  photoInput.onchange = () => {
    const [file] = photoInput.files;
    if (file) {
      photoPreview.src = URL.createObjectURL(file);
    }
  };

// Scroll to Bottom
const conversationThread = document.querySelector(".room__box");
if (conversationThread) conversationThread.scrollTop = conversationThread.scrollHeight;
