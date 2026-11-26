const viewport = document.querySelector("#board-viewport");
const toggle = document.querySelector("#display-zoom");
if (viewport && toggle) {
  toggle.addEventListener("click", () => {
    const fullSize = viewport.dataset.fullSize !== "true";
    viewport.dataset.fullSize = String(fullSize);
    toggle.setAttribute("aria-pressed", String(fullSize));
    toggle.textContent = fullSize ? "Fit to screen" : "View at full size";
    viewport.scrollLeft = 0;
  });
  toggle.hidden = false;
}
