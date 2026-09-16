const store = JSON.parse(localStorage.getItem("sts-draft") || "{}");

document.querySelectorAll("[data-key]").forEach((el) => {
  const key = el.dataset.key;
  if (el.type === "checkbox") {
    el.checked = Boolean(store[key]);
  } else if (store[key]) {
    el.value = store[key];
  }

  const save = () => {
    store[key] = el.type === "checkbox" ? el.checked : el.value;
    localStorage.setItem("sts-draft", JSON.stringify(store));
  };

  el.addEventListener("input", save);
  el.addEventListener("change", save);
});

const page = (location.pathname.split("/").pop() || "index.html");
document.querySelectorAll(".sidebar nav a").forEach((link) => {
  const href = link.getAttribute("href");
  if (href === page || (page === "" && href === "index.html")) {
    link.classList.add("active");
  }
});
