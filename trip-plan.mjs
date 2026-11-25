// One text representation is used for preview, copying, email and print.
export const MAX_MAILTO_LENGTH = 2000; // Conservative handoff policy, not a universal client limit.
export const FIELDS = [
  ["tripDate", "Date of trip", true, "date"],
  ["departureTime", "Departure", true, "time"],
  ["people", "People", true],
  ["groupSize", "Number of people / dogs"],
  ["startingPoint", "Starting point", true],
  ["destination", "Destination", true],
  ["route", "Planned route", true],
  ["turnaround", "Turnaround", false, "datetime"],
  ["expectedReturn", "Expected return", true, "datetime"],
  ["contactNumbers", "Contact numbers", true],
  ["vehicle", "Vehicle"],
  ["satellite", "Satellite messenger"],
  ["medical", "Medical notes"],
  ["equipment", "Equipment"],
  [
    "callDeadline",
    "CALL 9-1-1 IF WE HAVE NOT RETURNED OR CHECKED IN BY",
    true,
    "datetime",
  ],
];
const clean = (value) =>
  String(value ?? "")
    .replace(/\r\n?/g, "\n")
    .trim();
function validDate(value) {
  if (!/^\d{4}-\d{2}-\d{2}$/.test(value)) return false;
  const date = new Date(value + "T00:00:00Z");
  return (
    Number.isFinite(date.getTime()) && date.toISOString().slice(0, 10) === value
  );
}
const validTime = (value) => /^(?:[01]\d|2[0-3]):[0-5]\d$/.test(value);
const validDateTime = (value) =>
  validDate(value.slice(0, 10)) &&
  value[10] === "T" &&
  validTime(value.slice(11));
export function validatePlan(data) {
  data = Object.fromEntries(FIELDS.map(([key]) => [key, clean(data[key])]));
  const errors = {};
  for (const [key, , required, type] of FIELDS) {
    const value = clean(data[key]);
    if (!value && required) errors[key] = "Complete this field.";
    else if (
      value &&
      ((type === "date" && !validDate(value)) ||
        (type === "time" && !validTime(value)) ||
        (type === "datetime" && !validDateTime(value)))
    ) {
      errors[key] = "Enter a valid date or time.";
    }
  }
  const departure = clean(data.tripDate) + "T" + clean(data.departureTime);
  if (
    !errors.tripDate &&
    !errors.departureTime &&
    !errors.expectedReturn &&
    data.expectedReturn <= departure
  ) {
    errors.expectedReturn = "Expected return must be after departure.";
  }
  if (
    !errors.expectedReturn &&
    !errors.callDeadline &&
    data.callDeadline < data.expectedReturn
  ) {
    errors.callDeadline =
      "The calling deadline cannot be earlier than expected return.";
  }
  if (
    data.turnaround &&
    !errors.turnaround &&
    !errors.tripDate &&
    !errors.departureTime &&
    !errors.expectedReturn &&
    (data.turnaround < departure || data.turnaround > data.expectedReturn)
  ) {
    errors.turnaround =
      "Turnaround must be between departure and expected return.";
  }
  return errors;
}
export function formatDate(value) {
  if (!value) return "Not provided";
  const [year, month, day] = value.slice(0, 10).split("-");
  const months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
  ];
  const date = `${Number(day)} ${months[Number(month) - 1]} ${year}`;
  return value.includes("T") ? `${date} at ${value.slice(11)}` : date;
}
export function planText(data) {
  const lines = [
    "TRIP PLAN",
    "All dates and times are local to this trip.",
    "",
  ];
  // Keep the contact's calling trigger on the first printed page, even with long notes.
  const textFields = [
    FIELDS.find(([key]) => key === "callDeadline"),
    ...FIELDS.filter(([key]) => key !== "callDeadline"),
  ];
  for (const [key, label, , type] of textFields) {
    let value = clean(data[key]);
    if (key === "departureTime")
      value = value ? formatDate(data.tripDate + "T" + value) : "";
    else if (value && (type === "date" || type === "datetime"))
      value = formatDate(value);
    lines.push(label + ":", value || "Not provided", "");
  }
  lines.push(
    "Please keep this plan and agree the calling deadline with us. If we miss it, call 9-1-1 and share this plan.",
    "",
    "This is not an official rescue site. In an emergency, call 9-1-1.",
  );
  return lines.join("\n");
}
export function emailDraft(data, recipient = "") {
  recipient = clean(recipient);
  // A single simple address is sufficient; the user can choose recipients in their mail app.
  if (
    recipient &&
    (!/^[^\s@,;<>]+@[^\s@,;<>]+$/.test(recipient) || /[\r\n]/.test(recipient))
  ) {
    return {
      error: "Please enter one valid email address, or leave it blank.",
    };
  }
  const to = recipient
    ? recipient.split("@").map(encodeURIComponent).join("@")
    : "";
  const destination = clean(data.destination).replace(/\n/g, " ");
  const subject = `Trip plan — ${destination} — ${formatDate(data.tripDate)}`;
  const uri = `mailto:${to}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(planText(data).replace(/\n/g, "\r\n"))}`;
  if (uri.length > MAX_MAILTO_LENGTH)
    return {
      error:
        "This plan is too long to open reliably as an email draft. Copy the complete text into a message instead.",
    };
  return { uri };
}

function attachPlanner() {
  const form = document.querySelector("#trip-form");
  if (!form) return;
  const review = document.querySelector("#plan-review");
  const output = document.querySelector("#plan-text");
  const printed = document.querySelector("#plan-print");
  const status = document.querySelector("#planner-status");
  const errorsBox = document.querySelector("#form-errors");
  const email = document.querySelector("#email-to");
  let reviewedData = null;
  const read = () =>
    Object.fromEntries(
      FIELDS.map(([key]) => [key, clean(form.elements.namedItem(key).value)]),
    );
  function clearErrors() {
    errorsBox.hidden = true;
    for (const [key] of FIELDS) {
      form.elements.namedItem(key).removeAttribute("aria-invalid");
      document.getElementById(key + "-error").textContent = "";
    }
  }
  function makeReview(report = true) {
    const data = read();
    const errors = validatePlan(data);
    clearErrors();
    for (const [key, message] of Object.entries(errors)) {
      form.elements.namedItem(key).setAttribute("aria-invalid", "true");
      document.getElementById(key + "-error").textContent = message;
    }
    if (Object.keys(errors).length) {
      reviewedData = null;
      review.hidden = true;
      printed.textContent = "";
      document.body.classList.remove("plan-reviewed");
      errorsBox.hidden = false;
      if (report) form.elements.namedItem(Object.keys(errors)[0]).focus();
      return false;
    }
    reviewedData = data;
    output.value = planText(data);
    printed.textContent = output.value;
    review.hidden = false;
    document.body.classList.add("plan-reviewed");
    if (report) {
      status.textContent = "Review ready. Check the plan below before sharing.";
      review.querySelector("h2").focus();
    }
    return true;
  }
  form.addEventListener("submit", (event) => {
    event.preventDefault();
    makeReview();
  });
  form.addEventListener("input", () => {
    if (reviewedData)
      status.textContent =
        "Your plan has changed. Review it again before sharing.";
    reviewedData = null;
    review.hidden = true;
    output.value = "";
    printed.textContent = "";
    document.body.classList.remove("plan-reviewed");
  });
  form.addEventListener("reset", () => {
    reviewedData = null;
    review.hidden = true;
    output.value = "";
    printed.textContent = "";
    email.value = "";
    clearErrors();
    document.body.classList.remove("plan-reviewed");
    status.textContent =
      "Form cleared. The website has not saved your entries.";
  });
  document.querySelector("#copy-plan").addEventListener("click", async () => {
    if (!reviewedData) return;
    try {
      await navigator.clipboard.writeText(output.value);
      status.textContent =
        "Plan text copied. Paste it into your message and send it yourself.";
    } catch {
      output.focus();
      output.select();
      status.textContent =
        "Copy is unavailable. The plan text is selected; copy it manually.";
    }
  });
  document.querySelector("#email-plan").addEventListener("click", () => {
    if (!reviewedData) return;
    if (!email.checkValidity()) {
      email.reportValidity();
      return;
    }
    const result = emailDraft(reviewedData, email.value);
    if (result.error) {
      status.textContent = result.error;
      status.focus();
      return;
    }
    const link = document.createElement("a");
    link.href = result.uri;
    link.hidden = true;
    document.body.append(link);
    link.click();
    link.remove();
    status.textContent =
      "Check your email app for the draft. If it does not open, copy the plan text instead. You still need to send the message yourself.";
  });
  document.querySelector("#print-plan").addEventListener("click", () => {
    if (makeReview(false)) window.print();
  });
  window.addEventListener("beforeprint", () => makeReview(false));
  form.hidden = false;
  document.querySelector("#online-unavailable").hidden = true;
}
if (typeof document !== "undefined") attachPlanner();
