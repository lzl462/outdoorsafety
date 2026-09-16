const store = JSON.parse(localStorage.getItem("sts-draft") || "{}");

document.querySelectorAll("[data-key]").forEach((el) => {
  const key = el.dataset.key;
  if (el.type === "checkbox") {
    el.checked = Boolean(store[key]);
  } else if (store[key]) {
    el.value = store[key];
  }

  el.addEventListener("input", () => {
    store[key] = el.type === "checkbox" ? el.checked : el.value;
    localStorage.setItem("sts-draft", JSON.stringify(store));
  });

  el.addEventListener("change", () => {
    store[key] = el.type === "checkbox" ? el.checked : el.value;
    localStorage.setItem("sts-draft", JSON.stringify(store));
  });
});

const links = [...document.querySelectorAll(".sidebar nav a")];

const setActive = () => {
  const y = window.scrollY + 80;
  let current = links[0];
  links.forEach((link) => {
    const id = link.getAttribute("href").slice(1);
    const section = document.getElementById(id);
    if (section && section.offsetTop <= y) current = link;
  });
  links.forEach((link) => link.classList.toggle("active", link === current));
};

window.addEventListener("scroll", setActive);
setActive();
