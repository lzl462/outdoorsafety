// Progressive rehearsal aid: the full outline is the default and no-JS view.
const parts = [...document.querySelectorAll(".presentation-part")];
const controls = document.querySelector("#practice-controls");
const contents = document.querySelector("#presentation-parts");
const previous = document.querySelector("#practice-previous");
const next = document.querySelector("#practice-next");
const toggle = document.querySelector("#practice-toggle");
const progress = document.querySelector("#practice-progress");

if (
  parts.length &&
  controls &&
  contents &&
  previous &&
  next &&
  toggle &&
  progress
) {
  let focused = false;
  let index = 0;

  function update(moveFocus = true) {
    parts.forEach((part, number) => {
      part.hidden = focused && number !== index;
    });
    contents.hidden = focused;
    previous.hidden = next.hidden = progress.hidden = !focused;
    previous.disabled = index === 0;
    next.disabled = index === parts.length - 1;
    controls.dataset.focused = String(focused);
    toggle.textContent = focused ? "All parts" : "Practise one part";
    const heading = parts[index].querySelector("h2");
    progress.textContent = `Part ${index + 1} of ${parts.length}: ${heading.textContent.trim()}`;
    const header = document.querySelector(".site-header");
    const headerHeight =
      header && getComputedStyle(header).position === "sticky"
        ? header.getBoundingClientRect().height
        : 0;
    if (focused && moveFocus) {
      heading.focus({ preventScroll: true });
      const offset =
        headerHeight + controls.getBoundingClientRect().height + 24;
      window.scrollTo({
        top: window.scrollY + parts[index].getBoundingClientRect().top - offset,
        behavior: "instant",
      });
    } else if (moveFocus) {
      toggle.focus({ preventScroll: true });
      window.scrollTo({
        top:
          window.scrollY +
          controls.getBoundingClientRect().top -
          headerHeight -
          24,
        behavior: "instant",
      });
    }
  }

  toggle.addEventListener("click", () => {
    focused = !focused;
    update();
  });
  previous.addEventListener("click", () => {
    if (index > 0) {
      index--;
      update();
    }
  });
  next.addEventListener("click", () => {
    if (index < parts.length - 1) {
      index++;
      update();
    }
  });
  update(false);
  controls.hidden = false;
}
