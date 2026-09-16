const page = location.pathname.split("/").pop() || "index.html";
document.querySelectorAll(".sidebar nav a").forEach((link) => {
  const href = link.getAttribute("href");
  if (href === page || (page === "" && href === "index.html")) {
    link.classList.add("active");
  }
});
