document.documentElement.classList.add("js");
// Pages keep navigation, calling links and advice usable without JavaScript.
const menu = document.querySelector(".site-menu");
if (menu) {
  const trigger = menu.querySelector("summary");
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && menu.open) {
      menu.open = false;
      trigger.focus();
    }
  });
  document.addEventListener("click", (event) => {
    if (menu.open && !menu.contains(event.target)) menu.open = false;
  });
  document.addEventListener("focusin", (event) => {
    if (menu.open && !menu.contains(event.target)) menu.open = false;
  });
}
document.querySelectorAll("[data-print-guide]").forEach((button) => {
  button.hidden = false;
  button.addEventListener("click", () => window.print());
});
// Include reminder bodies in print, then restore the reader's disclosure choices.
let openedForPrint = [];
window.addEventListener("beforeprint", () => {
  openedForPrint = [
    ...new Set([
      ...openedForPrint,
      ...document.querySelectorAll("details.tip:not([open])"),
    ]),
  ];
  openedForPrint.forEach((detail) => {
    detail.open = true;
  });
});
window.addEventListener("afterprint", () => {
  openedForPrint.forEach((detail) => {
    detail.open = false;
  });
  openedForPrint = [];
});
const boxes = [...document.querySelectorAll("[data-essential]")];
if (boxes.length) {
  const key = "outdoorsafety-essentials-v1";
  const feedback = document.querySelector(".checklist-feedback");
  const count = document.querySelector("[data-checklist-count]");
  const storageNote = document.querySelector("[data-checklist-storage]");
  let canSave = false;
  try {
    const probe = key + "-probe";
    localStorage.setItem(probe, "1");
    localStorage.removeItem(probe);
    canSave = true;
    const saved = JSON.parse(localStorage.getItem(key) || "[]");
    if (Array.isArray(saved))
      boxes.forEach((box) => {
        box.checked = saved.includes(box.dataset.essential);
      });
  } catch {
    // Native checkboxes also work when storage is unavailable.
  }
  function update(save = false) {
    const checked = boxes
      .filter((box) => box.checked)
      .map((box) => box.dataset.essential);
    if (save && canSave) {
      try {
        localStorage.setItem(key, JSON.stringify(checked));
      } catch {
        canSave = false;
      }
    }
    count.textContent = checked.length + " of " + boxes.length + " checked";
    storageNote.textContent = canSave
      ? "Saved in this browser."
      : "Checks stay in this tab.";
  }
  boxes.forEach((box) => box.addEventListener("change", () => update(true)));
  document
    .querySelector("[data-clear-checks]")
    .addEventListener("click", () => {
      boxes.forEach((box) => {
        box.checked = false;
      });
      update(true);
    });
  update();
  feedback.hidden = false;
}
