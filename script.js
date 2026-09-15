const menuBtn = document.querySelector(".menu-btn");
const nav = document.querySelector("nav");

if (menuBtn && nav) {
  menuBtn.addEventListener("click", () => {
    const open = nav.classList.toggle("open");
    menuBtn.setAttribute("aria-expanded", String(open));
  });

  nav.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => nav.classList.remove("open"));
  });
}

const saved = JSON.parse(localStorage.getItem("sts-checklists") || "{}");

document.querySelectorAll("label.check input").forEach((box) => {
  const key = box.dataset.key;
  if (saved[key]) box.checked = true;

  box.addEventListener("change", () => {
    saved[key] = box.checked;
    localStorage.setItem("sts-checklists", JSON.stringify(saved));
  });
});

document.getElementById("print-plan")?.addEventListener("click", () => {
  window.print();
});
